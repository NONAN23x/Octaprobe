import sqlite3

def conect_db():
    conn = sqlite3.connect("assets/data/octaprobe.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            project TEXT NOT NULL,
            data TEXT NOT NULL
        )
    """)
    
    conn.commit()