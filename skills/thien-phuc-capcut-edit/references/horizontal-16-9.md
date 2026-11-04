# Bản ngang 16:9 — học từ “kia sonet ngang 4”

Kiểm tra ngày17/10/2026: đọc root/active timeline, lần source range, xem cảnh nguồn của cả17clip chính và9B-roll, đối chiếu trực tiếp một số khung trong CapCut. Đây là mẫu đã quan sát; chưa nghe trọn nguồn/bản mix bằng tai, không khẳng định lý do ngữ nghĩa của từng đoạn bị bỏ.

Mẫu cập nhật24/10/2026: đọc [Civic ngang do người dùng sửa](civic-revised-16-9.md) trước lần dựng ngang tiếp theo. Đối chiếu bản trợ lý với bản sửa để học lựa chọn cụ thể; không suy ra độ mượt chỉ từ số giây hoặc số clip.

Hook ngang mới được người dùng duyệt ngày26/10/2026: đọc [bài học Forte](forte-hook-review.md) khi thêm hoặc sửa hook. Hook vẫn không có caption lời nói; dùng lời nguồn, cảnh chứng minh và chữ nhấn riêng.

## Quy tắc người dùng xác nhận

- **Bản16:9 không có caption lời nói. Không tạo auto caption hoặc gắn phụ đề từ bản dọc.** Vẫn dùng brand, chữ ưu đãi, tên xe, odo, bảng cam kết và giá theo mẫu.
- Giữ tiếng nói, nhạc và từng SFX chỉnh được riêng. Hỏi và chờ người dùng đồng ý trước render/export. Học mẫu là chỉ đọc project.
- Dùng đúng brand trong mẫu đang được chỉ định; không tự thay tên chỉ vì skill có tên Ô Tô Thiên Phúc.

## Cách hiểu đúng về trim và nối — người dùng đính chính

**Mục tiêu là người xem thấy thoải mái, mượt mà; không phải cắt trong bao nhiêu giây hoặc giữ bao nhiêu phần trăm nguồn.** Các thống kê và bảng mốc bên dưới chỉ giúp tìm lại ví dụ, không chứng minh chất lượng nhịp dựng và không là công thức cho video mới.

Khi học từng điểm nối, xem/nghe đoạn trước và sau ở tốc độ thường: câu đã đủ ý chưa, còn đầu/cuối âm không, khoảng nghỉ có tự nhiên không; tay chỉ/hướng nhìn/tư thế và chuyển động camera có bị giật không; chi tiết được chèn đã kịp hiểu chưa; âm nền có cụt hay đổi mức bất ngờ không. Xem thêm chuỗi cảnh để biết cảm giác tổng thể, không đánh giá riêng từng clip bằng độ dài.

Tùy điểm nối, có thể chừa thêm hơi nghỉ, dịch mép trim, giữ động tác liền hoặc kéo cảnh nhám qua phần hình khó nối. Đây là lựa chọn theo ngữ cảnh, không yêu cầu cắt đều hoặc thêm transition cho mọi chỗ. Giữ bản16:9 không caption và giữ âm thanh riêng như người dùng đã yêu cầu.

Lần kiểm tra17/10 mới xác minh nguồn/timeline, hình tĩnh và cài đặt âm; chưa nghe/xem toàn bộ chuyển động liên tục. Vì vậy **chưa xác nhận lý do chính xác cho từng điểm cắt hoặc đã đánh giá đủ độ mượt**. Muốn rút ra quyết định dựng cụ thể phải xem/nghe lại đúng điểm nối, không suy ra chỉ từ source range.

## Bản đồ nguồn để tra cứu, không là công thức cắt

- Canvas1920×1080, timeline60fps, dài219,2s (3:39,2).
- Nguồn chính `DJI_20261010083715_0219_D.MP4`, dài236,5s, HEVC2688×1512,59,94fps, AAC. Đây là take ngang riêng, không phải crop take dọc0226/0227.
-17segment giữ cùng thứ tự và tốc độ1×, liền nhau trên timeline. Chỉ10khoảng bị bỏ trong nguồn và0,467s đuôi; tổng bỏ17,3s (~7,3%), giữ92,7%.
-6ranh giới tách clip vẫn nối tiếp thời gian nguồn. Đừng coi mọi vạch chia clip là một lần bỏ lời hoặc ép trim mạnh giống bản dọc.
- Nối bằng cắt thẳng; không có transition giữa clip trong mẫu. Có cảnh nhám che qua điểm trim. Kết riêng bằng **Horizontal Close0,9s**, không sao chép Vertical Close của mẫu dọc.
- Ví dụ: nguồn0–5,017s → timeline0–5,017s; bỏ5,017–5,733s; nguồn5,733–20,833s chia3clip nhưng giữ liên tục; bỏ20,833–22,283s; nối tiếp nguồn22,283s tại timeline20,117s.
- Ví dụ dài hơn: nguồn28,867–57,067s giữ nguyên28,2s trên timeline24,883–53,083s. Giữ mạch nói dài khi cần, không đổi cảnh/cắt lời theo khoảng thời gian đều nhau.
- Kiểm tra khoảng bị bỏ bằng nguồn thực. Đo silence chỉ hỗ trợ: một số đoạn bị bỏ không phải im lặng ở ngưỡng-40dB, nên không tự kết luận tất cả là cắt khoảng lặng.

