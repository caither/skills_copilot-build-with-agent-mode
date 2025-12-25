# OctoFit Tracker 設定說明

本文件說明 OctoFit Tracker 應用程式的各項設定選項與環境變數。

---

## 目錄

- [環境變數](#環境變數)
- [Django 後端設定](#django-後端設定)
- [React 前端設定](#react-前端設定)
- [MongoDB 設定](#mongodb-設定)
- [開發環境設定](#開發環境設定)

---

## 環境變數

### 後端環境變數

在 `octofit-tracker/backend/.env` 檔案中設定：

```bash
# Django 設定
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# 資料庫設定
DB_NAME=octofit_db
DB_HOST=localhost
DB_PORT=27017

# CORS 設定
CORS_ALLOWED_ORIGINS=http://localhost:3000

# Codespace 設定（自動偵測）
CODESPACE_NAME=auto-detect
```

### 前端環境變數

在 `octofit-tracker/frontend/.env` 檔案中設定：

```bash
# API 端點
REACT_APP_API_URL=http://localhost:8000/api

# Codespace 環境（自動偵測）
REACT_APP_CODESPACE_NAME=auto-detect
```

---

## Django 後端設定

### settings.py 核心設定

#### 1. ALLOWED_HOSTS

自動偵測 Codespace 環境並動態配置：

```python
import os

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Codespace 環境自動配置
if os.environ.get('CODESPACE_NAME'):
    ALLOWED_HOSTS.append(
        f"{os.environ.get('CODESPACE_NAME')}-8000.app.github.dev"
    )
```

#### 2. 資料庫設定

使用 Djongo 連接 MongoDB：

```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': os.environ.get('DB_NAME', 'octofit_db'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': int(os.environ.get('DB_PORT', 27017)),
        'CLIENT': {
            'host': os.environ.get('DB_HOST', 'localhost'),
            'port': int(os.environ.get('DB_PORT', 27017)),
        }
    }
}
```

#### 3. CORS 設定

允許前端跨域請求：

```python
INSTALLED_APPS = [
    # Django 內建應用程式
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 第三方應用程式
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'django_allauth',
    'django_allauth.account',
    'dj_rest_auth',
    'dj_rest_auth.registration',

    # 自訂應用程式
    'api',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # 必須在 CommonMiddleware 之前
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS 設定
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

if os.environ.get('CODESPACE_NAME'):
    CORS_ALLOWED_ORIGINS.append(
        f"https://{os.environ.get('CODESPACE_NAME')}-3000.app.github.dev"
    )

CORS_ALLOW_CREDENTIALS = True
```

#### 4. REST Framework 設定

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}
```

#### 5. 認證設定

```python
# Django Allauth 設定
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

# Email 設定（開發環境）
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# 帳號設定
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_VERIFICATION = 'optional'
```

---

## React 前端設定

### package.json 設定

```json
{
  "name": "octofit-tracker-frontend",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.20.0",
    "bootstrap": "^5.3.2",
    "axios": "^1.6.2"
  },
  "proxy": "http://localhost:8000",
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }
}
```

### API 連線設定

在 `src/config.js` 建立 API 配置：

```javascript
const getApiUrl = () => {
  const codespace = process.env.REACT_APP_CODESPACE_NAME;

  if (codespace && codespace !== 'auto-detect') {
    return `https://${codespace}-8000.app.github.dev/api`;
  }

  // 自動偵測 Codespace
  const hostname = window.location.hostname;
  if (hostname.includes('app.github.dev')) {
    const codespaceName = hostname.split('-')[0];
    return `https://${codespaceName}-8000.app.github.dev/api`;
  }

  // 本機開發環境
  return process.env.REACT_APP_API_URL || 'http://localhost:8000/api';
};

export const API_BASE_URL = getApiUrl();
export const API_TIMEOUT = 10000; // 10 秒

export default {
  API_BASE_URL,
  API_TIMEOUT,
};
```

---

## MongoDB 設定

### 基本設定

**資料庫名稱**: `octofit_db`

**連線設定** (本機開發):
```
mongodb://localhost:27017/octofit_db
```

### 建議的集合 (Collections)

```javascript
// 使用者
db.createCollection("users")

// 活動記錄
db.createCollection("activities")

// 團隊
db.createCollection("teams")

// 排行榜快取
db.createCollection("leaderboards")
```

### 索引設定

```javascript
// 使用者索引
db.users.createIndex({ "username": 1 }, { unique: true })
db.users.createIndex({ "email": 1 }, { unique: true })

// 活動索引
db.activities.createIndex({ "user_id": 1, "date": -1 })
db.activities.createIndex({ "activity_type": 1 })
db.activities.createIndex({ "date": -1 })

// 團隊索引
db.teams.createIndex({ "name": 1 }, { unique: true })
db.teams.createIndex({ "total_points": -1 })
```

### 效能調校

```javascript
// 設定連線池大小
mongod --maxConns=200

// 設定記憶體使用
mongod --wiredTigerCacheSizeGB=1
```

---

## 開發環境設定

### GitHub Codespaces

#### devcontainer.json

```json
{
  "name": "OctoFit Tracker App codespace",
  "image": "mcr.microsoft.com/devcontainers/base:jammy",
  "features": {
    "ghcr.io/devcontainers/features/docker-in-docker:2": {},
    "ghcr.io/devcontainers/features/github-cli:1": {},
    "ghcr.io/devcontainers/features/node:1": {
      "version": "lts"
    }
  },
  "forwardPorts": [3000, 8000, 27017],
  "portAttributes": {
    "3000": {
      "label": "octofit-tracker",
      "requireLocalPort": true
    },
    "8000": {
      "label": "octofit-api",
      "requireLocalPort": true
    }
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "github.copilot",
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-python.debugpy"
      ],
      "settings": {
        "chat.agent.enabled": true
      }
    }
  }
}
```

#### 埠口可見性

Codespace 自動配置埠口可見性：

- **3000**: Public (React 前端)
- **8000**: Public (Django API)
- **27017**: Private (MongoDB)

### VS Code 設定

#### .vscode/settings.json

```json
{
  "python.defaultInterpreterPath": "octofit-tracker/backend/venv/bin/python",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "[python]": {
    "editor.defaultFormatter": "ms-python.python",
    "editor.tabSize": 4
  },
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.tabSize": 2
  }
}
```

#### .vscode/launch.json

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Django: runserver",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/octofit-tracker/backend/manage.py",
      "args": ["runserver", "0.0.0.0:8000"],
      "django": true,
      "justMyCode": false
    },
    {
      "name": "React: start",
      "type": "node",
      "request": "launch",
      "cwd": "${workspaceFolder}/octofit-tracker/frontend",
      "runtimeExecutable": "npm",
      "runtimeArgs": ["start"]
    }
  ]
}
```

---

## 安全性設定

### 生產環境建議

```python
# settings.py (生產環境)

# 安全性設定
DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')  # 從環境變數讀取

# HTTPS 設定
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# HSTS 設定
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

### 密碼政策

```python
# settings.py

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
```

---

## 日誌設定

```python
# settings.py

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'octofit_tracker.log',
            'formatter': 'verbose',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'octofit_tracker': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
```

---

## 效能設定

### 快取設定

```python
# settings.py

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'octofit-cache',
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}

# 排行榜快取時間（秒）
LEADERBOARD_CACHE_TIMEOUT = 300  # 5 分鐘
```

### 資料庫連線池

```python
# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'CLIENT': {
            'host': 'localhost',
            'port': 27017,
            'maxPoolSize': 50,
            'minPoolSize': 10,
        }
    }
}
```

---

**更新日期**: 2025-12-24
