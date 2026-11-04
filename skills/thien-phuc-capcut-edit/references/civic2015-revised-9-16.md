# Civic 1.8AT 2015 dọc — bản người dùng sửa, 02/11/2026

Ưu tiên bài học này khi dựng dọc tiếp theo. Đối chiếu snapshot timeline và khung hình UI; chưa nghe bằng tai hoặc xem chuyển động liên tục toàn bản. Các mốc là bằng chứng của xe này, không phải định mức cho xe khác. Không coi bản final là bằng chứng mọi caption còn lại đều đúng.

## Những thay đổi đã xác nhận

- Hook nội thất: bản trợ lý chép nguyên source73.30–78.30; người dùng chọn73.616666–76.95 rồi77.6–78.4. Rút phần dở/nghỉ giữa, giữ lời khen cuối. Khi được chỉ khoảng thời gian, lấy đó làm vùng chọn; xét đầu/cuối âm và câu trong vùng. Nếu người dùng yêu cầu chính xác từng frame thì giữ đúng yêu cầu đó.
- Phần chính: người dùng tách lại các câu trong dải mà trợ lý đã giữ nguyên; loại source19.85–22.45, các phần lặp/chuyển ý quanh37.63–38.48 và48.38–51.93. Không giữ một dải dài chỉ vì ASR đã phát hiện đoạn lặp lớn khác. Rà mạch ý còn lại sau cắt để phát hiện cả lặp nhỏ.
- **Preset:** khôi phục Text presets1 cho nhãn trắng tên xe/nhãn đỏ “Lái Hay,Bền, Bảo Dưỡng Rẻ”, và News–Highlight tên xe. Bản trợ lý bỏ template rồi dùng plain yellow text đã sai phong cách. Không tự hạ cấp preset vì script chưa hỗ trợ; sửa đúng preset bằng UI/adapter đã xác minh. Giữ thiết kế, đổi dữ kiện đúng xe.
- **Odo:** chữ131.000km đi với lượt giới thiệu km đầu; khi nhắc km ở nội thất thì dùng cảnh đồng hồ...0457 ở61.0–63.483333 của bản mới. Hình cabin chung không thay được hình chứng minh. Lập cặp lời–chi tiết trước khi chọn cảnh đẹp.
- **SFX:** Swish riêng ở nối hook về giới thiệu (~12.58s), Magic reveal ở intro/tên xe/km, Money ở giá. Trợ lý đã xóa Swish là thiếu sót. Kiểm tra danh sách vai trò âm thanh đã có, retime đúng mốc mới; không yêu cầu mọi video có số hiệu ứng giống nhau.
- **Caption:** người dùng sửa “sáng tân” thành “sáng tưng”, “Xe lướt...” thành “sáng lóa anh chị thấy hong”, nối/chia lại các cụm về500–700ngàn và “em sẽ để lại...”. Caption chia đều số từ và nội suy thời gian đã không đủ chính xác. Dùng word timestamps làm điểm neo, chỉnh cụm nghĩa và đối chiếu lời; không sửa ASR nghi vấn bằng suy đoán cho câu nghe có vẻ hợp lý. Nếu không xác minh được, ghi mốc cần kiểm tra thay vì coi là đã sửa đúng.
- **Kết:** bản mới nới nguồn tới141.666667 và thêm bye bye; trợ lý dừng141.0 đã bỏ lời cuối. Kiểm tra hết nguồn và lời cuối trước hiệu ứng đóng.

## Thay đổi trong cách thực hiện

Trước build, kiểm tra plan có đủ: preset cần giữ, câu hook trọn ý, hình chứng minh km/trang bị, vai trò SFX, caption theo lời và lời kết. Đây là kiểm tra phương án trong cùng lượt dựng, không phải thêm một vòng nghiên cứu.

Nếu toolkit không hỗ trợ phần bắt buộc, không được âm thầm xóa lớp hoặc thay bằng loại chữ đơn giản để validator pass. Giữ/retime lớp đó hoặc dùng adapter/UI đúng phần bị thiếu. Không tuyên bố bộ script bao phủ toàn workflow khi chưa kiểm chứng phần này.

20 phút là mục tiêu bàn giao có chất lượng cho bản2:30–4:00 theo người dùng; không là hạn chót để dừng QA. Bản cũ20.85phút còn cần anh sửa nhiều nên chưa đạt cả yêu cầu thời gian lẫn chất lượng. Thời gian sửa của người dùng và tổng lỗi chưa được cung cấp thì để trống; chỉ ghi phản hồi định tính đã xác nhận. Giữ số đo cũ, không sửa lịch sử để làm đẹp report.
