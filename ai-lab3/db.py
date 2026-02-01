import sqlite3
import csv
import os


def get_connection():
    return sqlite3.connect("attendance.db")

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS attendance (
        student_name TEXT,
        subject TEXT,
        branch TEXT,
        month TEXT,
        attendance_percentage INTEGER
    )
    """)

    cur.execute("DELETE FROM attendance")

    with open("data.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = [
            (
                r["student_name"],
                r["subject"],
                r["branch"],
                r["month"],
                int(r["attendance_percentage"])
            )
            for r in reader
        ]

    cur.executemany(
        "INSERT INTO attendance VALUES (?, ?, ?, ?, ?)",
        rows
    )

    conn.commit()
    conn.close()

def run_query(sql: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    return rows
