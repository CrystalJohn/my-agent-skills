# Hook Forte ngang — bản sửa được người dùng duyệt

Project “Kia Forte 2012-ngang 1”: sửa ngày25/10/2026, người dùng xác nhận tốt và yêu cầu cập nhật skill ngày26/10/2026. Đây là ví dụ chọn hình/lời và sửa mép cắt, không là công thức thời lượng cho xe khác.

## Điều thay đổi quyết định dựng

- Đọc timecode đầy đủ trước khi sửa: ảnh người dùng chỉ `00:00:01:54` trên timeline60fps là 1giây54frame, không phải 1phút54giây.
- Không đặt đầu đoạn theo một timestamp ASR duy nhất. Mốc word alignment có thể chứa khoảng nghỉ hoặc dính đuôi câu trước. Kiểm tra nguồn trước/sau mép; giữ đầu âm, cuối âm và hơi nghỉ tự nhiên. Waveform chỉ hỗ trợ, không tự chứng minh câu nối nghe mượt.
- Trong ví dụ, đầu câu số km cũ tại nguồn10,483333s còn nằm trong âm của câu trước. Dời sang10,85s ở khoảng nghỉ trước câu mới; cuối14,30s vẫn giữ đủ lời và chưa ăn vào lượt nói lặp sau. Không mang các mốc này sang nguồn khác.
- Giữ câu cửa sổ trời và câu giá nối liên tục từ cùng đoạn lời khi nguồn đã nói tự nhiên, thay vì tạo thêm một mối ghép âm không cần thiết. Hình đổi theo ý, tiếng không cần cắt cùng mọi lần đổi hình.
- Tìm hình thật sự thấy trang bị: nguồn lúc nói cửa sổ trời chỉ có người đứng ngoài chỉ tay; nguồn77–79s mới thấy rõ kính và khung cửa sổ trời trong cabin. Dùng hình đó làm B-roll tắt tiếng, giữ lời cửa sổ trời bên dưới. Không gọi cảnh ghế hoặc cảnh chỉ tay là đã thấy rõ trang bị.

## Bản đã được duyệt để tra cứu

| Ý hook | Lời nguồn | Hình hiển thị |
|---|---|---|
|Cửa sổ trời → giá185Tr|37,45–41,35s, giữ liên tục|Kính/khung cửa sổ trời, rồi chính diện xe lúc nói giá|
|Mới86.000km|10,85–14,30s|Cận đồng hồ/odo|

Hook dài7,35s trong ví dụ này. Chữ nhấn riêng: “Có Cửa Sổ Trời”, “Chỉ185Tr”, “Mới86.000km”; giữ brand ngang hiện có. Không có caption lời nói. Khi xe khác hoặc câu khác cần nhịp khác, chọn lại từ nguồn.

## Bảo toàn bản người dùng đã chỉnh

Sao lưu bản đang lưu mới nhất; thay prefix hook cũ, không cộng dồn hai hook. Trong ví dụ,36segment phần chính được giữ nguyên source trim, bố cục, gain, chữ, cảnh nhám và quan hệ SFX; chỉ dịch cùng một độ lệch để nhường chỗ hook mới. Nhớ dịch hoặc mở rộng các lớp brand/nhạc liên quan, retime chữ/SFX của hook, kiểm tra khe hình và điểm nối vào phần chính. ID compound có thể được CapCut gộp lại hoặc thời gian làm tròn vài microsecond; đối chiếu nội dung tham chiếu và timing theo frame trước khi kết luận dữ liệu bị đổi.

Giữ lời chính+10dB, B-roll mute, nhạc và từng SFX riêng. Mở lại CapCut để xác minh cảnh mái kính, giá, odo, chữ, brand và phần giới thiệu sau hook đều hiện đúng; lưu project rồi hỏi trước render.

## Giới hạn bằng chứng

Lần này người dùng cho phép ASR thay nghe trực tiếp cho riêng project Forte. Đã phân tích toàn bộ nguồn, kiểm tra lại câu ghép bằng ASR/waveform và xem hình/playback trong CapCut; chưa nghe trực tiếp bằng tai. Người dùng duyệt kết quả sau đó. Không biến lần duyệt này thành chứng cứ rằng công cụ đã nghe hoặc thành quyền ASR cho các project sau; vẫn tuân thủ thứ tự nghe hết → lọc → cắt trong SKILL.md trừ phạm vi ngoại lệ được người dùng cho phép.
