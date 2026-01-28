import sqlite3
from datetime import datetime

def init_db(db_file):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS scans (
            timestamp TEXT,
            ip TEXT,
            latency REAL,
            ports TEXT
        )
    """)

    conn.commit()
    conn.close()

def save_result(db_file, ip, latency, ports):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    c.execute(
        "INSERT INTO scans VALUES (?, ?, ?, ?)",
        (datetime.now(), ip, latency, ",".join(map(str, ports)))
    )

    conn.commit()
    conn.close()

