# Camry-dọc 10 — lọc ý lặp và chọn lượt cuối

Ngày02/11/2026, người dùng xác nhận: khi nói đi nói lại cùng một ý, **thường chọn lượt cuối vì lúc đó nói chuẩn hơn**. Đây là ưu tiên chọn take, không phải luật giữ câu cuối bất kể bị cụt/sai dữ kiện. Xét toàn bộ lời của cùng ý trước khi dựng. Quy tắc cảnh nhám người dùng bổ sung: **mỗi cảnh chỉ dùng một lần trong toàn video, gồm hook và phần chính**.

## Bằng chứng đối chiếu

Snapshot active timeline và khung UI của bản người dùng sửa đã được đọc; không nghe bằng tai hay xem chuyển động liên tục. Bản trợ lý144.65s, bản người dùng114.033333s. Số giây là dấu mốc đối chiếu, không phải định mức độ ngắn.

- Bản trợ lý đưa source113.1–119.85 +125–130.95 (điều khiển ghế sau/rộng rãi/vị thế) lên hook, rồi giữ113.1–130.95 trong phần chính: lặp nguyên cụm nội dung. Bản người dùng bỏ hook thêm này, mở bằngsource0–13.55 về giảm20triệu/giá525triệu. Bài học: nguồn mở đầu có hook thật rồi thì dùng nó; không bắt buộc chép một đoạn phía sau lên đầu chỉ để có hook mới.
- Bản trợ lý giữ câu điều hòa3vùng ở84.25–89.65 và nhắc lại ở92.25–104.95. Bản người dùng chỉ giữ84.25–87.583 (lẫy số/cảm biến), rồi94.483–102.0 chứa camera lùi/điều hòa/rèm điện/sạc. Loại phiên bản nói trước, chọn lượt sau đủ ý, không cắt mất chức năng riêng.
- Bản trợ lý giữ166.1–167.35 “đây khoang máy nè” rồi169.3–176.1; bản người dùng chỉ giữ169.3–176.1 cho lời chứng minh động cơ/hộp số. Không giữ mọi câu mở đầu khi câu sau đã bắt đầu lại tốt hơn.
- Không chuyển dữ kiện Civic sang Camry. Mốc Camry là84.000km. Bản trợ lý dùng cùng cảnh đồng hồ...0511 hai lần, cùng cảnh ghế sau...0491 ởhook vàbody. Dù mỗi lần hợp lời, vẫn trái quy tắc mỗi cảnh một lần cho các lần dựng tiếp theo.
- Bản người dùng còn thay hình minh họa ghế nhớ bằng...0489 và cụm ghế sau bằng nguồn...0235; chỉ dùng các cảnh đã xác minh cùng xe/đúng trang bị trong project mới. Không tự coi mọi nguồn cũ là được phép ghép.

## Thực hiện ngay trong lượt chốt phương án

Gom theo **ý nghĩa**, không theo độ giống chữ: tên/phiên bản, km, điều hòa, ghế sau, cam kết, giá... Với mỗi ý ghi các mốc lượt nói theo thứ tự, lượt được chọn và phần thông tin riêng cần giữ. Bắt đầu xem xét từ lượt cuối; nếu trọn, rõ và đúng dữ kiện thì bỏ các lượt thử trước. Nếu lượt cuối lỗi, chọn lượt trước tốt nhất và ghi lý do. Không ghép vài mảnh của nhiều lượt khi đã có một lượt đầy đủ.

Sau khi chọn, đọc mạch ý của timeline từ đầu đến cuối: cùng một lợi ích bị nói lại bằng chữ khác vẫn là lặp. Có thể giữ thông tin mới hoặc nhắc giá ở mở/kết khi phục vụ rõ vai trò hook/chốt; không dùng ngoại lệ này để giữ cả đoạn tính năng trùng. Hook đưa lời phía sau lên trước phải xử lý phần tương ứng ở thân bài để không phát lại nguyên cụm. Không tự bỏ hook người dùng đã chỉ định cụ thể; giữ yêu cầu và chọn nội dung thân bài bổ sung thay vì lặp.

Lập sổ cảnh nhám theo đường dẫn nguồn chuẩn hóa/asset thật và vai trò đã dùng. Một cảnh được dành cho hook thì không dùng lại trong body; đổi điểm trim, đổi materialID, đổi track hoặc đổi tên file không làm nó thành cảnh mới. Nhiều cảnh riêng biệt trong một file dài chỉ tính riêng khi đã quan sát và xác minh là cảnh khác. Thiếu cảnh phù hợp thì giữ hình chính hoặc dùng cảnh khác đúng ý; không copy/lặp/đóng băng để đủ B-roll. Các mảnh liên tục do split kỹ thuật trong cùng một lần hiện hình không phải tái sử dụng.

Trước build, hai câu hỏi phải trả lời được: **mỗi ý vì sao còn xuất hiện ở những chỗ này? mỗi cảnh nhám đã dùng ở đâu?** Đây là bước kiểm tra phương án hiện có, không thêm vòng nghiên cứu hay ASR toàn nguồn lần nữa.
