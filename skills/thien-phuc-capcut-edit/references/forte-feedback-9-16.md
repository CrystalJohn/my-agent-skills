# Forte dọc — góp ý người dùng ngày 24/10/2026

Ưu tiên hơn cách viết/tọa độ trong các snapshot trợ lý cũ. Người dùng đã tự sửa và render “Kia Forte 1.6MT 2012-dọc 1”, chỉ yêu cầu ghi nhận và cập nhật skill; không sửa lại project, không render lại.

## Quy tắc được xác nhận trực tiếp

- Tên đúng: **Chương**, không phải Trương. Áp dụng cho caption, chữ và nội dung kèm video. Những lần trợ lý tự “sửa” Chương thành Trương trước đây là sai, không tiếp tục dùng bảng thay thế đó.
- **Không cần title liên hệ tên người giới thiệu.** Không chỉ đổi banner sai tên thành “Liên Hệ Em Chương”: phải bỏ ý định tạo banner đó. Giữ câu thoại và phụ đề liên hệ nếu có trong lời nguồn; không xóa lời chỉ vì bỏ title. Không giữ SFX mồ côi từng phục vụ banner bị bỏ.
- Giá đặt ở khoảng trống hợp cảnh cho người xem đọc thuận mắt. Ảnh người dùng gửi cho thấy khoảng trời phía trên xe/người có thể dùng; đây là gợi ý bố cục, không phải tọa độ bắt buộc. Xem cả chuyển động trong thời gian chữ xuất hiện, tránh che chủ thể hoặc để chữ chen vào caption/vùng giao diện.
- **~00:24 bản trợ lý: cắt thô, cụt câu**, người dùng phải nối lại cho dễ chịu. **~00:52: cắt sót**, người dùng phải loại thêm phần thừa. Hai lỗi cần kiểm tra riêng; không chỉ kiểm tra khe hình hoặc source range hợp lệ.

## Đối chiếu bản lưu, không suy diễn đã nghe

Đọc ngày24/10 active timeline `A108884E-6C14-460e-BB49-A32C131ADA03`; root và active timeline khớp. Bản trợ lý trong workspace dài156,95s; bản người dùng lưu dài152,18s. Đây là số đo để tra cứu, không phải mục tiêu rút ngắn cho lần sau.

| Điểm | Bản trợ lý | Bản người dùng lưu | Bài học |
| --- | --- | --- | --- |
| Đuôi đoạn trước điểm ~00:24 | Nguồn16,833–22,750s, sang đoạn26,900s tại timeline24,567s | Nguồn16,833–23,217s; điểm nối sang26,900s dời tới25,033s | Nới đuôi khoảng0,467s. Không ép cắt sát mốc ASR; giữ cuối câu và khoảng nghỉ đủ tự nhiên theo lời/động tác. Không suy ra phải cộng0,467s cho mọi cut. |
| Cụm ~00:52 | Nguồn26,900–57,250s giữ liền | Tách thành26,900–53,950s rồi54,933–57,250s; điểm nối mới tại52,083s | Bỏ thêm khoảng0,983s trong cụm chuyển ý/nói lại. Sau sửa lời vẫn phải rà cả phần được giữ, không chỉ kiểm tra những gì đã xóa. |

Các nguồn/time range trên đã đọc thực; nhận xét “thô/cụt” và “cắt sót” do người dùng xác nhận. Lần đối chiếu này không nghe lại bằng tai, không khẳng định chính xác âm tiết bị cắt chỉ từ dữ liệu. Những thay đổi khác của bản người dùng không tự biến thành quy tắc chung.

Chữ giá trong bản lưu vẫn là185Tr, đã đổi bố cục; title liên hệ không còn là segment hoạt động. Không chép giá185Tr sang xe khác. Bằng chứng cục bộ nếu workspace còn: `work/forte_edit/prepared/draft_content.json` là bản trợ lý; `work/forte_edit/user-revised-2026-10-24.json` là snapshot chỉ đọc của bản người dùng; ba ảnh trong tin nhắn góp ý là bằng chứng yêu cầu. Skill không phụ thuộc các snapshot lớn này.
