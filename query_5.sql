SELECT Subjects.name
FROM Subjects
INNER JOIN Professors ON Subjects.professor_id = Professors.id
WHERE Professors.name = '<professor_name>';
