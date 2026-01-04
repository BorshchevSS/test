--Найти проекты в которых участвуют сотрубдики принятые на работу после 2020 года 
--и общее кол-во таких сотрудников в проекте больше одного

--1. Фильтруем сотрудников 
--1. Считаем сотрудников
--2. Считаем по проекту сотрудников 
SELECT p.project_name, count (e.employee_id)
as count_emp_project from Projects as p
JOIN ProjectAssignments as pa
on p.project_id = pa.project_id
JOIN Employees as e
on pa.employee_id = e.employee_id
--Фильтр на этапе запроса 
WHERE e.hire_date > '2020-12-31'
--Группируем по проектам
GROUP by p.project_name
--Фильтр на этапе результата
HAVING count(e.employee_id) > 1