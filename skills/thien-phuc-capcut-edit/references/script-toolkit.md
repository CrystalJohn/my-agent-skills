# editkit v1 — chuẩn hóa thao tác, không tự quyết định biên tập

Chạy bằng Python 3.10+ (thư viện chuẩn, không cần pip). Tìm Python hoạt động trong phiên, không mặc định alias WindowsApps chạy được. Lệnh dưới dùng `python` như tên thay thế cho executable đã xác minh. Đường dẫn làm việc và tên project phải lấy từ yêu cầu hiện tại.

## Các lệnh

```text
python editkit.py log RUN.json start --project "Tên project"
python editkit.py log RUN.json phase --phase build --note "Đã chốt nguồn và phương án"
python editkit.py snapshot PROJECT_DIR ACTIVE_TIMELINE_ID SNAPSHOT_NEW_DIR
python editkit.py build SNAPSHOT_NEW_DIR PLAN.json STAGE_NEW_DIR
python editkit.py validate STAGE_NEW_DIR/draft_content.json
python editkit.py install STAGE_NEW_DIR --editor-closed
python editkit.py log RUN.json phase --phase qa
python editkit.py log RUN.json phase --phase rework --note "Sửa mép câu, bố cục giá"
python editkit.py log RUN.json finish --note "draft_saved_pending_audio_review"
python editkit.py log RUN.json feedback --metrics USER_FEEDBACK.json
python editkit.py report REPORT.csv RUN1.json RUN2.json
```

`--editor-closed` là xác nhận của agent sau khi đã quan sát UI đóng editor về Home, không tự phát hiện ứng dụng. Phải lưu/đóng trước snapshot và trước install. Install kiểm tra hash bản đang lưu và bản sao, không ghi nếu đã thay đổi. Cần quyền filesystem đúng phạm vi. Không có lệnh render. Khi người dùng đã tự sửa xong, không install bản trợ lý cũ.

## Plan

Inventory chứa track/segment ID thật. Plan tham chiếu segment làm mẫu có sẵn trong snapshot, giữ resource và thiết kế của project. Không lấy thứ tự track làm ID. Một clip mới clone mẫu, source range, extra refs và âm lượng tương ứng; main +10dB, B-roll mute. Music/SFX giữ gain mẫu và từng clip riêng.

Ví dụ hình dạng plan (thay ID bằng inventory thật, không chạy nguyên ví dụ):

```json
{
  "project_name": "Tên project",
  "source_review_complete": true,
  "review_method": "asr_authorized",
  "asr_authorization": "Người dùng cho phép ASR riêng cho project này",
  "ratio": "9:16",
  "duration_seconds": 8,
  "parts": [
    {"key": "hook", "source": [20, 23]},
    {"key": "body", "source": [0, 5]}
  ],
  "keep_tracks": [],
  "drop_tracks": [],
  "timing_rationale": "Mọi lớp được dựng theo timeline mới",
  "tracks": [{
    "id": "ACTUAL_TRACK_ID",
    "role": "speech",
    "clips": [
      {"template_segment": "ACTUAL_SEGMENT_ID", "source_start": 20, "anchor": "hook", "anchor_source": [20, 23]},
      {"template_segment": "ACTUAL_SEGMENT_ID", "source_start": 0, "anchor": "body", "anchor_source": [0, 5]}
    ]
  }]
}
```

Mọi track hiện có phải thuộc đúng một nhóm keep/drop/replace. Keep chỉ khi thời gian vẫn đúng và nêu lý do; không giữ nhạc/chữ ở timestamp cũ sau khi chèn hook. Thêm clip vào track có sẵn bằng plan; thêm track/material mới hoặc nhập mẫu từ project khác cần adapter/UI riêng, không giả đã hỗ trợ.

Role: `speech`, `broll`, `captions`, `music`, `sfx`, `title`, `effect`. Track ID/type phải phù hợp. `target:[start,end]` tính giây trên timeline mới; hoặc `anchor` + `anchor_source` để ánh xạ nguồn vào phần hook/body có tên riêng. Không tự cắt caption băng qua vùng bị bỏ; chia câu theo nghĩa trước. Với B-roll, `source_start` chỉ nguồn hình mẫu, còn anchor chỉ nơi đặt hình theo lời.

`text` thay plain text một style (range UTF-16), giữ font mẫu; `transform:{"x":0,"y":0.5}` là vị trí có chủ đích sau kiểm tra hình. Chữ nhiều style, composite preset, speed curve/keyframe chưa có adapter được xác nhận sẽ bị từ chối hoặc cần xử lý riêng. Không thay nội dung preset cam kết bằng plain text tự tạo. Kiểm tra Roboto-Blk thực trong UI; size 8 không đủ chứng minh đúng font.

Build xuất draft, meta, plan, time-map và validation. Validate cấu trúc không chứng minh preset tải đúng hoặc chuyển động/âm thanh mượt. Mốc khe ngắn chỉ cảnh báo để xem, không phải quy tắc kéo dài cảnh tự động. Build không trộn audio, không sửa file nguồn, không tự cắt theo ASR.

Feedback JSON chỉ từ người dùng: `{"correction_minutes":12,"error_count":3,"accepted":true}`. Có thể bỏ trường chưa biết. Không tự suy ra số lỗi từ số vòng sửa của agent.

## Kiểm chứng và giới hạn

Chạy `python test_editkit.py` trong thư mục test thuộc workspace; fixtures được giữ lại để kiểm tra. Có test dựng/install trên project giả, source overrun, thiếu track, quyền ASR, stale snapshot và log/report. Validator đã chạy trên snapshot Cross dọc 2 trong workspace; không ghi vào project thật. Đây chưa phải benchmark tốc độ hay xác nhận hình/âm trên các phiên bản CapCut khác. Gặp schema khác thì dừng đúng bước không hỗ trợ; mở rộng adapter nhỏ và kiểm tra bản sao trước.

## Điều kiện dùng sau phản hồi Civic 2015

Toolkit chỉ là lõi thao tác, chưa bao phủ composite preset hoặc tự căn caption theo lời. Plan thiếu preset bắt buộc/SFX/lời kết không được xem là bản dựng hoàn thiện dù validate pass. Không drop track preset chỉ vì build chưa hỗ trợ. Dùng UI hoặc adapter đã xác minh cho phần đó; việc chọn câu, chia caption và đặt điểm neo phải thực hiện trước. Xem [bài học Civic 2015](civic2015-revised-9-16.md).