## Nhịp nội dung và cảnh nhám

Người dùng góp ý sau bản “kia sonet ngang 3”: **cho cảnh nhám đẹp dài hơn một chút để người xem ngắm xe**, thay vì chỉ đủ che điểm nối. Khi còn đoạn pan/reveal hoặc chi tiết đẹp phù hợp lời nói, ưu tiên giữ thêm và chuyển khi chuyển động/ý hình đã trọn. Không áp thời lượng cố định cho mọi cảnh, không kéo quá nguồn hoặc phủ nhầm nội dung. Bản Sonet3 đã được người dùng tự chỉnh lại; không tự sửa tiếp project đó khi chỉ được yêu cầu ghi nhớ.

Nguồn đưa người giới thiệu đi quanh xe → ghế/hàng sau → vị trí lái/trang bị/odo → khoang máy/tình trạng → cam kết → giá/quà/lời kết. Trình tự này được xác minh bằng cảnh và chữ; không phải transcript đầy đủ.

9cảnh nhám trên track tắt tiếng, tổng55,917s (~25,5%video). Phần lớn hình vẫn là người bán giới thiệu trực tiếp; không phủ kín như bản ngắn.

| Timeline (giây) | Cảnh/nguồn | Vai trò hình ảnh |
|---|---|---|
|6,883–13,200|0212,10/10|Chính diện xe; banner tên xe|
|20,117–27,033|0211,10/10|Góc chéo ngoại thất; phủ điểm trim24,883s|
|27,033–35,383|0216,10/10|Đuôi xe, nối thẳng từ cảnh ngoại thất trước|
|67,267–75,283|0960,24/9|Ghế/hàng sau|
|75,283–84,850|0199,10/10|Ghế trước nhìn từ sau; phủ điểm trim84,333s|
|119,533–125,483|0201,10/10|Toàn bộ vị trí lái/táp-lô|
|125,483–128,133|0222,10/10|Cận đồng hồ/odo|
|141,067–146,733|0223,10/10|Màn hình, cụm điều khiển|
|146,733–149,217|0956,24/9|Nội thất/cửa trước|

Có tái sử dụng2cảnh quay cũ24/9 với7cảnh10/10; chỉ tái dùng khi xác minh cùng xe/trang bị. Không thay nguồn chính bằng cảnh cũ. Hai cảnh nối trực tiếp có thể tạo chuỗi hình liên tục qua nhiều câu; không bắt buộc trở về người bán ở mỗi điểm cắt thoại.

## Brand, chữ và màu

- Brand thật trong mẫu: **XE CŨ SÀI GÒN**, dòng dưới **0972608010**, đặt nhỏ ở góc trái trên. Tên trắng, số vàng**#F0FF00**, cả hai viền đen, font resource Roboto-Blk (tên nội bộ Roboto Condensed Black).
- Brand là preset ghép2text trong compound clip. Mẫu lặp compound dài122,15s để phủ tiếp timeline; đây là lớp nhận diện, không phải caption. Giữ lớp này chỉnh được, kiểm tra độ phủ khi đổi tổng thời lượng.
- Bảng màu chữ: **đỏ/trắng/đen** cho banner ưu đãi và tên xe; **vàng#F0FF00/đen** cho số điện thoại, odo và cam kết. Không tự dùng bố cục hook đỏ/trắng phía trên của bản dọc.

