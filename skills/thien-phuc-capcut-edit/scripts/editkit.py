"""CapCut JSON staging and honest timing reports. Python standard library only.
Never selects creative cuts, runs ASR, controls UI, or renders.
"""
import argparse
import copy
import csv
import hashlib
import json
import math
import os
from pathlib import Path
from datetime import datetime, timezone, timedelta
import uuid

TZ = timezone(timedelta(hours=7))
VERSION = '1.0'

def now():
    return datetime.now(TZ).isoformat(timespec='seconds')

def read(p):
    return json.loads(Path(p).read_text(encoding='utf-8-sig'))

def write(p, value):
    p = Path(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_name(p.name + '.tmp')
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')
    os.replace(tmp, p)

def require(ok, message):
    if not ok:
        raise ValueError(message)

def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def index(d):
    entries = [(k, m) for k, items in d['materials'].items() if isinstance(items, list)
               for m in items if isinstance(m, dict) and 'id' in m]
    result = {}
    for k, m in entries:
        require(m['id'] not in result or result[m['id']] == (k, m), 'Conflicting duplicate material IDs')
        result[m['id']] = (k, m)
    return result

def snapshot(project, timeline, out):
    project, out = Path(project).resolve(), Path(out).resolve()
    require(not out.exists(), 'Snapshot must be a new directory')
    require(not out.is_relative_to(project), 'Snapshot must be outside live project')
    active = project / 'Timelines' / timeline / 'draft_content.json'
    require(active.resolve().is_relative_to(project), 'Invalid timeline path')
    root = project / 'draft_content.json'
    require(read(root) == read(active), 'Root/active differ; inspect in CapCut first')
    d = read(root)
    index(d)
    meta = read(project / 'draft_meta_info.json')
    out.mkdir(parents=True)
    files = {}
    for name, path in [('root.json', root), ('active.json', active),
                       ('meta.json', project / 'draft_meta_info.json')]:
        (out / name).write_bytes(path.read_bytes())
        files[name] = {'path': str(path), 'sha256': digest(path)}
    write(out / 'snapshot.json', {'version': VERSION, 'project': str(project),
          'project_name': meta['draft_name'], 'timeline': timeline, 'saved_at': now(), 'files': files})
    # Compact inventory for choosing actual segment IDs; no hardcoded track numbers.
    mi = index(d)
    write(out / 'inventory.json', [{'id': t['id'], 'type': t['type'], 'name': t.get('name'),
          'segments': [{'id': s['id'], 'material_id': s['material_id'],
          'path': mi[s['material_id']][1].get('path'), 'target': s['target_timerange'],
          'source': s.get('source_timerange')} for s in t['segments']]} for t in d['tracks']])

def validate(d, roles=None, check_files=True):
    mi = index(d)
    errors, warnings, ids = [], [], set()
    duration = d['duration']
    for t in d['tracks']:
        role = (roles or {}).get(t['id'])
        previous = 0
        for s in sorted(t['segments'], key=lambda x: x['target_timerange']['start']):
            sid = s['id']
            if sid in ids:
                errors.append('Duplicate segment ' + sid)
            ids.add(sid)
            a, length = s['target_timerange']['start'], s['target_timerange']['duration']
            if not (0 <= a and length > 0 and a + length <= duration + 2):
                errors.append('Target bounds ' + sid)
            if a < previous - 2:
                errors.append('Same-track overlap ' + sid)
            if role == 'speech' and abs(a - previous) > 2:
                errors.append('Speech gap ' + sid)
            if role == 'broll' and 2 < a - previous < 500000 and previous:
                warnings.append('Review possible visible flash before ' + sid)
            previous = a + length
            if s['material_id'] not in mi:
                errors.append('Missing material ' + sid)
                continue
            m = mi[s['material_id']][1]
            for ref in s.get('extra_material_refs', []):
                if ref not in mi:
                    errors.append('Missing extra reference ' + ref)
            if check_files and m.get('path'):
                path = Path(m['path'])
                valid = path.is_file() if mi[s['material_id']][0] in ('videos', 'audios') else path.exists()
                if not valid:
                    errors.append('Missing media/resource ' + m['path'])
            sr = s.get('source_timerange')
            if sr and t['type'] in ('video', 'audio'):
                if sr['start'] < 0 or sr['start'] + sr['duration'] > m['duration'] + 20000:
                    errors.append('Source bounds ' + sid)
            if role == 'speech' and not math.isclose(s.get('volume', 0), 10 ** .5, rel_tol=1e-6):
                errors.append('Speech is not +10dB ' + sid)
            if role == 'broll' and s.get('volume') != 0:
                errors.append('B-roll not muted ' + sid)
        if role == 'speech' and abs(previous - duration) > 2:
            errors.append('Speech end does not match project')
    return {'errors': errors, 'warnings': warnings, 'duration_seconds': duration / 1e6,
            'direct_listening_verified': False, 'visual_playback_verified': False}

def build(snapshot_dir, plan_path, out):
    base, out = Path(snapshot_dir), Path(out)
    require(not out.exists(), 'Use a new staging directory per revision')
    info, plan, d = read(base / 'snapshot.json'), read(plan_path), read(base / 'root.json')
    require(plan['project_name'] == info['project_name'], 'Project name mismatch')
    require(plan.get('source_review_complete') is True, 'Review full source before selecting cuts')
    require(plan.get('review_method') in ('listened', 'asr_authorized'), 'Specify actual review method')
    if plan['review_method'] == 'asr_authorized':
        require(bool(plan.get('asr_authorization')), 'Record project-specific ASR authorization')
    fps = float(d['fps'])
    require(fps > 0, 'Invalid fps')
    def us(seconds):
        require(math.isfinite(seconds), 'Nonfinite timing')
        return round(round(seconds * fps) * 1000000 / fps)
    source_index = index(d)
    segments = {s['id']: s for t in d['tracks'] for s in t['segments']}
    tracks = {t['id']: t for t in d['tracks']}
    require(set(plan['keep_tracks']) | set(plan['drop_tracks']) | {t['id'] for t in plan['tracks']} == set(tracks),
            'Explicitly account for every existing track (keep, drop, replace)')
    listed = plan['keep_tracks'] + plan['drop_tracks'] + [t['id'] for t in plan['tracks']]
    require(len(listed) == len(set(listed)), 'Track appears in multiple actions')
    require(bool(plan.get('timing_rationale')), 'Record why kept tracks remain aligned after edits')
    d['duration'] = us(plan['duration_seconds'])
    roles = {}
    # Unique part keys disambiguate repeated source excerpts used in hook and body.
    anchors, cursor = {}, 0
    for part in plan.get('parts', []):
        require(part['key'] not in anchors, 'Duplicate part key')
        a, b = us(part['source'][0]), us(part['source'][1])
        require(b > a, 'Invalid source part')
        anchors[part['key']] = (a, b, cursor)
        cursor += b-a
    if anchors:
        require(abs(cursor-d['duration']) <= 2, 'Parts do not match planned duration')
    for tp in plan['tracks']:
        track = tracks[tp['id']]
        allowed = {'speech':'video', 'broll':'video', 'captions':'text', 'title':'text',
                   'music':'audio', 'sfx':'audio', 'effect':'effect'}
        require(tp['role'] in allowed and track['type'] == allowed[tp['role']], 'Role/track type mismatch')
        roles[track['id']] = tp['role']
        if tp['role'] == 'captions':
            require(plan['ratio'] == '9:16', 'No spoken captions for horizontal video')
        result = []
        for item in tp['clips']:
            s = copy.deepcopy(segments[item['template_segment']])
            require(not s.get('common_keyframes') and not s.get('keyframe_refs'), 'Animated clip needs a verified adapter')
            require(s.get('speed', 1) == 1, 'Speed changes need a verified adapter')
            s['id'] = str(uuid.uuid4()).upper()
            s['group_id'] = s['raw_segment_id'] = ''
            refs = []
            for ref in s.get('extra_material_refs', []):
                k, material = source_index[ref]
                material = copy.deepcopy(material)
                if material.get('type') == 'speed':
                    require(material.get('speed', 1) == 1 and not material.get('curve_speed'), 'Speed curve unsupported')
                material['id'] = str(uuid.uuid4()).upper()
                d['materials'][k].append(material)
                refs.append(material['id'])
            s['extra_material_refs'] = refs
            if 'anchor' in item:
                part_start, part_end, target_start = anchors[item['anchor']]
                left, right = map(us, item['anchor_source'])
                require(part_start <= left < right <= part_end, 'Anchor range crosses a removed boundary; split explicitly')
                a, b = target_start+left-part_start, target_start+right-part_start
            else:
                a, b = us(item['target'][0]), us(item['target'][1])
            s['target_timerange'] = {'start': a, 'duration': b-a}
            if track['type'] in ('video', 'audio'):
                source_start = us(item['source_start'])
                s['source_timerange'] = {'start': source_start, 'duration': b-a}
            if tp['role'] == 'speech':
                s['volume'] = s['last_nonzero_volume'] = 10 ** .5
            elif tp['role'] == 'broll':
                s['volume'] = 0
            if 'text' in item:
                k, material = source_index[s['material_id']]
                require(k == 'texts' and not material.get('text_info_resources'), 'Composite preset: use verified adapter/UI')
                material = copy.deepcopy(material)
                material['id'] = str(uuid.uuid4()).upper()
                for field in ('content', 'base_content'):
                    if not material.get(field):
                        continue
                    content = json.loads(material[field])
                    require('text' in content and len(content.get('styles', [])) == 1, 'Only single-style plain text supported')
                    content['text'] = item['text']
                    content['styles'][0]['range'] = [0, len(item['text'].encode('utf-16-le')) // 2]
                    if tp['role'] == 'captions':
                        require(content['styles'][0]['size'] == 8, 'Use approved Roboto-Blk 8 template')
                    material[field] = json.dumps(content, ensure_ascii=False)
                material['recognize_text'] = item['text']
                material['words'] = material['current_words'] = {'start_time': [], 'end_time': [], 'text': []}
                d['materials'][k].append(material)
                s['material_id'] = material['id']
            if 'transform' in item:
                s['clip']['transform'] = item['transform']
            result.append(s)
        track['segments'] = sorted(result, key=lambda s:s['target_timerange']['start'])
    d['tracks'] = [t for t in d['tracks'] if t['id'] not in plan['drop_tracks']]
    canvas = d['canvas_config']
    require(plan['ratio'] in ('9:16', '16:9'), 'Unsupported ratio')
    require((canvas['width'] < canvas['height']) == (plan['ratio'] == '9:16'), 'Canvas mismatch; do not crop implicitly')
    check = validate(d, roles)
    require(not check['errors'], json.dumps(check['errors'], ensure_ascii=False))
    out.mkdir(parents=True)
    meta = read(base / 'meta.json')
    meta['tm_duration'] = d['duration']
    write(out / 'draft_content.json', d)
    write(out / 'draft_meta_info.json', meta)
    write(out / 'validation.json', check)
    write(out / 'plan.json', plan)
    write(out / 'time-map.json', anchors)
    write(out / 'build.json', {'snapshot': str(base.resolve()), 'roles': roles,
          'content_sha256': digest(out / 'draft_content.json'), 'meta_sha256': digest(out / 'draft_meta_info.json')})

def install(stage, editor_closed):
    require(editor_closed, 'Save and close target editor to Home first; verify through UI')
    stage = Path(stage)
    build_info = read(stage / 'build.json')
    base = Path(build_info['snapshot'])
    snapshot_info = read(base / 'snapshot.json')
    require(digest(stage / 'draft_content.json') == build_info['content_sha256'] and
            digest(stage / 'draft_meta_info.json') == build_info['meta_sha256'], 'Stage changed; rebuild')
    check = validate(read(stage / 'draft_content.json'), build_info['roles'])
    require(not check['errors'], str(check['errors']))
    destinations = []
    for name, info in snapshot_info['files'].items():
        target = Path(info['path'])
        require(target.resolve().is_relative_to(Path(snapshot_info['project']).resolve()), 'Invalid target')
        require(digest(target) == info['sha256'], 'Live project changed: take fresh snapshot, do not overwrite')
        require(digest(base / name) == info['sha256'], 'Backup changed')
        destinations.append((target, base / name, stage / ('draft_meta_info.json' if name == 'meta.json' else 'draft_content.json')))
    touched = []
    try:
        for target, backup, source in destinations:
            touched.append((target, backup))
            target.write_bytes(source.read_bytes())
            require(digest(target) == digest(source), 'Write verification failed')
    except BaseException:
        for target, backup in touched:
            target.write_bytes(backup.read_bytes())
        raise
    write(stage / 'installed.json', {'installed_at': now(), 'rendered': False})

def log_event(path, action, project=None, phase=None, note='', received_at=None, metrics=None):
    path = Path(path)
    if action == 'start':
        require(not path.exists(), 'Existing run; resume with phase instead of resetting clock')
        received = received_at or now()
        dt = datetime.fromisoformat(received)
        require(dt.tzinfo is not None and dt <= datetime.now(TZ), 'Received timestamp needs timezone and must not be future')
        d = {'version': VERSION, 'project': project, 'received_at': received,
             'timing_basis': 'provided_timestamp' if received_at else 'first_recorded_action',
             'events': [], 'feedback': None}
    else:
        d = read(path)
    require(action == 'feedback' or not d.get('finished_at'), 'Run finished; use a new run for more editing')
    stamp = now()
    if action == 'finish':
        d['finished_at'] = stamp
        d['outcome'] = note or 'draft_saved_pending_review'
    elif action == 'feedback':
        require(bool(d.get('finished_at')), 'Finish draft before recording user feedback')
        for field in ('correction_minutes', 'error_count'):
            if field in (metrics or {}):
                require(isinstance(metrics[field], (int, float)) and metrics[field] >= 0, 'Feedback counts must be nonnegative')
        d['feedback'] = {'at': stamp, **(metrics or {})}
    else:
        d['events'].append({'at': stamp, 'phase': phase or 'analysis', 'note': note})
    write(path, d)
    return d

def report(logs, output):
    rows = []
    for path in logs:
        d = read(path)
        start = datetime.fromisoformat(d['received_at'])
        end = datetime.fromisoformat(d['finished_at']) if d.get('finished_at') else datetime.now(TZ)
        totals = {}
        for i, e in enumerate(d['events']):
            stop = datetime.fromisoformat(d['events'][i+1]['at']) if i+1 < len(d['events']) else end
            totals[e['phase']] = totals.get(e['phase'], 0) + (stop-datetime.fromisoformat(e['at'])).total_seconds()/60
        feedback = d.get('feedback') or {}
        rows.append({'project': d['project'], 'received_at': d['received_at'], 'handed_off_at': d.get('finished_at', ''),
          'timing_basis': d['timing_basis'], 'elapsed_minutes': round((end-start).total_seconds()/60, 2),
          **{k+'_minutes': round(totals.get(k, 0), 2) for k in ('analysis','build','qa','rework','waiting','paused')},
          'unclassified_minutes': round((end-start).total_seconds()/60-sum(totals.values()), 2),
          'rework_rounds': sum(e['phase']=='rework' for e in d['events']),
          'user_correction_minutes': feedback.get('correction_minutes', ''), 'user_error_count': feedback.get('error_count', ''),
          'accepted': feedback.get('accepted', ''), 'outcome': d.get('outcome', 'in_progress')})
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    write(output.with_suffix('.json'), rows)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('snapshot'); p.add_argument('project'); p.add_argument('timeline'); p.add_argument('out')
    p = sub.add_parser('build'); p.add_argument('snapshot'); p.add_argument('plan'); p.add_argument('out')
    p = sub.add_parser('validate'); p.add_argument('draft')
    p = sub.add_parser('install'); p.add_argument('stage'); p.add_argument('--editor-closed', action='store_true')
    p = sub.add_parser('log'); p.add_argument('file'); p.add_argument('action', choices=['start','phase','finish','feedback'])
    p.add_argument('--project'); p.add_argument('--phase', choices=['analysis','build','qa','rework','waiting','paused'])
    p.add_argument('--note', default=''); p.add_argument('--received-at'); p.add_argument('--metrics', help='JSON user feedback file')
    p = sub.add_parser('report'); p.add_argument('output'); p.add_argument('logs', nargs='+')
    a = parser.parse_args()
    if a.command == 'snapshot': snapshot(a.project, a.timeline, a.out)
    elif a.command == 'build': build(a.snapshot, a.plan, a.out)
    elif a.command == 'validate':
        result = validate(read(a.draft)); print(json.dumps(result, ensure_ascii=False, indent=2))
        require(not result['errors'], 'Validation failed')
    elif a.command == 'install': install(a.stage, a.editor_closed)
    elif a.command == 'log':
        require(a.action != 'start' or bool(a.project), 'Start requires project name')
        require(a.action != 'phase' or bool(a.phase), 'Phase required')
        log_event(a.file, a.action, a.project, a.phase, a.note, a.received_at, read(a.metrics) if a.metrics else None)
    elif a.command == 'report': report(a.logs, a.output)

if __name__ == '__main__':
    main()
