# Quy trình ổn định sau các lần dựng và sửa

Cập nhật 30/10/2026 từ góp ý trực tiếp của người dùng và các giới hạn quan sát ở lượt Cross dọc 2. Đây là cải tiến quy trình, không phải tuyên bố đã học bản Cross final người dùng tự sửa. Không dùng bản trợ lý chưa được duyệt làm mẫu thẩm mỹ mới.

## Trước khi cắt: bản đồ nội dung toàn nguồn

Sau khi nghe/xem hết (hoặc ASR trong phạm vi được cho phép), ghi gọn cho từng cụm nội dung: mốc nguồn, câu trọn được chọn, lượt nói lại cần bỏ, dữ kiện cần xác minh, hình chứng minh tương ứng. Chọn hook sau bước này. Không lấy danh sách khoảng lặng làm danh sách cắt.

Khi có nhiều lượt sửa lời cùng ý, ưu tiên lượt cuối nếu đã trọn và chuẩn hơn theo góp ý Camry; bỏ các lượt thử trước rồi đọc/nghe lại cả đoạn sau khi ghép. Đọc [bài học Camry](camry10-revised-dedup.md) để rà lặp ý giữa hook/thân và sổ cảnh nhám dùng một lần. Một câu mở đầu đứng riêng có thể lặp ý với câu sau; không giữ chỉ vì mỗi clip tự nó có nghĩa. Giữ hơi nghỉ phục vụ ý nói và động tác; không lấy ngưỡng dB thấp làm chứng nhận mép cắt tốt.

## Bản đồ hình và đoạn nối

- Với mỗi cảnh nhám, xác định nhiệm vụ: chứng minh trang bị, cho ngắm xe hay che điểm nối. Ưu tiên nguồn thể hiện đúng chi tiết, giữ chuyển động máy hoàn chỉnh khi còn hữu ích.
- Nếu cảnh chính có người đang nói hoặc chỉ tay, không lấy đoạn khác có chuyển động miệng làm hình phủ cho lời không khớp. Chọn cận cảnh chi tiết hoặc góc không lộ miệng; giữ thao tác thật khi nó đã minh họa tốt.
- Sau sửa lời, lập mốc timeline mới cho caption, thông tin giá/ưu đãi, cam kết và SFX. Một thay đổi độ dài phía trước phải được phản ánh ở mọi lớp liên quan, kể cả sau hook.
- Rà từng điểm nối trong ngữ cảnh câu trước–câu sau, rồi cả chuỗi cảnh. Kiểm tra cả ranh giới hook về phần chính, đầu/cuối B-roll và cảnh chính lộ giữa hai lớp phủ. Không chỉ kiểm tra đường cắt của video chính.

## Kiểm tra chữ bằng khung hình thật

Xem ở giữa thời gian hiện chữ và khi camera/người tiếp tục chuyển động. Caption và headline là hai lớp riêng nhưng phải kiểm tra cùng lúc; hai lớp không chồng nhau trên timeline vẫn có thể che cùng chi tiết trong hình.

Nếu caption dài tự xuống ba dòng hoặc quá chật, chia theo cụm nghĩa tại mốc lời phù hợp hoặc sửa ngắt dòng; giữ Roboto-Blk 8 của bản dọc. Không thu nhỏ font để chữa mọi câu dài. Giá, năm, odo, trả trước phải đối chiếu nguồn/chi tiết thật; ASR nghi vấn cần xác minh, không đoán theo video trước.

## Hai mức kiểm tra, báo cáo đúng mức

1. **Cấu trúc:** đúng project/take, media và refs còn tồn tại, source range hợp lệ, caption theo timeline mới, lời +10dB, B-roll mute, nhạc/SFX riêng. Khi dùng script, làm theo capcut-projects.md và kiểm tra lại trạng thái CapCut đã lưu; sửa cục bộ trên bản mới nhất thay vì ghi đè toàn bộ từ snapshot cũ.
2. **Cảm giác xem/nghe:** xem chuyển động và nghe nối lời/mix trong ngữ cảnh, kiểm tra toàn bản. Project mở được, validator pass và ảnh tĩnh đẹp chỉ chứng minh mức 1 cùng những khung đã xem.

Khi công cụ chỉ trả ảnh chụp, để player chạy hết rồi chụp vài thời điểm không được gọi là đã xem liên tục. Theo dõi các mốc đã kiểm tra; tua lại đúng điểm chưa thấy, không chụp ngẫu nhiên nhiều lần rồi coi là đủ. Nếu không nghe trực tiếp được, ghi rõ đã dùng ASR/đo âm và phần cảm giác âm thanh chưa xác nhận. Bàn giao bản dựng đã lưu với giới hạn đó, không tuyên bố “đã mượt hoàn toàn”. Quyền render vẫn theo SKILL.md.

## Học bản người dùng sửa

Khi được giao học thêm, so bản trợ lý với bản final mới nhất theo những chỗ đổi thực tế: câu chọn/bỏ, mép cắt, thời gian giữ cảnh nhám, hình chứng minh, vị trí chữ và SFX. Phân biệt điều quan sát được với suy luận về lý do. Ghi thành nguyên tắc có ngữ cảnh, không biến timestamp/thời lượng của một xe thành định mức chung. Nếu người dùng báo đã tự làm xong, ngừng sửa/render bản đó; chỉ đọc khi có yêu cầu học phù hợp.
