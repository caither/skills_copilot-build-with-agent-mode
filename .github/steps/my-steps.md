
#### Use Copilot agent mode to create a branch and publish it

1. 請建立並發布一個名為 build-octofit-app 的新 Git 分支。

#### Prompt for GitHub Copilot in agent mode to start the creation of our application

2. 請根據OctoFit Tracker App structure 建立專案結構
3. 根據專案需求建立 Python的 requirements.txt
4. 建立 Python virtual environment並安裝 requirements.txt的內容

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

```sh
cd /workse/octofit-tracker/backend && source venv/bin/activate && python manage.py makemigrations octofit_tracker && python manage.py migrate

cd /workspaces/skills_copilot-build-with-agent-mode/octofit-tracker/backend && source venv/bin/activate && python manage.py populate_db

mongosh --eval "use octofit_db; show collections; db.users.findOne(); db.teams.findOne(); db.activities.findOne(); db.leaderboards.findOne(); db.workouts.findOne(); db.users.getIndexes();"
```
