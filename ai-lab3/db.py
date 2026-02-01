import sqlite3


def get_connection():
    return sqlite3.connect("attendance.db")

def run_query(sql: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    return rows

#One time function to create and seed the database
def seed_data():
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

    data = [
        ("Amit", "Maths", "CSE", "Jan", 100),
        ("Amit", "Physics", "CSE", "Jan", 90),
        ("Riya", "Physics", "CSE", "Jan", 45),
        ("Suresh", "Maths", "ECE", "Jan", 80),
        ("Suresh", "Maths", "ECE", "Feb", 70),
        ("Neha", "Maths", "ECE", "Jan", 60),
        ("Neha", "Physics", "ECE", "Jan", 40),
        ("Amit", "Chemistry", "CSE", "Feb", 95),
        ("Riya", "Physics", "CSE", "Feb", 85),
    ]

    cur.executemany("INSERT INTO attendance VALUES (?, ?, ?, ?, ?)", data)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    seed_data()
