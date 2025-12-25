# Prompt 輸出記錄

本文件記錄 GitHub Copilot 在本專案中所有文字輸出的追溯日誌。

---

## 記錄格式說明

每筆記錄包含以下欄位：

- **記錄時間**：ISO 8601 格式（UTC 時區）
- **變更範圍**：涉及的主要檔案或模組
- **Prompt**：使用者需求精簡轉述
- **Output**：完整輸出內容
- **Notes**：假設、限制或需確認事項

---

### 2025-12-24T12:44:33Z

- **Scope**: README.md, docs/Prompt-Output.md, docs/installation.md, docs/api.md, docs/configuration.md
- **Prompt**: 使用者要求依照指示產生及更新說明文件，包括分析專案技術架構後更新 README.md 及建立相關文件
- **Output**:

已完成以下文件更新與建立：

#### 1. README.md 更新

更新了專案主要說明文件，包含：

- **專案簡介**：OctoFit Tracker 的目的與背景
- **核心功能**：列出 5 大主要功能
- **技術架構**：
  - 技術棧表格（前端/後端/資料庫）
  - 專案結構樹狀圖
- **快速開始**：
  - GitHub Codespaces 使用步驟（推薦）
  - 本機開發安裝指引
  - 7 步驟完整設置流程
- **文件連結**：指向各類技術文件
- **開發工具**：GitHub Copilot 與 VS Code 擴充說明
- **設定範例**：環境變數與 MongoDB 連線設定
- **測試指令**：後端與前端測試命令
- **貢獻指南**：參與專案的基本規則
- **授權與相關連結**

#### 2. docs/Prompt-Output.md 建立

依照指示建立 Prompt 輸出記錄檔，用於追溯所有文字輸出：

- 建立記錄格式說明
- 新增首筆記錄（本次更新）
- 採用 ISO 8601 時間格式（UTC）

#### 3. 文件特色

- **語言**：全部使用繁體中文，符合臺灣地區語言習慣
- **結構清晰**：使用 Markdown 格式化、表格、程式碼區塊
- **圖示增強**：使用 emoji 提升可讀性
- **完整性**：包含從安裝到部署的完整流程
- **連結整合**：串接各類技術文件與外部資源

#### 4. 待建立文件（參考連結已加入 README）

以下文件在 README 中已參考，但尚未建立實體檔案：

- `docs/installation.md` - 詳細安裝指南
- `docs/api.md` - REST API 端點參考
- `docs/configuration.md` - 設定選項說明
- `docs/deployment.md` - 部署指南
- `docs/faq.md` - 常見問題

這些文件可在後續開發過程中依需要建立。

#### 5. 遵循的指令規則

本次更新完全遵循 `.github/instructions/update-docs-on-code-change.instructions.md` 的規範：

- ✅ 使用繁體中文撰寫
- ✅ 文件內容與專案架構分析結果同步
- ✅ 保持結構清晰易讀
- ✅ 包含實際可用的範例與指令
- ✅ 建立 Prompt-Output.md 記錄檔
- ✅ 記錄時間採用 ISO 8601 (UTC)

- **Notes**:
  1. README.md 中參考的部分文件檔案（installation.md、api.md 等）尚未建立，僅先建立參考連結
  2. 實際的 Django 和 React 應用程式尚未建立，README 中的指令為預期流程
  3. 後續當實際程式碼建立後需要再次更新文件以反映真實的 API 端點、設定參數等細節

---

### 2025-12-24T12:47:41Z

- **Scope**: docs/installation.md, docs/api.md, docs/configuration.md, docs/Prompt-Output.md (update)
- **Prompt**: 依照 update-docs-on-code-change.instructions.md 指示，建立詳細的技術文件包括安裝指南、API 文件、設定說明
- **Output**:

已成功建立以下三份詳細技術文件：

#### 1. docs/installation.md - 安裝指南

