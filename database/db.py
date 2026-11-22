import sqlite3

conn = sqlite3.connect("database/machine_data.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS machine_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    machine_id TEXT,
    temperature REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Database and Table Created Successfully!")
