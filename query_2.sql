SELECT student_id, AVG(grade) as avg_grade
FROM Grades
WHERE subject_id = <subject_id>
GROUP BY student_id
ORDER BY avg_grade DESC
LIMIT 1;