**內容概要**：
- **GitHub Codespaces 安裝**（推薦方式）
  - 優點說明（預配置環境、自動安裝、無需本機軟體）
  - 4 步驟快速啟動流程
- **本機開發環境設定**
  - 前置需求表格（Python, Node.js, MongoDB, Git）
  - 6 大安裝步驟：
    1. 複製專案
    2. 建立專案結構
    3. 設定後端（虛擬環境、requirements.txt、Django 初始化）
    4. 設定前端（React 應用程式、Bootstrap、React Router）
    5. 啟動 MongoDB（多平台指令）
- **驗證安裝**
  - 後端伺服器啟動驗證
  - 前端伺服器啟動驗證
  - MongoDB 連線測試
- **常見問題排解**
  - MongoDB 無法啟動
  - Django 資料庫錯誤
  - React CORS 問題
  - Python 虛擬環境問題
- 包含完整的程式碼範例與指令

#### 2. docs/api.md - REST API 文件

**內容概要**：
- **基礎資訊**
  - Base URL（Codespaces 與本機）
  - Token 認證方式
  - 通用回應格式（成功/錯誤）
- **認證 API**
  - 註冊新使用者 (`POST /api/auth/register/`)
  - 登入 (`POST /api/auth/login/`)
  - 登出 (`POST /api/auth/logout/`)
- **使用者管理 API**
  - 取得個人資料 (`GET /api/users/profile/`)
  - 更新個人資料 (`PATCH /api/users/profile/`)
- **活動追蹤 API**
  - 記錄新活動 (`POST /api/activities/`)
  - 取得活動歷史 (`GET /api/activities/`)
  - 取得活動統計 (`GET /api/activities/stats/`)
  - 支援 6 種活動類型（跑步、走路、騎車、力量訓練、瑜珈、其他）
- **團隊管理 API**
  - 建立團隊 (`POST /api/teams/`)
  - 加入團隊 (`POST /api/teams/{team_id}/join/`)
  - 取得團隊列表 (`GET /api/teams/`)
- **排行榜 API**
  - 個人排行榜 (`GET /api/leaderboard/users/`)
  - 團隊排行榜 (`GET /api/leaderboard/teams/`)
- **訓練建議 API**
  - 個人化訓練建議 (`GET /api/recommendations/`)
- **錯誤處理**
  - HTTP 狀態碼表格
  - 錯誤碼列表（AUTH_REQUIRED, INVALID_CREDENTIALS 等）
  - 錯誤回應範例
- **測試範例**
  - 完整的 curl 指令範例

每個 API 端點都包含：
- 請求格式（JSON）
- 回應格式（JSON）
- 狀態碼說明
- 參數說明

#### 3. docs/configuration.md - 設定說明

**內容概要**：
- **環境變數**
  - 後端環境變數（SECRET_KEY, DEBUG, DB_NAME 等）
  - 前端環境變數（REACT_APP_API_URL）
- **Django 後端設定**
  - ALLOWED_HOSTS（自動偵測 Codespace）
  - 資料庫設定（Djongo + MongoDB）
  - CORS 設定（完整的 middleware 配置）
  - REST Framework 設定（認證、分頁、渲染器）
  - 認證設定（Django Allauth）
- **React 前端設定**
  - package.json 範例
  - API 連線設定（自動偵測 Codespace 的 JavaScript 程式碼）
- **MongoDB 設定**
  - 基本連線設定
  - 建議的集合結構
  - 索引設定（使用者、活動、團隊）
  - 效能調校參數
- **開發環境設定**
  - devcontainer.json 完整配置
  - 埠口可見性設定
  - VS Code settings.json
  - VS Code launch.json（Django 和 React 除錯配置）
- **安全性設定**
  - 生產環境建議（HTTPS, HSTS, Cookies）
  - 密碼政策（密碼驗證器）
- **日誌設定**
  - Django LOGGING 完整配置
  - 格式化器與處理器
- **效能設定**
  - 快取設定（排行榜快取）
  - 資料庫連線池

