from faker import Faker
import sqlite3
import random

fake = Faker()

conn = sqlite3.connect('../university.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    group_id INTEGER
                    )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS groups (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT
                    )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS teachers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT
                    )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS subjects (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    teacher_id INTEGER
                    )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS grades (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER,
                    subject_id INTEGER,
                    grade INTEGER,
                    FOREIGN KEY (student_id) REFERENCES students(id),
                    FOREIGN KEY (subject_id) REFERENCES subjects(id)
                    )''')

for _ in range(30):
    cursor.execute("INSERT INTO students (name, group_id) VALUES (?, ?)", (fake.name(), random.randint(1, 3)))

for i in range(3):
    cursor.execute("INSERT INTO groups (name) VALUES (?)", (f"Group {i+1}",))

for _ in range(3):
    cursor.execute("INSERT INTO teachers (name) VALUES (?)", (fake.name(),))

subjects = ["Mathematics", "Physics", "Biology", "Chemistry", "History", "Literature", "Geography", "Programming"]

for subject in subjects:
    cursor.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (subject, random.randint(1, 3)))

for student_id in range(1, 31):
    for subject_id in range(1, 9):
        cursor.execute("INSERT INTO grades (student_id, subject_id, grade) VALUES (?, ?, ?)",
                       (student_id, subject_id, random.randint(1, 20)))

conn.commit()
conn.close()
