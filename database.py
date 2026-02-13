import sqlite3

conn = sqlite3.connect("app.db", check_same_thread=False)
c = conn.cursor()

def create_tables():
    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        pin TEXT
    )
    """)
    c.execute("""
    CREATE TABLE IF NOT EXISTS history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        prompt TEXT
    )
    """)
    conn.commit()

def register_user(username, password, pin):
    c.execute("INSERT INTO users VALUES (NULL, ?, ?, ?)", (username, password, pin))
    conn.commit()

def login_user(username, password):
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    return c.fetchone()

def verify_pin(username, pin):
    c.execute("SELECT * FROM users WHERE username=? AND pin=?", (username, pin))
    return c.fetchone()

def save_prompt(username, prompt):
    c.execute("INSERT INTO history VALUES (NULL, ?, ?)", (username, prompt))
    conn.commit()

def get_history(username):
    c.execute("SELECT prompt FROM history WHERE username=?", (username,))
    return c.fetchall()
