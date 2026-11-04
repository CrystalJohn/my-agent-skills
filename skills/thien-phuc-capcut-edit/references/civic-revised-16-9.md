# Civic ngang — học từ bản người dùng sửa ngày 24/10/2026

Đối chiếu `Civic 1.8G 2020-ngang 1` do người dùng sửa với bản trợ lý vừa bàn giao. Mẫu này mới hơn Sonet ngang4; ưu tiên các lựa chọn quan sát được dưới đây khi dựng bản ngang tiếp theo. Đây là ví dụ quyết định dựng, không phải sơ đồ để sao chép timestamps, số cảnh hoặc dữ kiện sang xe khác.

## Phạm vi bằng chứng

Đã đọc root/active timeline và compound, đối chiếu source range, cảnh nguồn, nội dung chữ, vị trí và các clip âm; mở CapCut xác minh project và khung giá đã hiện đầy đủ. Transcript ASR chỉ hỗ trợ tìm ý, còn nhiều lỗi từ/ngắt câu; không dùng nó làm lời chuẩn. Chưa nghe trực tiếp trọn mix hoặc xem liên tục toàn bộ chuyển động của bản sửa, nên chưa xác nhận lý do chính xác của từng mép cắt, hơi nghỉ hay độ cân âm bằng tai.

## Chọn lại lời trước, rồi mới đặt lại lớp minh họa

- Bản trợ lý giữ 7 clip lời, bản người dùng chia thành 17 clip. Ý chính vẫn đi theo nguồn; người dùng chọn lại ở cấp câu/cụm thay vì giữ nguyên nhiều cụm dài chỉ vì chưa thấy khoảng lặng lớn. Không lấy số clip nhiều hơn làm tiêu chí tốt hơn.
- Ví dụ source: bỏ 40,050–41,583; chọn lại câu phim cách nhiệt bắt đầu 71,733 thay vì 71,100; phần 71,733–132,950 được chia và bỏ các đoạn giữa thay vì giữ liền một khối. Cụm lái/vô lăng giữ 136,233–138,383 rồi nối 144,650, thay vì giữ 135,817–141,900. Đây là vị trí tra nguồn, không phải quy tắc bỏ từ dựa trên ASR.
- Sau khi đổi lời, dựng lại quan hệ lời–hình–chữ–SFX theo **timeline mới**. Không chỉ trừ một độ lệch chung hoặc dời mọi lớp sau một điểm cắt; mỗi ý cần dò lại vì có nhiều lần trim ở giữa.
- B-roll có thể che mép nối hoặc bắt đầu trước chủ đề kế tiếp một chút để hình liền, nhưng phải còn liên quan cả cụm. Câu nói vẫn phải nghe trọn, không dùng hình che để bỏ qua lỗi nối âm. Xem/nghe lại ở tốc độ thường trước khi chốt.

## Cảnh nhám theo chi tiết đang bán, không phủ để đủ số lượng

| Ví dụ trong bản sửa (timeline) | Thay đổi thực tế | Cách dùng cho video sau |
|---|---|---|
|11,600–22,100|Đổi góc ngoại thất mở đầu sang clip `095412`, giữ khoảng ngắm 10,5s|Chọn góc đẹp phù hợp vai trò mở xe; không mặc định nguồn đầu tiên trong thư viện|
|22,250–26,250|Vẫn có chữ odo đầu video nhưng bỏ cảnh đồng hồ ở đây|Không buộc mọi text phải kéo theo một B-roll; xét cảnh chính đang thể hiện gì|
|53,417–57,050|Thêm cận mâm/lốp `095346` trong cụm nói tình trạng lốp|Dùng hình chứng minh đúng bộ phận, thay vì phủ góc toàn xe suốt cụm|
|64,450–71,333 rồi 71,333–74,633|Ghế sau nối liền cửa gió|Giữ chuỗi nội thất có quan hệ, không trở về người giới thiệu ở mỗi ý nhỏ|
|86,200–91,600|Thêm khoang hành lý/lốp dự phòng `095454` trong cụm quanh xe|Xem đủ thư viện để chọn chi tiết hữu ích; không chỉ dùng các góc dễ thấy đầu tiên|
|96,133–103,467 rồi 103,467–107,433|Cockpit `.mov` nối đồng hồ/odo|Cảnh đồng hồ được đặt lại vào cụm nói odo xuất hiện lần sau; không nhầm hai lần nhắc cùng thông tin|
|110,633–121,917|Hai góc táp-lô/vô lăng nối nhau|Phân biệt lời về cảm giác lái, vô lăng và trang bị; tránh dùng một góc chung cho mọi ý|
|127,183–135,067|Màn hình và cụm điều khiển `.mov`|Minh họa cụm chức năng khi người giới thiệu đang nói đến chúng|
|141,817–145,217|Thêm góc đuôi xe `095436`|Bổ sung góc còn thiếu nếu phù hợp ngữ cảnh và nhịp quay quanh xe|
|Cụm giá cuối|Bỏ cảnh chính diện xe trợ lý từng phủ qua đoạn này, để người bán và xe mở nắp capo hiện trực tiếp|Không cần che mọi điểm nối bằng B-roll; giữ người giới thiệu khi cảnh chính phục vụ bán hàng và bố cục chữ tốt|

