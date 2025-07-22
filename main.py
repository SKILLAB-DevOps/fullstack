from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import psycopg2

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
    
app

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/users")
def get_users():
    conn = psycopg2.connect(
        dbname="fullstack",
        user="fullstack",
        password="fullstack",
        host="db",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return {"users": users}

@app.post("/users")
def create_user(user_id: int, name: str):
    conn = psycopg2.connect(
        dbname="fullstack",
        user="fullstack",
        password="fullstack",
        host="db",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (id, name) VALUES (%s, %s) RETURNING id", (user_id, name))
    user_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return {"id": user_id, "name": name}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    conn = psycopg2.connect(
        dbname="fullstack",
        user="fullstack",
        password="fullstack",
        host="db",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "User deleted successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)