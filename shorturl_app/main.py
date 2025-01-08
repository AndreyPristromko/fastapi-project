from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import shortuuid

app = FastAPI()

# Database setup
conn = sqlite3.connect("shorturl.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS urls (
    id TEXT PRIMARY KEY,
    full_url TEXT NOT NULL,
    clicks INTEGER DEFAULT 0
)
""")
conn.commit()

# Models
class URLRequest(BaseModel):
    url: str

# Endpoints
@app.post("/shorten")
def shorten_url(request: URLRequest):
    short_id = shortuuid.ShortUUID().random(length=6)
    cursor.execute(
        "INSERT INTO urls (id, full_url) VALUES (?, ?)",
        (short_id, request.url)
    )
    conn.commit()
    return {"short_id": short_id, "full_url": request.url}

@app.get("/{short_id}")
def redirect_to_url(short_id: str):
    cursor.execute("SELECT full_url FROM urls WHERE id = ?", (short_id,))
    row = cursor.fetchone()
    if row:
        cursor.execute("UPDATE urls SET clicks = clicks + 1 WHERE id = ?", (short_id,))
        conn.commit()
        return {"redirect_to": row[0]}
    raise HTTPException(status_code=404, detail="URL not found")

@app.get("/stats/{short_id}")
def get_url_stats(short_id: str):
    cursor.execute("SELECT full_url, clicks FROM urls WHERE id = ?", (short_id,))
    row = cursor.fetchone()
    if row:
        return {"full_url": row[0], "clicks": row[1]}
    raise HTTPException(status_code=404, detail="URL not found")
