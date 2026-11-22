from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    conn = sqlite3.connect("database/machine_data.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT machine_id, temperature, timestamp
        FROM machine_data
        ORDER BY id DESC
        LIMIT 10
    """)

    records = cursor.fetchall()
    conn.close()

    return render_template("index.html", records=records)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
