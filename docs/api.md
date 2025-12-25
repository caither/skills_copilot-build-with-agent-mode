# OctoFit Tracker API 文件

本文件說明 OctoFit Tracker REST API 的所有端點、請求格式與回應範例。

> **注意**：本 API 文件將隨著專案開發持續更新。目前列出的是規劃中的端點。

---

## 目錄

- [認證](#認證)
- [使用者管理](#使用者管理)
- [活動追蹤](#活動追蹤)
- [團隊管理](#團隊管理)
- [排行榜](#排行榜)
- [訓練建議](#訓練建議)
- [錯誤處理](#錯誤處理)

---

## 基礎資訊

### Base URL

- **開發環境（Codespaces）**: `https://{CODESPACE_NAME}-8000.app.github.dev/api/`
- **本機環境**: `http://localhost:8000/api/`

### 認證方式

API 使用 Token 認證。在請求標頭中包含：

```
Authorization: Token YOUR_AUTH_TOKEN
```

### 通用回應格式

**成功回應**：
```json
{
  "success": true,
  "data": { ... },
  "message": "操作成功"
}
```

**錯誤回應**：
```json
{
  "success": false,
  "error": "錯誤訊息",
  "code": "ERROR_CODE"
}
```

---

## 認證

### 註冊新使用者

**端點**: `POST /api/auth/register/`

**請求**：
```json
{
  "username": "student001",
  "email": "student001@school.edu",
  "password": "SecurePass123!",
  "first_name": "John",
  "last_name": "Doe",
  "grade": 10
}
```

**回應**：
```json
{
  "success": true,
  "data": {
    "user": {
      "id": "507f1f77bcf86cd799439011",
      "username": "student001",
      "email": "student001@school.edu",
      "first_name": "John",
      "last_name": "Doe"
    },
    "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
  },
  "message": "註冊成功"
}
```

**狀態碼**：
- 201: 註冊成功
- 400: 資料格式錯誤或使用者名稱已存在

---

### 登入

**端點**: `POST /api/auth/login/`

**請求**：
```json
{
  "username": "student001",
  "password": "SecurePass123!"
}
```

**回應**：
```json
{
  "success": true,
  "data": {
    "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b",
    "user": {
      "id": "507f1f77bcf86cd799439011",
      "username": "student001",
      "email": "student001@school.edu"
    }
  },
  "message": "登入成功"
}
```

**狀態碼**：
- 200: 登入成功
- 401: 帳號或密碼錯誤

---

### 登出

**端點**: `POST /api/auth/logout/`

**標頭**：需要認證

**回應**：
```json
{
  "success": true,
  "message": "登出成功"
}
```

**狀態碼**：
- 200: 登出成功
- 401: 未認證

---

## 使用者管理

### 取得個人資料

**端點**: `GET /api/users/profile/`

**標頭**：需要認證

**回應**：
```json
{
  "success": true,
  "data": {
    "id": "507f1f77bcf86cd799439011",
    "username": "student001",
    "email": "student001@school.edu",
    "first_name": "John",
    "last_name": "Doe",
    "grade": 10,
    "avatar": "https://example.com/avatars/student001.jpg",
    "total_points": 1250,
    "level": 5,
    "activities_count": 45,
    "joined_date": "2025-01-15T08:30:00Z"
  }
}
```

**狀態碼**：
- 200: 成功
- 401: 未認證

---

### 更新個人資料

**端點**: `PATCH /api/users/profile/`

**標頭**：需要認證

**請求**：
```json
{
  "first_name": "Johnny",
  "avatar": "data:image/png;base64,..."
}
```

**回應**：
```json
{
  "success": true,
  "data": {
    "id": "507f1f77bcf86cd799439011",
    "first_name": "Johnny",
    "avatar": "https://example.com/avatars/student001_new.jpg"
  },
  "message": "個人資料已更新"
}
```

**狀態碼**：
- 200: 更新成功
- 400: 資料格式錯誤
- 401: 未認證

---

## 活動追蹤

### 記錄新活動

**端點**: `POST /api/activities/`

**標頭**：需要認證

**請求**：
```json
{
  "activity_type": "running",
  "duration_minutes": 30,
  "distance_km": 5.2,
  "calories": 350,
  "date": "2025-12-24T06:30:00Z",
  "notes": "晨跑，天氣很好"
}
```

**活動類型**：
- `running` - 跑步
- `walking` - 走路
- `cycling` - 騎自行車
- `strength` - 力量訓練
- `yoga` - 瑜珈
- `other` - 其他

**回應**：
```json
{
  "success": true,
  "data": {
    "id": "507f1f77bcf86cd799439012",
    "activity_type": "running",
    "duration_minutes": 30,
    "distance_km": 5.2,
    "calories": 350,
    "points_earned": 52,
    "date": "2025-12-24T06:30:00Z",
    "created_at": "2025-12-24T06:45:00Z"
  },
  "message": "活動記錄成功！獲得 52 點"
}
```

**狀態碼**：
- 201: 記錄成功
- 400: 資料格式錯誤
- 401: 未認證

---

### 取得活動歷史

**端點**: `GET /api/activities/`

**標頭**：需要認證

**查詢參數**：
- `page` (int, optional): 頁碼，預設 1
- `limit` (int, optional): 每頁筆數，預設 20
- `type` (string, optional): 活動類型篩選
- `start_date` (string, optional): 開始日期 (ISO 8601)
- `end_date` (string, optional): 結束日期 (ISO 8601)

**範例請求**：
```
GET /api/activities/?page=1&limit=10&type=running&start_date=2025-12-01T00:00:00Z
```

**回應**：
```json
{
  "success": true,
  "data": {
    "activities": [
      {
        "id": "507f1f77bcf86cd799439012",
        "activity_type": "running",
        "duration_minutes": 30,
        "distance_km": 5.2,
        "calories": 350,
        "points_earned": 52,
        "date": "2025-12-24T06:30:00Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 10,
      "total": 45,
      "pages": 5
    }
  }
}
```

**狀態碼**：
- 200: 成功
- 401: 未認證

---

### 取得活動統計

**端點**: `GET /api/activities/stats/`

**標頭**：需要認證

**查詢參數**：
- `period` (string): `week`, `month`, `year`, `all`

**回應**：
```json
{
  "success": true,
  "data": {
    "period": "month",
    "total_activities": 15,
    "total_duration_minutes": 450,
    "total_distance_km": 78.5,
    "total_calories": 5250,
    "total_points": 785,
    "by_type": {
      "running": {
        "count": 10,
        "duration_minutes": 300,
        "distance_km": 52.0
      },
      "walking": {
        "count": 5,
        "duration_minutes": 150,
        "distance_km": 26.5
      }
    }
  }
}
```

**狀態碼**：
- 200: 成功
- 401: 未認證

---

## 團隊管理

### 建立團隊

**端點**: `POST /api/teams/`

**標頭**：需要認證

**請求**：
```json
{
  "name": "晨跑勇士",
  "description": "每天早上一起跑步的團隊",
  "avatar": "https://example.com/team-avatar.jpg"
}
```

**回應**：
```json
{
  "success": true,
  "data": {
    "id": "507f1f77bcf86cd799439013",
    "name": "晨跑勇士",
    "description": "每天早上一起跑步的團隊",
    "creator": "student001",
    "members_count": 1,
    "total_points": 0,
    "created_at": "2025-12-24T07:00:00Z"
  },
  "message": "團隊建立成功"
}
```

**狀態碼**：
- 201: 建立成功
- 400: 資料格式錯誤
- 401: 未認證

---

### 加入團隊

**端點**: `POST /api/teams/{team_id}/join/`

**標頭**：需要認證

**回應**：
```json
{
  "success": true,
  "data": {
    "team_id": "507f1f77bcf86cd799439013",
    "team_name": "晨跑勇士",
    "joined_at": "2025-12-24T07:05:00Z"
  },
  "message": "成功加入團隊"
}
```

**狀態碼**：
- 200: 加入成功
- 400: 已是團隊成員或團隊已滿
- 404: 團隊不存在
- 401: 未認證

---

### 取得團隊列表

**端點**: `GET /api/teams/`

**標頭**：需要認證

**回應**：
```json
{
  "success": true,
  "data": {
    "teams": [
      {
        "id": "507f1f77bcf86cd799439013",
        "name": "晨跑勇士",
        "members_count": 12,
        "total_points": 5420,
        "rank": 3
      }
    ]
  }
}
```

**狀態碼**：
- 200: 成功
- 401: 未認證

---

## 排行榜

### 取得個人排行榜

**端點**: `GET /api/leaderboard/users/`

**標頭**：需要認證

**查詢參數**：
- `period` (string): `week`, `month`, `all`
- `limit` (int, optional): 顯示筆數，預設 50

**回應**：
```json
{
  "success": true,
  "data": {
    "period": "month",
    "leaderboard": [
      {
        "rank": 1,
        "user": {
          "id": "507f1f77bcf86cd799439011",
          "username": "student001",
          "avatar": "https://example.com/avatar.jpg"
        },
        "points": 1250,
        "activities_count": 45
      }
    ],
    "current_user_rank": 5
  }
}
```

**狀態碼**：
- 200: 成功
- 401: 未認證

---

### 取得團隊排行榜

**端點**: `GET /api/leaderboard/teams/`

**標頭**：需要認證

**回應**：
```json
{
  "success": true,
  "data": {
    "period": "month",
    "leaderboard": [
      {
        "rank": 1,
        "team": {
          "id": "507f1f77bcf86cd799439013",
          "name": "晨跑勇士"
        },
        "total_points": 5420,
        "members_count": 12,
        "avg_points_per_member": 451.67
      }
    ]
  }
}
```

**狀態碼**：
- 200: 成功
- 401: 未認證

---

## 訓練建議

### 取得個人化訓練建議

**端點**: `GET /api/recommendations/`

**標頭**：需要認證

**回應**：
```json
{
  "success": true,
  "data": {
    "recommendations": [
      {
        "type": "workout",
        "title": "增加耐力訓練",
        "description": "根據你的活動記錄，建議增加長距離慢跑",
        "suggested_activity": {
          "type": "running",
          "duration_minutes": 40,
          "intensity": "moderate"
        }
      }
    ],
    "next_challenge": {
      "title": "月度挑戰：100公里",
      "progress": 78.5,
      "target": 100.0,
      "days_remaining": 7
    }
  }
}
```

**狀態碼**：
- 200: 成功
- 401: 未認證

---

## 錯誤處理

### HTTP 狀態碼

| 狀態碼 | 說明 |
|--------|------|
| 200 | 請求成功 |
| 201 | 資源建立成功 |
| 400 | 錯誤的請求（參數錯誤、格式不正確） |
| 401 | 未認證（缺少 token 或 token 無效） |
| 403 | 無權限（已認證但無存取權限） |
| 404 | 資源不存在 |
| 500 | 伺服器內部錯誤 |

### 錯誤碼

| 錯誤碼 | 說明 |
|--------|------|
| `AUTH_REQUIRED` | 需要認證 |
| `INVALID_CREDENTIALS` | 帳號或密碼錯誤 |
| `USER_EXISTS` | 使用者名稱或信箱已存在 |
| `INVALID_DATA` | 資料格式錯誤 |
| `NOT_FOUND` | 資源不存在 |
| `PERMISSION_DENIED` | 權限不足 |
| `TEAM_FULL` | 團隊已滿 |

### 錯誤回應範例

```json
{
  "success": false,
  "error": "提供的認證資訊無效",
  "code": "INVALID_CREDENTIALS",
  "details": {
    "field": "password",
    "message": "密碼錯誤"
  }
}
```

---

## 測試 API

### 使用 curl

```bash
# 註冊新使用者
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "TestPass123!",
    "first_name": "Test",
    "last_name": "User",
    "grade": 10
  }'

# 登入
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "TestPass123!"
  }'

# 記錄活動（需要 token）
curl -X POST http://localhost:8000/api/activities/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -d '{
    "activity_type": "running",
    "duration_minutes": 30,
    "distance_km": 5.0,
    "calories": 350,
    "date": "2025-12-24T06:30:00Z"
  }'
```

---

## 版本歷史

| 版本 | 日期 | 變更 |
|------|------|------|
| 1.0 | 2025-12-24 | 初始 API 規格 |

---

**更新日期**: 2025-12-24
**API 版本**: 1.0
**狀態**: 規劃中
