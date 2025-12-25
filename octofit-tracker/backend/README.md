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