| Thời gian | Chữ/template | Bố cục đã xem |
|---|---|---|
|0,4–3,2s|TITLE LOWER THIRD EN: “Giảm Ngay10Tr” + tên xe|Góc trái dưới; chữ giảm giá đen trên trắng, tên xe trắng trên đỏ, cột đỏ bên trái; scale tổng56%|
|3,2–5,483s|Title EN - Title Here: “Tặng2Tr Check Hãng”|Dải trắng giữa phía dưới, chữ đen, hai đầu nhấn đỏ; scale~56%|
|6,883–12,583s|News - Highlight: tên xe|Banner đỏ, chữ trắng nghiêng, dưới cảnh chính diện xe; scale38%|
|13,2–16,2s|“Odo:16.500km”|Chữ vàng viền đen phía dưới; font size15, scale~45,5%; Showing Down0,5s vào/Sliding Drop0,5s ra|
|195,133–198,767s|“Cam Kết Chất Lượng” và4ý|Block góc trái dưới; chữ vàng viền đen, căn trái, font size10; nền trắng50%opacity, bo góc|
|206,1–208,033s|“Giá:438Tr”|Trắng viền đen, giữa phía dưới, font size15, scale~60%; Drift Reunion~0,983s|
|208,217–210,15s|“Tặng2Tr Check Hãng”|Cùng bố cục trắng viền đen, Drift Reunion|

Số tiền/odo/năm/tên xe ở bảng là nội dung của Sonet mẫu, không phải dữ liệu mặc định cho xe mới. Cỡ chữ ghi bằng đơn vị CapCut, không phải pixel. Các font text trong mẫu đều trỏ resource Roboto Condensed Black; không mang cỡ8 của phụ đề dọc sang bản ngang.

**Cam kết: lấy trực tiếp preset “cam kết xe” tại Text → Yours → Presets**. Đọc [commitment-preset.md](commitment-preset.md) để dùng đúng câu chữ, thiết kế và cách thay block đã được người dùng duyệt trong “camry ngang 6”. Giữ đủ4ý của preset, căn ở góc trái dưới, không tự tóm tắt lại.

Về màu hình: không thấy LUT/filter/HSL/curve được áp trong dữ liệu. Clip chính đã xem trong UI có LUTNone, Temp/Tint/Saturation/Exposure/Contrast=0, AutoAdjust/ColorMatch/ColorCorrection tắt. Bài học là giữ màu nguồn tự nhiên của mẫu; không tự gán một công thức grading hoặc khẳng định mọi clip đều có xử lý giống nhau chỉ từ các cờ enable.

## Nhạc và SFX

- Tiếng nói gắn từng clip video chính: **đặt +10dB** theo quy tắc người dùng xác nhận sau bản Camry ngang6, kể cả take mới. Không tự thay bằng −1,5dB theo phép đo đỉnh. Giữ cảnh nhám mute và nhạc/SFX riêng; +10dB là gain, không phải LUFS.
- **Mustang March(phonk)** riêng track, gain~-19,3dB. Clip đầu0–193,733s; clip thứ hai193,733–219,2s lấy lại từ đầu bản nhạc; nối thẳng, không thấy crossfade. Fade-out cuối~0,917s.
- SFX riêng: **Flame magic sound effects** ở0–2,1s (lấy từ nguồn0,617s); **Magic reveal** ở0,4s,3,2s,13,2s,208,217s; **Ding** ở194,95s; **Money,coin,cash register,shop,accounting1** ở206,1s.
- Như vậy7lượtSFX trên2track, nhạc trêntrackthứ3. SFX gain0dB ở mẫu; dùng theo gain/nguồn thực, không gộp thành1lineâm.
- SFX đi với chữ/ý: Flame mở đầu, Magic cho ưu đãi/odo/quà, Ding báo cam kết (sớm hơn text~0,183s), Money khi xuất giá. Không thêm Swish/UI Prompt của bản dọc chỉ vì thuộc thư viện quen dùng; cũng không rải SFX ở mọi B-roll/cut.
- Có xác minh clip, mốc, fade và gain; **chưa nghe trọn bằng tai**. Chưa được kết luận mọi nối âm/độ cân bằng mix đã tốt từ các thông số này.

## Phạm vi sử dụng lại

Áp dụng các quan sát trên như mẫu tham chiếu bản ngang do người dùng chọn, không như công thức bất biến cho toàn bộ kênh. Mẫu ngang người dùng sửa sau này được ưu tiên. Không render để kiểm tra nếu chưa được người dùng đồng ý.

Bằng chứng chi tiết nếu workspace còn tồn tại: `C:/Users/tranp/Documents/Codex/2026-10-15/b-n/work/sonet-horizontal-study/` chứa snapshot chỉ đọc, `edit-map.json`, `cut-source-map.md`, ảnh nguồn và log đo nguồn. Không cần các file này để hiểu quy tắc trong tài liệu.
