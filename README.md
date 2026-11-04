# My agent skills

Bản sao các skill đang có trên máy, lập ngày 2026-11-04 để lưu phiên bản và chuyển sang máy khác.

## Nội dung

| Nhóm | Số skill có nội dung trong repo |
|---|---:|
| Skill cài riêng: skills/ | 42 |
| Skill hệ thống có giấy phép Apache kèm theo: system-skills/ | 4 |
| Snapshot skill Vercel và tài nguyên hỗ trợ: plugins/vercel/ | 54 |
| Tổng | 100 |

inventory.json ghi đủ 135 skill đã kiểm kê: 100 được sao lưu và 35 chỉ ghi tên/nguồn để cài lại. Đây là số file skill trên ổ đĩa, không phải số skill đang bật trong mọi phiên.

## Dùng trên máy khác với Codex

1. Đăng nhập GitHub bằng tài khoản có quyền đọc repo. Nếu repo chuyển private, máy mới vẫn cần quyền đó.
2. Để cài một skill, yêu cầu Codex:

   > Dùng $skill-installer cài skill từ repo CrystalJohn/my-agent-skills, đường dẫn skills/learning-product-ux.

3. Hoặc clone repo và chép nguyên các thư mục muốn dùng trong skills/ vào thư mục skill cá nhân mà Codex trên máy mới hỗ trợ (tài liệu hiện tại: ~/.agents/skills/). Giữ cả references/, scripts/, assets/ và agents/ nếu có. Tránh cài hai bản cùng tên vào nhiều đường dẫn.
4. Nếu skill chưa xuất hiện, mở phiên mới hoặc khởi động lại Codex.
5. Sau khi nâng cấp bản gốc, commit/push cập nhật repo. Trên máy khác, pull rồi cập nhật các bản đã cài. git pull trong repo không tự thay đổi những bản đã được chép sang thư mục skill.

Tài liệu: https://learn.chatgpt.com/docs/build-skills

Không cần cài lại system-skills nếu Codex đã cung cấp bản phù hợp. Các skill/plugin cần công cụ, tài khoản hoặc phần mềm tương ứng; sao chép hướng dẫn không cài các công cụ đó.

## Plugin và ChatGPT

Các plugin do ứng dụng quản lý nên cài lại từ nguồn gốc để có đúng công cụ và tài nguyên. Snapshot Vercel ở đây là bản lưu nội dung, không đăng ký connector hay tự tạo một plugin đã cài.

Với ChatGPT web/mobile, repository này không tự trở thành skill trong tài khoản. Cần đóng gói/cài qua luồng plugin được hỗ trợ. Tài liệu: https://learn.chatgpt.com/docs/skills-and-plugins

## 35 skill không sao chép nội dung

- 1 skill hệ thống review-agent: không tìm thấy giấy phép phân phối độc lập trong bản cài.
- 34 skill từ các plugin do ứng dụng quản lý: computer-use, visualize, openai-templates, plugin-management, sites, work-pets và các công cụ tài liệu/bảng tính/trình chiếu.
- Giấy phép documents cấm trích xuất, giữ bản sao ngoài dịch vụ và phân phối; không sao chép nội dung đó. Các plugin còn lại chưa xác lập quyền phân phối riêng nên được ghi danh mục để cài lại.

Thay đổi repo thành private không thay thế quyền phân phối.

## Nguồn và giới hạn

Giữ các LICENSE/NOTICE đi kèm; xem THIRD_PARTY.md và licenses/. Không áp dụng một giấy phép chung lên mọi nguồn.

Đây là snapshot đúng phần đã cài, không phải cam kết mọi skill chạy độc lập. Ví dụ ui-ux-pro-max hiện có hướng dẫn gọi scripts/search.py nhưng script đó không có trong thư mục nguồn đã sao lưu; cần cài đủ bộ từ nguồn gốc trước khi dùng chức năng tìm kiếm đó. Một số skill tham chiếu phần mềm, đường dẫn dự án hoặc tài liệu nằm ngoài thư mục skill; máy mới cần điều chỉnh theo môi trường.

Không sao lưu thông tin đăng nhập, cấu hình tài khoản Codex, lịch sử chat, node_modules hay bộ nhớ đệm Python. Nội dung skill và ví dụ dự án được giữ theo bản nguồn; rà soát tự động các mẫu khóa/token phổ biến không thay thế kiểm toán bảo mật toàn diện.
