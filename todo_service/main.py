from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Database setup
conn = sqlite3.connect("todo.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    completed BOOLEAN NOT NULL DEFAULT 0
)
""")
conn.commit()

# Models
class Task(BaseModel):
    title: str
    description: str = None
    completed: bool = False

# Endpoints
@app.post("/items")
def create_task(task: Task):
    cursor.execute(
        "INSERT INTO tasks (title, description, completed) VALUES (?, ?, ?)",
        (task.title, task.description, task.completed)
    )
    conn.commit()
    return {"id": cursor.lastrowid, "title": task.title, "description": task.description, "completed": task.completed}

@app.get("/items")
def read_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return tasks

@app.get("/items/{item_id}")
def read_task(item_id: int):
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (item_id,))
    task = cursor.fetchone()
    if task:
        return task
    return {"error": "Task not found"}

@app.put("/items/{item_id}")
def update_task(item_id: int, task: Task):
    cursor.execute(
        "UPDATE tasks SET title = ?, description = ?, completed = ? WHERE id = ?",
        (task.title, task.description, task.completed, item_id)
    )
    conn.commit()
    return {"message": "Task updated successfully"}

@app.delete("/items/{item_id}")
def delete_task(item_id: int):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (item_id,))
    conn.commit()
    return {"message": "Task deleted successfully"}
