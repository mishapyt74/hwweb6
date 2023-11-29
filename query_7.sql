SELECT Students.name, Grades.grade
FROM Grades
INNER JOIN Students ON Grades.student_id = Students.id
INNER JOIN Groups ON Students.group_id = Groups.id
WHERE Groups.name = '<group_name>' AND Grades.subject_id = <subject_id>;
