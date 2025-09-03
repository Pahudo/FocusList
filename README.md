# FocusList

Simple task API (CRUD) to practice back-end with FastAPI + SQLite with the help of ChatGPT

## 🚀 How to Run
```bash
python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Docs: http://127.0.0.1:8000/docs

## 📦 Stack

FastAPI • Uvicorn • SQLAlchemy • SQLite

## 🔗 Endpoints

GET /tasks — list tasks

POST /tasks — create tasks (title, description)

GET /tasks/{id} — find tasks by id

PUT /tasks/{id} — update tasks (title, description, done)

DELETE /tasks/{id} — delete tasks

## 🗂️ Structure

```app/
  main.py
  models.py
  database.py
  routes.py
requirements.txt
```

## 🛣️ Nexts Steps

Authentication (JWT)

Fields created_at/updated_at

pagination and filters

Deploy (Render/Railway)
