
## Step 1: Hello GitHub Copilot agent mode

#### Use Copilot agent mode to create a branch and publish it

1. 請建立並發布一個名為 build-octofit-app 的新 Git 分支。

## Step 2: The initial application setup

#### Prompt for GitHub Copilot in agent mode to start the creation of our application

2. 請根據OctoFit Tracker App structure 建立專案結構
3. 根據專案需求建立 Python的 requirements.txt
4. 建立 Python virtual environment並安裝 requirements.txt的內容

## Step 3: Initialize the octofit_db MongoDB database, and update Django project/app

#### Setup the Python Django project/app

運行 `.github/prompts/create-django-project.prompt.md`

```sh
source octofit-tracker/backend/venv/bin/activate && django-admin startproject octofit_tracker octofit-tracker/backend

cd octofit-tracker/backend && python manage.py migrate

# 運行 Django 測試來驗證專案是否正常
cd octofit-tracker/backend
python manage.py test
```

#### Initialize MongoDB


```sh
ps aux | grep mongod
service mongodb-org start

mkdir -p /tmp/mongodb && mongod --dbpath /tmp/mongodb --logpath /tmp/mongodb.log

sleep 2 && mongosh --eval "db.runCommand('ping')"

# 驗證 mongosh 連接是否正常：
mongosh --eval "print('Connected to MongoDB'); db.admin.command('ping')"

# MongoDB 沒有正常啟動，重新啟動並檢查詳細的錯誤信息：
rm -rf /tmp/mongodb && mkdir -p /tmp/mongodb && mongod --dbpath /tmp/mongodb --logpath /tmp/mongodb.log 2>&1 &

sleep 2 && ps aux | grep mongod | grep -v grep

# MongoDB 現在已在運行。讓我測試 mongosh 連接：
mongosh --eval "db.runCommand('ping')" 2>&1
```

#### Initialize, create, and populate the octofit_db MongoDB database

執行 `.github/prompts/init-populate-octofit_db.prompt.md`


```sh
cd /workse/octofit-tracker/backend && source venv/bin/activate && python manage.py makemigrations octofit_tracker && python manage.py migrate

cd /workspaces/skills_copilot-build-with-agent-mode/octofit-tracker/backend && source venv/bin/activate && python manage.py populate_db

mongosh --eval "use octofit_db; show collections; db.users.findOne(); db.teams.findOne(); db.activities.findOne(); db.leaderboards.findOne(); db.workouts.findOne(); db.users.getIndexes();"
```

#### Run Django test

```
cd /workspaces/skills_copilot-build-with-agent-mode/octofit-tracker/backend && source venv/bin/activate && python manage.py test
```

#### to update the Python Django project/app files

建立 `.github/prompts/update-octofit-tracker-app.prompt.md`

```md
* 所有 Django 專案檔案皆位於 `octofit-tracker/backend/octofit_tracker` 目錄中。

1. 更新 `settings.py`，以支援 MongoDB 連線與 CORS 設定。
2. 更新 `models.py`、`serializers.py`、`urls.py`、`views.py`、`tests.py` 以`admin.py` 及 tests，以支援 users、teams、activities、leaderboard 與 workouts 等集合（collections）。
3. 確保 `/` 路徑指向 API，且在 `urls.py` 中存在 `api_root`。

```

## Step 4: Setup Django REST Framework

#### Setup Django REST Framework and test the REST API endpoints

> 在 Github Codespace，具有`$CODESPACE_NAME`這個環境變數

```md
請為 Codespace 設定對應的 URL。
- 所有 Django 專案檔案皆位於 `octofit-tracker/backend/octofit_tracker` 目錄中。
- **僅**更新 `settings.py` 與 `urls.py` 中與 URL 相關的設定。
- REST API 端點格式為：
  `https://$CODESPACE_NAME-8000.app.github.dev/api/[component]/`
- 完整 URL 範例：
  `https://$CODESPACE_NAME-8000.app.github.dev/api/activities/`
- 請勿硬編碼 `$CODESPACE_NAME`，必須使用環境變數。
- 請勿更新 `views.py`。

1. 更新 `urls.py`，將 REST API URL 端點的回傳網址替換為使用環境變數 `$CODESPACE_NAME` 的
   `https://$CODESPACE_NAME-8000.app.github.dev`，以供 Django 使用，並避免 HTTPS 憑證問題。
2. 透過更新 `settings.py` 中的 `ALLOWED_HOSTS`，確保 Django 後端可同時在 Codespace URL（即 `$CODESPACE_NAME` 的值） 與 localhost正常運作。
```

請透過 VS Code 的 `launch.json` 啟動伺服器，並使用 `curl` 指令測試 API 端點。
- REST API 端點格式為：
  `https://$CODESPACE_NAME-8000.app.github.dev/api/[component]/`
- 完整 URL 範例：
  `https://$CODESPACE_NAME-8000.app.github.dev/api/activities/`
- 請勿硬編碼 `$CODESPACE_NAME`，必須使用環境變數。

```sh
# 需要確保虛擬環境已激活並且依賴項已安裝
cd /workspaces/skills_copilot-build-with-agent-mode/octofit-tracker/backend && source venv/bin/activate && pip list | grep -i django

# 進行資料庫遷移和啟動伺服器
cd /workspaces/skills_copilot-build-with-agent-mode/octofit-tracker/backend && source venv/bin/activate && python manage.py migrate

# 取得當前 CODESPACE_NAME
CODESPACE_NAME=$(echo ${CODESPACE_NAME:-localhost})
echo "Using CODESPACE_NAME: $CODESPACE_NAME"



# 測試 API 根路徑
curl -s https://$CODESPACE_NAME-8000.app.github.dev/api/ | jq .

# 測試個別端點
curl -s https://$CODESPACE_NAME-8000.app.github.dev/api/users/ | jq .
curl -s https://$CODESPACE_NAME-8000.app.github.dev/api/teams/ | jq .
curl -s https://$CODESPACE_NAME-8000.app.github.dev/api/activities/ | jq .
curl -s https://$CODESPACE_NAME-8000.app.github.dev/api/workouts/ | jq .
curl -s https://$CODESPACE_NAME-8000.app.github.dev/api/leaderboards/ | jq .
```



