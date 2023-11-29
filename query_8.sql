SELECT Professors.name, AVG(Grades.grade) as avg_grade
FROM Grades
INNER JOIN Subjects ON Grades.subject_id = Subjects.id
INNER JOIN Professors ON Subjects.professor_id = Professors.id
GROUP BY Professors.name;
