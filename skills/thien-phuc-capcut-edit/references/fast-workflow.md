# Workflow dựng thường ngày và đo cải thiện

## Ba lượt

1. **Hiểu nguồn/chốt phương án:** ghi thời điểm nhận project ngay; xác minh đúng bản mới nhất và tỷ lệ. Nghe/xem hết hoặc ASR toàn nguồn khi được phép cho project đó. Lập một phương án gồm nhóm ý/các lượt nói (ưu tiên lượt cuối tốt nhất), câu giữ/bỏ, hook và phần thân không lặp, sổ cảnh nhám dùng một lần, caption/chữ nhấn và SFX. Một lần hiểu nguồn phục vụ mọi lớp. Không đọc lại tất cả lịch sử mẫu cho mỗi video; chỉ mở mẫu đúng tỷ lệ hoặc khi quyết định còn chưa rõ.
2. **Dựng bằng script:** dùng `scripts/editkit.py` theo `script-toolkit.md`. Tạo bản sao, inventory và plan; dựng ra staging, tự kiểm tra rồi mới cài vào project đang đóng. Áp dụng quyết định biên tập đã có, không tự cắt theo độ im lặng. Giữ preset đã xác nhận; cấu trúc không hỗ trợ thì xử lý đúng phần đó bằng UI/adapter đã kiểm chứng, không viết lại toàn bộ bộ dựng.
3. **Kiểm tra tập trung:** mở CapCut kiểm tra hình/chữ/âm thực tế. Rà bản dựng rồi sửa gộp các lỗi đã xác định; sau sửa chỉ kiểm tra lại vùng bị ảnh hưởng và kiểm tra cấu trúc. Không lặp ASR toàn nguồn hoặc kiểm tra toàn bộ khi không có thay đổi liên quan. Lưu và ghi bàn giao trước khi hỏi render. Giới hạn nghe/xem phải báo trung thực.

Cache ASR/inventory theo đường dẫn nguồn, kích thước, mtime, model/ngôn ngữ/tham số và phiên bản công cụ. Chỉ dùng lại khi khớp; cần hash nội dung khi file có thể bị thay mà giữ metadata. Kết quả của xe khác không phải cache hợp lệ. Bộ lõi hiện chưa chạy ASR hay quản lý cache tự động; dùng công cụ ASR sẵn có và lưu bằng chứng cache trong thư mục phiên.

## Nhật ký thời gian bắt buộc từ project kế tiếp

Mỗi lần nhận edit tạo một `run.json` trong thư mục làm việc của project, không ghi log công việc vào thư mục skill. Ghi theo ISO8601 có múi giờ +07:00:

- `received_at`: thời điểm nhận yêu cầu. Nếu client có timestamp thật, truyền `--received-at`; nếu không, script ghi thời điểm bắt đầu ghi nhận và đánh dấu `first_recorded_action`. Không giả là giờ nhận tin nhắn chính xác.
- `analysis`, `build`, `qa`: lần lượt hiểu nguồn, dựng, kiểm tra.
- `rework`: mỗi đợt sửa sau kiểm tra; note nguyên nhân. Không tính mỗi clip sửa là một vòng.
- `waiting`: chờ người dùng/nguồn/quyền. `paused`: phiên ngừng hoạt động. Ghi rõ nguyên nhân; không tự trừ thời gian chờ công cụ đang thực hiện công việc khỏi thời gian dựng.
- `finished_at`: lúc lưu và bàn giao bản dựng, chưa bao gồm render. Chỉ ghi khi thực sự bàn giao; trạng thái `draft_saved_pending_audio_review` nếu chưa nghe được.

Log là thời gian trôi qua giữa các mốc, không phải thời gian CPU hay thời gian lao động chính xác. Nếu phiên gián đoạn mà không kịp ghi pause, giữ khoảng đó và chú thích; không tự dựng lại số phút. Khi tiếp tục dùng log cũ, không reset đồng hồ. Các phiên sửa mới sau bàn giao có run riêng để không xóa lịch sử.

`report` xuất CSV UTF-8 BOM mở được trong Excel và JSON: project, giờ nhận/bàn giao, tổng phút, từng lượt, chờ/tạm dừng, phần chưa phân loại, số vòng sửa và feedback. Chỉ điền số lỗi/số phút anh sửa khi anh cung cấp; chưa biết để trống, không điền 0. Chưa phản hồi không có nghĩa được duyệt.

Đánh giá sau 2–3 video tương đương về độ dài nguồn/tỷ lệ/độ phức tạp. Mục tiêu người dùng chốt: **20 phút edit cho video thành phẩm 2:30–4:00**, chưa gồm render; chờ/tạm dừng ghi riêng. Không bỏ QA để đạt số phút. Mốc 90 phút do người dùng phản ánh là ước lượng lịch sử, không được biến thành thời gian đo của từng project cũ. Báo cả thời gian và lượng sửa tay; nhanh hơn mà lỗi nhiều hơn chưa đạt.

## Quy tắc chất lượng giữ nguyên

Ưu tiên lời trọn, hình đúng ý, cảnh nhám đủ ngắm, giá/odo/năm đúng. 9:16 có caption Roboto-Blk 8; 16:9 không caption lời nói. Main +10dB, nhạc/SFX riêng, B-roll mute. Cắt theo nghĩa và chuyển động, không theo định mức giây. Chi tiết khi cần: `editorial-rules.md`, `edit-reliability.md`, `capcut-projects.md`.

Bản dựng cần người dùng sửa nhiều là chưa đạt chất lượng, kể cả gần mốc20phút. Áp dụng bài học [Civic 2015](civic2015-revised-9-16.md) để tránh bỏ preset, SFX, lời kết và caption căn ước lượng.
