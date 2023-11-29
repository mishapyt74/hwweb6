from faker import Faker
import sqlite3
import random
import datetime

fake = Faker()
SELECT student_id, AVG(grade) as avg_grade
FROM Grades
GROUP BY student_id
ORDER BY avg_grade DESC
LIMIT 5;

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE Students (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    group_id INTEGER)''')

cursor.execute('''CREATE TABLE Groups (
                    id INTEGER PRIMARY KEY,
                    name TEXT)''')

cursor.execute('''CREATE TABLE Professors (
                    id INTEGER PRIMARY KEY,
                    name TEXT)''')

cursor.execute('''CREATE TABLE Subjects (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    professor_id INTEGER)''')

cursor.execute('''CREATE TABLE Grades (
                    id INTEGER PRIMARY KEY,
                    student_id INTEGER,
                    subject_id INTEGER,
                    grade INTEGER,
                    date TEXT,
                    FOREIGN KEY (student_id) REFERENCES Students(id),
                    FOREIGN KEY (subject_id) REFERENCES Subjects(id))''')

for _ in range(30):
    cursor.execute("INSERT INTO Students (name, group_id) VALUES (?, ?)", (fake.name(), random.randint(1, 3)))

for group_name in ['Group A', 'Group B', 'Group C']:
    cursor.execute("INSERT INTO Groups (name) VALUES (?)", (group_name,))

for _ in range(3):
    cursor.execute("INSERT INTO Professors (name) VALUES (?)", (fake.name(),))

subjects = ['Mathematics', 'Physics', 'Biology', 'Chemistry', 'History', 'Literature', 'Computer Science']
for subject in subjects:
    cursor.execute("INSERT INTO Subjects (name, professor_id) VALUES (?, ?)", (subject, random.randint(1, 3)))

for student_id in range(1, 31):
    for subject_id in range(1, 8):
        grade = random.randint(60, 100)
        date = fake.date_between(start_date='-1y', end_date='today')
        cursor.execute("INSERT INTO Grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)",
                       (student_id, subject_id, grade, date))

conn.commit()
conn.close()
