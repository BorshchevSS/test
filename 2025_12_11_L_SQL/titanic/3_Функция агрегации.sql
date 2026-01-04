-- LEFT JOIN
SELECT name, Survived FROM test t
left JOIN gender_submission gs
on t.PassengerId = gs.PassengerId;

-- Функция агрегации - возвращают одно значение
-- count() - количество записей
-- max()
-- min()
--AVG() - среднее значение

SELECT count(*) FROM train;
SELECT count(Age) as count_age FROM train;
SELECT age, count(*) as count_passenger FROM train
GROUP BY Age;

SELECT name, max(age) as max_age from train --ответ 9 так как это текст а не число
WHERE pclass = 1 --ищим пассажиров первого класса
GROUP by Name; --группируй по имени