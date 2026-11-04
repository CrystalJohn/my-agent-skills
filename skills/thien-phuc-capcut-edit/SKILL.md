---
name: thien-phuc-capcut-edit
description: Học và dựng video ô tô trong CapCut theo mẫu riêng 9:16 và 16:9 của người dùng. Bản dọc có phụ đề Roboto-Blk 8; bản ngang không caption, có brand/chữ nhấn riêng. Giữ nhạc/SFX riêng và hỏi trước render.
---

# Dựng video ô tô — nhanh, đúng mẫu và có số liệu

## Luồng mặc định mỗi project

Đọc [workflow ba lượt và báo cáo thời gian](references/fast-workflow.md), dùng [bộ script chuẩn](references/script-toolkit.md). Ghi nhận thời điểm bắt đầu ngay, không đợi dựng xong mới ước lượng. Bộ lõi nằm tại `scripts/editkit.py`, dùng Python chuẩn.

1. **Hiểu toàn nguồn → chốt phương án:** nghe/xem hết, chọn câu giữ/bỏ, hook và hình chứng minh trong một lượt. ASR chỉ thay nghe trong phạm vi người dùng đã cho phép; không hỏi lại cùng phạm vi. Không quyết định cắt chỉ theo khoảng lặng.
2. **Dựng một lượt bằng script:** dùng snapshot mới nhất và plan có ID thật; căn đồng bộ mọi lớp sau cắt/hook. Chỉ dùng UI/adapter cho phần preset/schema chưa hỗ trợ, không viết lại toàn bộ bộ dựng cho mỗi xe.
3. **Kiểm tra tập trung → bàn giao:** kiểm tra bản phát, sửa gộp lỗi, rà lại vùng ảnh hưởng. Lưu, ghi thời điểm bàn giao và báo giới hạn thực tế. Không gọi validator/ảnh tĩnh/ASR là đã nghe hoặc xem liên tục.

Không đọc lại mọi tài liệu mẫu ở mỗi video. Chỉ mở tài liệu tỷ lệ đang làm hoặc đúng vấn đề còn chưa rõ. Quy tắc có sẵn không phải lý do lặp kiểm tra nếu dữ liệu không đổi.

## Các yêu cầu luôn giữ

- **9:16:** caption Roboto-Blk 8, trắng viền đen; sửa tên người thành **Chương**. **16:9:** không caption lời nói, giữ brand/chữ nhấn đúng mẫu project.
- **Giữ đúng preset mở đầu/tên xe đã học.** Script không hỗ trợ composite preset thì dùng UI/adapter đúng phần đó; không xóa lớp hoặc thay chữ thường để dựng cho nhanh.
- **Caption theo cụm nghĩa và mốc lời thật:** không chia đều số từ rồi nội suy timing làm bản hoàn thiện; ASR nghi vấn phải xác minh, không đoán câu.
- Tiếng gốc/main **+10dB**, B-roll mute; nhạc và từng SFX riêng, còn chỉnh tiếp được.
- **Lọc theo nhóm ý trước cắt:** khi nhiều lượt nói lại cùng ý, ưu tiên lượt cuối trọn và chuẩn; bỏ các lượt thử trước, chỉ giữ thông tin riêng cần thiết. Không chỉ xóa câu vấp mà để cùng ý lặp lại.
- **Mỗi cảnh nhám dùng một lần trong toàn video**, tính cả hook và phần chính; đổi trim/materialID không tạo cảnh mới. Lập sổ cảnh đã dùng theo nguồn thật.
- Chọn điểm cắt theo câu trọn, hơi nghỉ và động tác. Giữ cảnh nhám đẹp đủ ngắm, đúng ý; tránh hình chính lóe lên giữa các cảnh phủ. Không định mức số giây/cảnh hoặc kéo giãn/đóng băng để làm dài.
- Hook lấy từ nội dung thật sau khi hiểu toàn nguồn, nối về phần chính tự nhiên. Không bịa giá/ưu đãi/thông số. Nếu đầu nguồn đã có hook tốt thì dùng nó; khi đưa lời từ thân bài lên hook, không phát lại nguyên cụm đó trong thân bài.
- Giá/chữ nhấn đặt theo khoảng trống thực tế; tránh mặt, chi tiết xe, caption và UI. Không thêm title “Liên Hệ Em Chương/Trương”. Cam kết dùng preset người dùng đã setup.
- Bản người dùng tự sửa mới nhất là đầu vào. Không sửa/render project đã hoàn thành nếu chưa có yêu cầu mới. Sao lưu trước khi thay đổi; dừng ghi nếu bản live khác snapshot.
- **Sau khi dựng phải hỏi anh có muốn render không và chờ đồng ý.** Edit không cấp quyền render, kể cả xuất bản xem thử. Quyền render không gồm đăng mạng xã hội.

## Đọc thêm đúng tình huống

- Lọc ý lặp và chọn lượt cuối theo bản Camry người dùng sửa: [camry10-revised-dedup.md](references/camry10-revised-dedup.md).
- Chi tiết đã học, quy tắc cắt/chữ/âm và giới hạn nghe: [editorial-rules.md](references/editorial-rules.md).
- Bài học dọc mới nhất từ bản anh sửa: [Civic 2015](references/civic2015-revised-9-16.md), ưu tiên cho preset, chọn câu, odo, SFX và caption.
- Mẫu dọc: [style.md](references/style.md), [Civic final](references/civic-final-9-16.md).
- Mẫu ngang: [horizontal-16-9.md](references/horizontal-16-9.md), [Civic ngang sửa](references/civic-revised-16-9.md).
- Hook/điểm nối: [Forte hook](references/forte-hook-review.md); lỗi đã góp ý: [Forte dọc](references/forte-feedback-9-16.md).
- Preset cam kết: [commitment-preset.md](references/commitment-preset.md).
- Khi sửa dữ liệu CapCut: [capcut-projects.md](references/capcut-projects.md). Khi thao tác UI: dùng skill Computer Use hiện hành, khám phá cửa sổ thật trong phiên.
- Khi học bản final hoặc điều tra chất lượng: [edit-reliability.md](references/edit-reliability.md). Không xem bản trợ lý chưa duyệt là mẫu thẩm mỹ đã được chấp nhận.

## Đo cải thiện

Mỗi project có run.json và report CSV/JSON gồm giờ nhận/bàn giao (+07:00), tổng phút, hiểu nguồn/dựng/QA/sửa/chờ/tạm dừng, số vòng sửa và feedback người dùng. Không ghi 0 cho số liệu chưa biết. Mục tiêu người dùng chốt: **20 phút edit cho video thành phẩm 2:30–4:00**, chưa gồm render, thời gian chờ ghi riêng; so sánh 2–3 project tương đương bằng cả thời gian lẫn lượng anh phải sửa tay. Không bịa thời gian cho các project trước.

Bản dựng đúng thời gian nhưng người dùng phải sửa nhiều chưa được coi là đạt. Ghi feedback định tính trung thực; không tự quy đổi thành số lỗi/số phút.
