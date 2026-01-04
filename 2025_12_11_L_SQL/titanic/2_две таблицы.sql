-- like
-- % - любое количество символов
-- _ - один символ
-- BETWEEN (AND)
-- IN (1 or 3 or 4)
-- 
-- JOIN = INNER JOIN 
-- LEFT JOIN
-- RIGHT JOIN
-- FULL JOIN

-- SELECT Name FROM train
-- WHERE Name like '%William%';

SELECT Name, age FROM train
WHERE Age BETWEEN 2 and 6;

SELECT Name, age FROM train
WHERE age in (1, 5, 8);


-- JOIN = INNER JOIN 
SELECT name, Survived FROM test t  --псевданим таблицы test 
JOIN gender_submission gs -- объединяю по
on t.PassengerId = gs.PassengerId -- условие объединения
WHERE t.Pclass = 1;
