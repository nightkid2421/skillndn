# skillndn

Bộ sưu tập skill đã được lọc từ các skill cài trên máy, để chia sẻ cho Codex và các agent hỗ trợ định dạng `SKILL.md`.

Snapshot ngày **03/11/2026**: rà soát **46 skill**, đóng gói **12 skill**, ghi nhận **34 skill không phân phối** do giấy phép độc quyền, hạn chế phân phối hoặc chưa có giấy phép rõ ràng. Xem toàn bộ [danh mục](CATALOG.md) và [manifest](manifest.json).

## Cài đặt

Yêu cầu Git và Python 3. Clone repo:

```bash
git clone https://github.com/nightkid2421/skillndn.git
cd skillndn
python3 scripts/verify.py
python3 scripts/install.py --list
```

Cài từng skill vào Codex:

```bash
python3 scripts/install.py para-memory-files paperclip
```

Hoặc cài tất cả skill đã đóng gói:

```bash
python3 scripts/install.py --all
```

Mặc định cài vào `$CODEX_HOME/skills`, hoặc `~/.codex/skills` khi chưa đặt `CODEX_HOME`. Thư mục đã tồn tại sẽ không bị ghi đè; nếu có xung đột, lệnh dừng trước khi sao chép. Để cài cho agent khác, chỉ định thư mục skill của agent đó:

```bash
python3 scripts/install.py para-memory-files --dest /path/to/agent/skills
```

Agent cần hỗ trợ phát hiện `SKILL.md`; nếu không, cấu hình agent đọc skill được chọn theo cơ chế của nền tảng đó. Sau khi cài, mở lượt chat mới hoặc nạp lại agent theo hướng dẫn của nền tảng.

## Skill có trong repo

- **Agent và bộ nhớ:** `create-agent-adapter`, `paperclip`, `paperclip-create-agent`, `para-memory-files`.
- **Tài liệu và bảng tính:** `pdf`, `presentations`, `spreadsheets`, `excel-live-control`.
- **Công cụ:** `imagegen`, `openai-docs`, `skill-creator`, `skill-installer`.

Mỗi thư mục giữ nguyên `SKILL.md` và tài nguyên hỗ trợ từ bản cài gốc; bổ sung giấy phép/nguồn giấy phép khi cần, bỏ cache Python và tệp rác. Repo chỉ cung cấp hướng dẫn/tài nguyên của skill, không cấp tài khoản, API key, quyền truy cập hoặc runtime riêng.

`paperclip` cần dịch vụ Paperclip và biến môi trường được cấu hình; `imagegen` cần công cụ tạo ảnh tương thích; các skill tài liệu, slide và bảng tính có thể gọi công cụ Codex/ChatGPT, artifact runtime hoặc kết nối ứng dụng tương ứng. `excel-live-control` cần phiên Excel được kết nối. Chép thư mục skill sang agent khác không tự tạo những công cụ này.

## Giấy phép và nguồn gốc

Các skill giữ giấy phép của chủ sở hữu gốc; xem [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Giấy phép MIT ở thư mục gốc chỉ áp dụng phần đóng gói, hướng dẫn và script mới của repo này, không thay thế giấy phép của skill bên thứ ba.

Các skill bị loại chỉ được liệt kê tên, nguồn và lý do trong danh mục, không kèm nội dung hay tài nguyên của chúng. Với các skill này, hãy cài plugin chính thức và sử dụng trong môi trường được cấp phép.

## Kiểm tra

```bash
python3 scripts/verify.py
```

Manifest ghi SHA-256 của từng tệp skill để kiểm tra tính toàn vẹn của snapshot. Đây là bản chụp tại thời điểm đóng gói, không tự đồng bộ với phiên bản upstream mới.
