SELECT Students.group_id, AVG(Grades.grade) as avg_grade
FROM Grades
INNER JOIN Students ON Grades.student_id = Students.id
WHERE subject_id = <subject_id>
GROUP BY Students.group_id;
