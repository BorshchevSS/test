--Задание 2: Сотрудники с Проблемными Записями
SELECT em.full_name, em.hire_date, c.email
from Employees 		as em
LEFT JOIN Contacts 	as c on em.contact_id = c.contact_id
 --Фильтр на этапе запроса 
WHERE c.email is NULL and (em.full_name like 'В%' or em.full_name like 'Е%') AND em.hire_date <='2025-01-01'