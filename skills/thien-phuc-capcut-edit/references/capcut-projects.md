# Làm việc với project CapCut trên máy người dùng

Đây là hướng dẫn bổ sung khi đọc dữ liệu hoặc dùng script, không yêu cầu bỏ qua giao diện. Chọn cách thao tác phù hợp và xác minh kết quả trong CapCut. Khi dùng giao diện Windows, đọc skill Computer Use hiện hành trước và dùng đúng API nó cung cấp.

## Khám phá lại trạng thái thật

- CapCut từng lưu project tại `%LOCALAPPDATA%/CapCut/User Data/Projects/com.lveditor.draft`. Đây là vị trí ứng viên, phải xác minh hiện tại; có thể người dùng đã đổi nơi lưu.
- Đọc tên project, media thực, canvas/fps và `Timelines/project.json` nếu có. Xác định `main_timeline_id` và timeline đang làm, không chỉ đọc `draft_content.json` ở root rồi giả định đó là timeline đang mở.
- Các phiên bản có cấu trúc khác nhau. Nếu nội dung mã hóa, schema không hiểu hoặc root/active timeline bất nhất, dùng UI để đọc/sửa thay vì đoán rồi ghi.
- Cửa sổ Home và editor có thể đổi HWND. Dùng đối tượng cửa sổ vừa được tool trả về; quan sát lại sau chuyển project/modal. Không dùng số cửa sổ, tọa độ cố định trong tài liệu cũ.

## Khi cần chỉnh bằng script

- Chỉ sửa project đích trong yêu cầu đã được phép edit. Bản người dùng mới sửa là đầu vào; không khôi phục snapshot trợ lý cũ lên đó.
- Đóng editor về Home để ứng dụng lưu xong trước khi sửa file; đọc lại trạng thái đã lưu. Sao lưu file root, timeline đích và manifest liên quan vào workspace trước khi ghi.
- Dùng quyền filesystem đúng phạm vi khi đường dẫn ngoài workspace. Không tự suy ra quyền kỹ thuật từ việc thấy file đọc được.
- Giữ ID dự án/timeline cần thiết; mọi clip phải tham chiếu material còn tồn tại, source range phải nằm trong nguồn, target range nhất quán với duration. Bảo toàn effect/resource refs và các chỉnh sửa không liên quan.
- Chỉ cập nhật root và timeline thực sự cần đồng bộ theo schema đã xác minh. Không ghi hàng loạt vào mọi timeline hoặc dự án mẫu.
- Sau ghi, mở lại đúng project và kiểm tra ảnh/chữ/track audio. Nếu CapCut báo thiếu media/lỗi tải, dừng sửa tiếp và khôi phục đúng snapshot trước thay đổi nếu phù hợp; không lặp ghi đoán schema.

## Kiểm tra điểm lóe hình

Đánh giá track hình thực sự hiển thị, không chỉ từng segment:

1. Lấy các mốc bắt đầu/kết thúc của clip chính và B-roll.
2. Xét clip trên cùng có hiệu lực ở từng khoảng (kể cả trạng thái hiện/ẩn, opacity, crop/mask nếu có).
3. Tìm khoảng rất ngắn lộ cảnh dưới giữa hai cảnh chèn hoặc ngay sát điểm cắt lời.
4. Xem khung hình trước/sau và phát đoạn đó trong UI; khép khe hoặc đặt lại B-roll theo nghĩa lời. Không kéo quá nguồn, đóng băng frame hay thay tốc độ ngầm để lấp chỗ trống.

Với timeline60fps, một frame xấp xỉ16,67ms. Cảnh nguồn59,94fps cần kiểm tra playback thực; sự khác nhau giữa59,94 và60 không tự chứng minh nguyên nhân giật là rớt frame.

## Caption và âm thanh

- Font/size có thể nằm trong JSON rich text `content`, `base_content` và metadata ngoài. Đọc style đang render rồi xác minh UI; không mặc định trường ngoài là đủ.
- Khi thay lời/cắt timeline, retime caption, chữ nhấn và SFX theo lời mới; không giữ từ khóa/karaoke timing cũ nếu không còn khớp.
- Kiểm tra clip mix cũ không còn hoạt động cùng tiếng gốc/nhạc/SFX riêng, tránh âm nhân đôi. Các media cache phải tồn tại; không nhúng nhạc/font có hạn chế vào gói skill để thay cho cache người dùng.
- Việc export chỉ diễn ra sau quyền render theo `SKILL.md`. Nút Share trong màn hình hoàn tất export là thao tác khác, không được cấp quyền ngầm.
