# logic/database.py
import sqlite3
import os

def save_record(plate, area, expiry, sticker_type):
    db_path = "data/stickers.db"
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS stickers (
        plate TEXT, area TEXT, expiry TEXT, type TEXT
    )""")
    cur.execute("INSERT INTO stickers VALUES (?, ?, ?, ?)",
                (plate, area, expiry, sticker_type))
    conn.commit()
    conn.close()