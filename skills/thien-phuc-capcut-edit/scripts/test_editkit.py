import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('editkit', Path(__file__).with_name('editkit.py'))
k = importlib.util.module_from_spec(spec)
spec.loader.exec_module(k)

class ToolkitTests(unittest.TestCase):
    def setUp(self):
        # Retain fixtures for inspection; never recursively delete computed paths.
        self.w = Path(tempfile.mkdtemp(prefix='editkit-test-', dir=Path.cwd()))
        self.project = self.w / 'project'
        media = self.w / 'media.mp4'
        media.write_bytes(b'fixture: data checks only, not playable media')
        self.d = {'fps':60, 'duration':10000000, 'canvas_config':{'width':1080,'height':1920},
          'materials':{'videos':[{'id':'v','path':str(media),'duration':10000000}],
                       'speeds':[{'id':'speed','type':'speed','speed':1}]},
          'tracks':[{'id':'main','type':'video','segments':[{'id':'main1','material_id':'v',
            'extra_material_refs':['speed'], 'volume':1,'speed':1,
            'source_timerange':{'start':0,'duration':10000000},
            'target_timerange':{'start':0,'duration':10000000}}]}]}
        k.write(self.project/'draft_content.json', self.d)
        k.write(self.project/'Timelines/t/draft_content.json', self.d)
        k.write(self.project/'draft_meta_info.json', {'draft_name':'Test','tm_duration':10000000})
        self.base = self.w/'snapshot'
        k.snapshot(self.project, 't', self.base)
        self.plan = {'project_name':'Test','source_review_complete':True,'review_method':'asr_authorized',
          'asr_authorization':'user permitted this fixture project','ratio':'9:16','duration_seconds':4,
          'keep_tracks':[],'drop_tracks':[],'timing_rationale':'all tracks rebuilt',
          'tracks':[{'id':'main','role':'speech','clips':[
            {'template_segment':'main1','source_start':6,'target':[0,2]},
            {'template_segment':'main1','source_start':0,'target':[2,4]}]}]}

    def build(self):
        k.write(self.w/'plan.json',self.plan)
        k.build(self.base,self.w/'plan.json',self.w/'stage')

    def test_build_install_editable_refs_and_gain(self):
        self.build()
        d=k.read(self.w/'stage/draft_content.json')
        self.assertEqual(d['tracks'][0]['segments'][0]['source_timerange']['start'],6000000)
        self.assertNotEqual(d['tracks'][0]['segments'][0]['extra_material_refs'],d['tracks'][0]['segments'][1]['extra_material_refs'])
        self.assertEqual(d['tracks'][0]['segments'][0]['volume'],10**.5)
        k.install(self.w/'stage',True)
        self.assertEqual(k.read(self.project/'draft_content.json'),k.read(self.project/'Timelines/t/draft_content.json'))

    def test_refuse_stale_project(self):
        self.build()
        self.d['duration']=9999999
        k.write(self.project/'draft_content.json',self.d)
        before=(self.project/'draft_content.json').read_bytes()
        with self.assertRaisesRegex(ValueError,'Live project changed'): k.install(self.w/'stage',True)
        self.assertEqual(before,(self.project/'draft_content.json').read_bytes())

    def test_reject_source_overrun(self):
        self.plan['tracks'][0]['clips'][0]['source_start']=9
        with self.assertRaisesRegex(ValueError,'Source bounds'): self.build()

    def test_reject_unaccounted_tracks(self):
        self.plan['tracks']=[]
        with self.assertRaisesRegex(ValueError,'account'): self.build()

    def test_requires_asr_authorization(self):
        self.plan['asr_authorization']=''
        with self.assertRaisesRegex(ValueError,'authorization'): self.build()

    def test_anchor_disambiguates_hook(self):
        self.plan['parts']=[{'key':'hook','source':[6,8]}, {'key':'body','source':[0,2]}]
        clips=self.plan['tracks'][0]['clips']
        for clip,key,span in zip(clips,['hook','body'],[[6,8],[0,2]]):
            del clip['target'];clip.update(anchor=key,anchor_source=span)
        self.build()
        d=k.read(self.w/'stage/draft_content.json')
        self.assertEqual(d['tracks'][0]['segments'][1]['target_timerange']['start'],2000000)

    def test_wrong_role_rejected(self):
        self.plan['tracks'][0]['role']='music'
        with self.assertRaisesRegex(ValueError,'Role/track'): self.build()

    def test_report_unknown_feedback_not_zero(self):
        log=self.w/'run.json'
        k.log_event(log,'start',project='Test')
        k.log_event(log,'phase',phase='waiting')
        k.log_event(log,'finish',note='draft_saved_pending_audio_review')
        k.report([log],self.w/'report.csv')
        row=k.read(self.w/'report.json')[0]
        self.assertEqual(row['user_error_count'],'')
        self.assertEqual(row['accepted'],'')
        self.assertTrue(row['handed_off_at'])
        with self.assertRaisesRegex(ValueError,'Existing run'):k.log_event(log,'start',project='Test')

if __name__=='__main__': unittest.main()
