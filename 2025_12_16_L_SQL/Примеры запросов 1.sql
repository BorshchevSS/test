-- Пример с INNER JOIN (совпадение в обеих таблицах)
-- SELECT e.full_name, c.email, c.phone_number
-- FROM Employees as e 
-- JOIN Contacts as c
-- on e.contact_id = C.contact_id


--Пример с LEFT JOIN
-- SELECT e.full_name, c.email
-- FROM Employees as e 
-- LEFT JOIN Contacts as c
-- on e.contact_id = C.contact_id
-- 
-- WHERE - на уровне строк (во время запроса)
-- HAVING - (на уровне сгруппированных результатов)

-- Порядок выполнения операций: FROM, JOIN, WHERE, GROUP by, Агрегации, HAVING, ORDER by

-- Узнать в каком отделе работает более 2 сотрудников.
--1 Количество в каждом отделе
SELECT d.department_name, count (e.employee_id) 
as Employees_count FROM Departments as d 
JOIN Employees as e 
on d.department_id = e.department_id
GROUP by d.department_name
--фильтруем результат группировки
HAVING count (e.employee_id) >= 2;