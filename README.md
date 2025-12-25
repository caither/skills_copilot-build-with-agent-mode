# OctoFit Tracker - 健身追蹤應用程式

[![GitHub Codespaces](https://img.shields.io/badge/Open%20in-GitHub%20Codespaces-blue?logo=github)](https://github.com/codespaces)
[![Django](https://img.shields.io/badge/Django-4.1.7-green.svg)](https://www.djangoproject.com/)
[![React](https://img.shields.io/badge/React-18.x-blue.svg)](https://reactjs.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB-6.0-green.svg)](https://www.mongodb.com/)

> 使用 GitHub Copilot Agent Mode 建構的現代化健身追蹤應用程式

## 📖 專案簡介

OctoFit Tracker 是為 Mergington 高中開發的健身追蹤應用程式，旨在透過遊戲化和社交競賽機制激勵學生保持運動習慣。本專案展示如何使用 GitHub Copilot Agent Mode 加速全端應用程式開發。

### 核心功能

- ✅ **使用者管理** - 註冊、登入與個人檔案
- 📊 **活動追蹤** - 記錄跑步、走路、力量訓練等活動
- 👥 **團隊系統** - 建立與管理運動團隊
- 🏆 **競爭排行榜** - 即時排名與月度挑戰
- 💡 **個人化建議** - 基於健身等級的訓練建議

## 🏗️ 技術架構

### 技術棧

| 層級 | 技術 | 埠口 |
|------|------|------|
| 前端 | React.js + Bootstrap + React Router | 3000 |
| 後端 | Django 4.1 + Django REST Framework | 8000 |
| 資料庫 | MongoDB 6.0 | 27017 |
| 開發環境 | GitHub Codespaces (Dev Container) | - |

### 專案結構

```
octofit-tracker/
├── backend/
│   ├── venv/                    # Python 虛擬環境
│   ├── octofit_tracker/         # Django 專案主目錄
│   │   ├── settings.py          # 專案設定
│   │   ├── urls.py              # URL 路由
│   │   └── ...
│   ├── api/                     # REST API 應用程式
│   └── requirements.txt         # Python 相依套件
│
└── frontend/
    ├── src/                     # React 原始碼
    │   ├── components/          # React 元件
    │   ├── pages/               # 頁面元件
    │   └── App.js               # 主應用程式
    ├── public/                  # 靜態資源
    └── package.json             # npm 配置
```

## 🚀 快速開始

### 前置需求

- GitHub 帳號（使用 Codespaces）
- 或本機安裝：
  - Python 3.8+
  - Node.js 16+
  - MongoDB 6.0+

### 使用 GitHub Codespaces（推薦）

1. **開啟 Codespace**
   ```bash
   # 自動執行 postCreateCommand 和 postStartCommand
   # 安裝所有相依套件並啟動 MongoDB
   ```

2. **建立 Python 虛擬環境**
   ```bash
   python3 -m venv octofit-tracker/backend/venv
   source octofit-tracker/backend/venv/bin/activate
   ```

3. **安裝後端相依套件**
   ```bash
   pip install -r octofit-tracker/backend/requirements.txt
   ```

4. **初始化 Django 專案**
   ```bash
   cd octofit-tracker/backend
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. **啟動後端伺服器**
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

6. **安裝並啟動前端**（新終端）
   ```bash
   npm install --prefix octofit-tracker/frontend
   npm start --prefix octofit-tracker/frontend
   ```

7. **存取應用程式**
   - 前端：`https://{CODESPACE_NAME}-3000.app.github.dev`
   - API：`https://{CODESPACE_NAME}-8000.app.github.dev/api/`
   - Admin：`https://{CODESPACE_NAME}-8000.app.github.dev/admin/`

### 本機開發

請參閱 [安裝指南](docs/installation.md) 了解詳細的本機安裝步驟。

## 📚 文件

- [專案故事](docs/octofit_story.md) - OctoFit Tracker 的發展背景
- [安裝指南](docs/installation.md) - 完整安裝與設定說明
- [API 文件](docs/api.md) - REST API 端點參考
- [設定說明](docs/configuration.md) - 環境變數與設定選項
- [Django 後端指引](.github/instructions/octofit_tracker_django_backend.instructions.md)
- [React 前端指引](.github/instructions/octofit_tracker_react_frontend.instructions.md)

## 🛠️ 開發工具

### GitHub Copilot

本專案使用 GitHub Copilot Agent Mode 加速開發：

- **程式碼生成** - 自動生成 Django 模型、API 端點、React 元件
- **測試撰寫** - 生成單元測試與整合測試
- **文件維護** - 同步更新程式碼與文件
- **問題排查** - 協助除錯與效能優化

### 開發容器擴充

- `github.copilot` - GitHub Copilot + Copilot Chat
- `ms-python.python` - Python 語言支援
- `ms-python.vscode-pylance` - Python 語言伺服器
- `ms-python.debugpy` - Python 除錯工具

## 🔧 設定

### 環境變數

後端 Django 自動偵測 Codespace 環境：

```python
# settings.py
if os.environ.get('CODESPACE_NAME'):
    ALLOWED_HOSTS.append(f"{os.environ.get('CODESPACE_NAME')}-8000.app.github.dev")
```

### MongoDB 連線

```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'HOST': 'localhost',
        'PORT': 27017,
    }
}
```

## 🧪 測試

```bash
# 後端測試
cd octofit-tracker/backend
python manage.py test

# 前端測試
npm test --prefix octofit-tracker/frontend
```

## 📦 部署

詳細部署指南請參考 [部署文件](docs/deployment.md)。

## 🤝 貢獻

歡迎提交 Pull Request！請確保：

1. 遵循專案的程式碼風格
2. 更新相關文件
3. 新增適當的測試
4. 通過所有現有測試

## 📄 授權

本專案採用 MIT 授權 - 詳見 [LICENSE](LICENSE) 檔案。

## 🔗 相關連結

- [GitHub Copilot 文件](https://docs.github.com/en/copilot)
- [Django 文件](https://docs.djangoproject.com/)
- [React 文件](https://react.dev/)
- [MongoDB 文件](https://www.mongodb.com/docs/)

## 💬 支援

如有問題或建議，請：

- 開啟 [GitHub Issue](../../issues)
- 參考 [常見問題](docs/faq.md)
- 查看 [專案 Wiki](../../wiki)

---

**使用 GitHub Copilot Agent Mode 打造** 🚀