Các thời lượng thay đổi theo từng cảnh: có cảnh giữ dài, có cảnh rút và đổi nguồn. Bài học không phải kéo dài tất cả. Giữ chuyển động đẹp còn hữu ích, cho chi tiết đủ thời gian nhận ra, rồi chuyển theo lời/động tác. Track cảnh chèn trong snapshot tắt tiếng (`flag=2`); một số segment có volume=1 vẫn bị mute bởi track. Kiểm tra trạng thái hiệu lực cả track và clip, không kết luận từ một trường gain.

## Hook và chữ nhấn bán hàng

- Mở đầu thay lợi ích `Xe Nhật Nhập Khẩu` bằng **`Lái Hay, Bền, Tiết Kiệm`**, giữ tên `Honda Civic 1.8G 2020` trong lower third. Đây là hook ngắn, nhiều lợi ích phù hợp xe; nhập khẩu vẫn có thể nằm trong lời, không cần biến mọi thông tin thành hook. Không mặc định ưu đãi giảm tiền khi nguồn không có.
- Chữ nhiên liệu đổi sang template **Title EN - Daily Vlog**, scale khoảng38,5%, vùng dưới; không chỉ thay text trong template cũ. Khi học phải xem cả thiết kế/resource, không chỉ đọc chuỗi chữ.
- Giá **538Tr** ở khoảng170,467–173,467, được dời từ góc phải trên xuống khoảng trống **nền đường phía dưới**. CapCut đã xác minh chữ hiện dưới xe, cạnh vùng chân người mà không đè lên xe/mặt. Không biến tọa độ này thành vị trí giá cố định cho xe khác.
- Thêm **`Trả Trước 220Tr Nhận Xe`** khoảng176,700–179,700, sau giá, cùng kiểu trắng viền đen vùng dưới. Chọn thông tin tài chính có thật trong nguồn và nhấn ở đúng lúc người bán nói; không chỉ có giá rồi bỏ qua lợi ích mua xe. Số 538/220 là dữ kiện riêng bản người dùng này, không là mặc định; ASR đoạn tiền trả trước nhận dạng sai nên không dùng để tự sửa số.
- Cuối dùng compound **My presets2** khoảng180,333–184,850: `Thu Xe tại nhà giá tốt nhất` và `Hỗ trợ tất toán bank và tất cả thủ tục pháp lý`. Khi nguồn có ý thu đổi và phù hợp yêu cầu, dùng preset thật của người dùng; không thay bằng title “Liên Hệ Em Chương/Trương”. Đây là lớp thông tin dịch vụ, không phải caption lời nói. Kiểm tra bố cục compound trong UI trước khi dùng ở video mới.
- Bảng cam kết vẫn giữ đủ4 ý preset, nhưng được đặt lại khoảng163,733–167,483. Không lấy thời điểm đặt của trợ lý trước làm chuẩn hoặc tự suy diễn rằng mọi bảng phải hiện đúng3,75s.

## SFX gắn với sự kiện chữ

Ngoài các clip đã giữ riêng, người dùng thêm **Magic reveal** ở tên xe11,350 và chữ trả trước176,700; thêm **Culin. It looks like a light bulb mark is on the head.** ở preset dịch vụ180,333. Money theo giá170,467; Ding trước bảng cam kết khoảng0,183s. Mỗi clip còn chỉnh riêng; không gộp mix và không thêm SFX ở mọi điểm cắt/B-roll.

Main speech vẫn +10dB, nhạc Mustang March khoảng−19,3dB. SFX trong bản này có cả0dB và−6dB; đó là lựa chọn từng clip, không phải mức chung cần áp hàng loạt. Chưa nghe trọn nên không xác nhận cân âm chỉ từ gain.

## Kiểm tra phần đuôi khi lấy mẫu

Nội dung chính và nhạc trong snapshot kết ở185,250s, Horizontal Close184,350–185,250. Nhưng compound brand thứ hai còn kéo tới201,016666s, đúng tổng thời lượng UI03:21:01. Không diễn giải rằng bản nội dung chỉ ngắn hơn bản trợ lý3,517s, cũng không sao chép phần brand thừa làm phong cách kết. Đây là chi tiết cần kiểm tra trước render trong lần edit được cấp quyền tiếp theo; **không sửa bản người dùng khi nhiệm vụ chỉ là học**.

Bằng chứng đối chiếu được giữ ở workspace `C:/Users/tranp/Documents/Codex/2026-10-15/b-n/work/civic_horizontal_edit/user-revision/`: `comparison.json`, `snapshot.json`; bản trợ lý đối chứng ở `../prepared/draft_content.json`. Tài liệu này tự đủ dùng nếu các snapshot không còn.
