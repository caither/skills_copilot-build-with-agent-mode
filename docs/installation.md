# OctoFit Tracker 安裝指南

本文件提供 OctoFit Tracker 應用程式的詳細安裝與設定說明。

## 目錄

- [使用 GitHub Codespaces（推薦）](#使用-github-codespaces推薦)
- [本機開發環境設定](#本機開發環境設定)
- [驗證安裝](#驗證安裝)
- [常見問題排解](#常見問題排解)

---

## 使用 GitHub Codespaces（推薦）

### 優點

- ✅ 預先配置完整的開發環境
- ✅ 自動安裝所有相依套件
- ✅ 內建 MongoDB 服務
- ✅ 無需本機安裝任何軟體
- ✅ 可在任何裝置上開發

### 步驟

1. **建立 Codespace**

   - 前往專案的 GitHub 頁面
   - 點擊綠色的 "Code" 按鈕
   - 選擇 "Codespaces" 標籤
   - 點擊 "Create codespace on build-octofit-app"

2. **等待環境初始化**

   Codespace 會自動執行：
   - 安裝 MongoDB 6.0
   - 安裝 Python 3 虛擬環境工具
   - 配置埠口可見性（3000, 8000 設為 public）
   - 啟動 MongoDB 服務

3. **檢查 MongoDB 狀態**

   ```bash
   ps aux | grep mongod
   ```

   應該會看到 mongod 正在運行。

4. **建立 Git 分支**（如尚未建立）

   ```bash
   git checkout -b build-octofit-app
   git push -u origin build-octofit-app
   ```

---

## 本機開發環境設定

### 前置需求

確保已安裝以下軟體：

| 軟體 | 版本 | 安裝連結 |
|------|------|----------|
| Python | 3.8+ | [python.org](https://www.python.org/downloads/) |
| Node.js | 16+ | [nodejs.org](https://nodejs.org/) |
| MongoDB | 6.0+ | [mongodb.com](https://www.mongodb.com/try/download/community) |
| Git | 最新版 | [git-scm.com](https://git-scm.com/) |

### 安裝步驟

#### 1. 複製專案

```bash
git clone https://github.com/YOUR_USERNAME/skills_copilot-build-with-agent-mode.git
cd skills_copilot-build-with-agent-mode
git checkout -b build-octofit-app
```

#### 2. 建立專案結構

```bash
mkdir -p octofit-tracker/backend
mkdir -p octofit-tracker/frontend
```

#### 3. 設定後端

**建立 Python 虛擬環境**

```bash
python3 -m venv octofit-tracker/backend/venv
```

**啟動虛擬環境**

```bash
# macOS/Linux
source octofit-tracker/backend/venv/bin/activate

# Windows
octofit-tracker\backend\venv\Scripts\activate
```

**建立 requirements.txt**

在 `octofit-tracker/backend/requirements.txt` 建立檔案並加入以下內容：

```txt
Django==4.1.7
djangorestframework==3.14.0
django-allauth==0.51.0
django-cors-headers==4.5.0
dj-rest-auth==2.2.6
djongo==1.3.6
pymongo==3.12
sqlparse==0.2.4
```

**安裝 Python 套件**

```bash
pip install -r octofit-tracker/backend/requirements.txt
```

**初始化 Django 專案**

```bash
cd octofit-tracker/backend
django-admin startproject octofit_tracker .
```

**設定 Django settings.py**

編輯 `octofit_tracker/settings.py`，新增：

```python
import os

# ALLOWED_HOSTS 設定
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
if os.environ.get('CODESPACE_NAME'):
    ALLOWED_HOSTS.append(f"{os.environ.get('CODESPACE_NAME')}-8000.app.github.dev")

# 資料庫設定
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'HOST': 'localhost',
        'PORT': 27017,
    }
}

# CORS 設定
INSTALLED_APPS = [
    # ... 其他應用程式
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # ... 其他中介軟體
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

if os.environ.get('CODESPACE_NAME'):
    CORS_ALLOWED_ORIGINS.append(
        f"https://{os.environ.get('CODESPACE_NAME')}-3000.app.github.dev"
    )
```

**執行資料庫遷移**

```bash
python manage.py migrate
```

**建立超級使用者**

```bash
python manage.py createsuperuser
```

#### 4. 設定前端

**建立 React 應用程式**

```bash
cd ../..  # 回到專案根目錄
npx create-react-app octofit-tracker/frontend --template cra-template --use-npm
```

**安裝相依套件**

```bash
npm install bootstrap --prefix octofit-tracker/frontend
npm install react-router-dom --prefix octofit-tracker/frontend
```

**匯入 Bootstrap CSS**

編輯 `octofit-tracker/frontend/src/index.js`，在檔案最頂端加入：

```javascript
import 'bootstrap/dist/css/bootstrap.min.css';
```

#### 5. 啟動 MongoDB

**macOS (使用 Homebrew)**

```bash
brew services start mongodb-community
```

**Ubuntu/Debian**

```bash
sudo systemctl start mongod
sudo systemctl enable mongod
```

**Windows**

```bash
net start MongoDB
```

**手動啟動**

```bash
mongod --dbpath /data/db
```

---

## 驗證安裝

### 1. 啟動後端伺服器

```bash
cd octofit-tracker/backend
source venv/bin/activate  # Windows: venv\Scripts\activate
python manage.py runserver 0.0.0.0:8000
```

訪問：
- API Root: http://localhost:8000/api/
- Admin Panel: http://localhost:8000/admin/

### 2. 啟動前端伺服器

開啟新終端：

```bash
npm start --prefix octofit-tracker/frontend
```

訪問：
- React App: http://localhost:3000

### 3. 檢查 MongoDB 連線

```bash
mongosh
> use octofit_db
> show collections
> exit
```

---

## 常見問題排解

### MongoDB 無法啟動

**問題**：`mongod: command not found`

**解決**：
- 確認 MongoDB 已正確安裝
- 檢查 PATH 環境變數
- 重新安裝 MongoDB

```bash
# Ubuntu
sudo apt-get update
sudo apt-get install -y mongodb-org

# macOS
brew install mongodb-community
```

### Django 資料庫錯誤

**問題**：`django.db.utils.ConnectionError: could not connect to MongoDB`

**解決**：
1. 確認 MongoDB 正在運行：`ps aux | grep mongod`
2. 檢查連線設定：確認 `settings.py` 中的 `DATABASES` 配置
3. 測試連線：`mongosh --eval "db.version()"`

### React 無法連接到後端

**問題**：CORS 錯誤或 API 請求失敗

**解決**：
1. 確認後端伺服器正在運行
2. 檢查 `settings.py` 中的 `CORS_ALLOWED_ORIGINS`
3. 確認前端 API URL 正確

### Python 虛擬環境問題

**問題**：`pip: command not found` 或套件安裝失敗

**解決**：
```bash
# 重新建立虛擬環境
rm -rf octofit-tracker/backend/venv
python3 -m venv octofit-tracker/backend/venv
source octofit-tracker/backend/venv/bin/activate
pip install --upgrade pip
pip install -r octofit-tracker/backend/requirements.txt
```

---

## 下一步

安裝完成後，請參考：

- [API 文件](api.md) - 了解可用的 REST API 端點
- [設定說明](configuration.md) - 進階設定選項
- [README.md](../README.md) - 專案概述與快速開始

---

**更新日期**: 2025-12-24
