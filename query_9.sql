SELECT Subjects.name
FROM Grades
INNER JOIN Subjects ON Grades.subject_id = Subjects.id
INNER JOIN Students ON Grades.student_id = Students.id
WHERE Students.name = '<student_name>';