#### 4. 更新 docs/Prompt-Output.md

新增本次記錄到輸出日誌檔案。

#### 文件特色

1. **完整性**：涵蓋從安裝到生產部署的所有面向
2. **實用性**：包含可直接使用的程式碼範例與指令
3. **結構化**：清晰的目錄、表格、程式碼區塊
4. **繁體中文**：符合臺灣地區語言習慣
5. **情境考量**：同時支援 Codespace 和本機開發
6. **問題排解**：包含常見問題與解決方案

#### 與專案指令的對應

完全遵循 `.github/instructions/` 中的規範：

- ✅ **octofit_tracker_setup_project.instructions.md**
  - 專案結構：`octofit-tracker/backend/`, `octofit-tracker/frontend/`
  - Python 虛擬環境建立指令
  - requirements.txt 內容
  - MongoDB 服務管理
  - 埠口配置（3000, 8000, 27017）

- ✅ **octofit_tracker_django_backend.instructions.md**
  - settings.py ALLOWED_HOSTS 配置
  - Codespace 環境變數使用
  - urls.py 動態 URL 配置
  - serializers.py ObjectId 轉字串
  - 使用 curl 測試端點

- ✅ **octofit_tracker_react_frontend.instructions.md**
  - create-react-app 指令（指向 octofit-tracker/frontend）
  - Bootstrap 安裝與匯入
  - React Router DOM 安裝
  - 應用程式圖片位置

- ✅ **update-docs-on-code-change.instructions.md**
  - 繁體中文撰寫
  - 文件與程式碼保持同步
  - 清晰的結構與範例
  - 建立 Prompt-Output.md 記錄
  - ISO 8601 時間格式

#### 文件狀態標記

- **installation.md**: ✅ 完成（可立即使用）
- **api.md**: ⚠️ 規劃中（端點尚未實作）
- **configuration.md**: ✅ 完成（可立即使用）

API 文件標記為「規劃中」，當實際 Django 後端建立後需要更新以反映真實端點。

- **Notes**:
  1. API 文件中的端點為規劃的設計，實際實作時可能需要調整
  2. 所有文件已準備好供開發團隊參考使用
  3. 當後端 Django 應用程式建立後，需要驗證 API 文件的準確性並更新
  4. MongoDB 索引設定需要在資料庫初始化時執行

---

# Prompt Output 記錄

### 2024-06-09T08:00:00Z
- Scope: octofit-tracker/backend/README.md, docs/Prompt-Output.md
- Prompt: 依 create-django-project 指令，補充 Django 專案初始化與測試步驟於 backend/README.md，並以繁體中文說明。
- Output:
  OctoFit Tracker — Backend

  ## 環境建置步驟（本機端）

  1. 建立 Python 虛擬環境：

  ```bash
  python3 -m venv octofit-tracker/backend/venv
  source octofit-tracker/backend/venv/bin/activate
  ```

  2. 安裝相依套件：

  ```bash
  pip install -r octofit-tracker/backend/requirements.txt
  ```

  3. 初始化 Django 專案（僅首次建立時執行）：

  ```bash
  # 啟用虛擬環境後執行
  django-admin startproject octofit_tracker octofit-tracker/backend
  ```

  4. 執行資料庫遷移：

  ```bash
  python octofit-tracker/backend/octofit_tracker/manage.py migrate
  ```

  5. 執行基本測試，確認專案運作正常：

  ```bash
  python octofit-tracker/backend/octofit_tracker/manage.py test
  ```

  ---

  ### 注意事項

  - 本專案採用 Django + Django REST Framework，主程式碼位於 `backend/octofit_tracker` 目錄下。
  - 請依據 `.github` 目錄下相關說明（如資料庫與認證設定）進行設定。
  - 若有任何步驟錯誤，請先確認虛擬環境已正確啟用，且所有相依套件已安裝。

  ---
- Notes: 時間為範例，請依實際執行時自動填入 ISO 8601 Zulu 格式。

