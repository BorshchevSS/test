--Подзапрос (запрос внутри запроса)
--WHERE - фильтрация строк внешнего запроса (до 32 уровня подзапросов) результатом будет одно значение (сколярный запрос) или список
--Найти всех сотрудников, работающих в отделе основанном после 2015 года

SELECT  d.department_name, e.full_name
FROM Employees as e
JOIN Departments as d
on e.department_id = d.department_id
WHERE d.department_id in 
(SELECT department_id FROM Departments
WHERE foundation_year >= 2015);

--подзапрос после FROM
--Найти среднее количество задач на один проект для проектов в статусе Active, 
	--вывести только те проектц, где задач больше чем это среднее кол-во задач.
SELECT T1.project_name, T1.task_count FROM 
(SELECT p.project_name, count(t.task_id) as task_count 
FROM Projects as p JOIN Tasks as t on p.project_id = t.project_id
WHERE p.status = 'Active'
GROUP by p.project_name) as T1
WHERE T1.task_count > (SELECT avg(task_count) from (SELECT count(t.task_id) as task_count 
FROM Projects as p JOIN Tasks as t on p.project_id = t.project_id
WHERE p.status = 'Active'));
