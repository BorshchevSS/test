--Задание 1: Эффективность Отделов по Проектам
SELECT de.department_name, count(p.project_id) --p.project_name, p.status,
as count_emp_project from Projects as p
JOIN ProjectAssignments as pa 	on p.project_id = pa.project_id
JOIN Employees as em 			on pa.employee_id = em.employee_id
JOIN Departments as de			on em.department_id = de.department_id
 --Фильтр на этапе запроса 
WHERE p.status = 'Active'
--Группируем по проектам
GROUP by de.department_name
--Фильтр на этапе результата
HAVING count(em.employee_id) > 1