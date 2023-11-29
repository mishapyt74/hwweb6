SELECT Students.name
FROM Students
INNER JOIN Groups ON Students.group_id = Groups.id
WHERE Groups.name = '<group_name>';
