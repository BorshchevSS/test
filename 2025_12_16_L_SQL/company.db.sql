BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS [Contacts] (
	[contact_id]	INTEGER,
	[email]	TEXT NOT NULL UNIQUE,
	[phone_number]	TEXT,
	PRIMARY KEY([contact_id])
);
CREATE TABLE IF NOT EXISTS [DepartmentLocations] (
	[department_id]	INTEGER,
	[city]	TEXT NOT NULL,
	[country]	TEXT NOT NULL,
	PRIMARY KEY([department_id]),
	FOREIGN KEY([department_id]) REFERENCES [Departments]([department_id])
);
CREATE TABLE IF NOT EXISTS [Departments] (
	[department_id]	INTEGER,
	[department_name]	TEXT NOT NULL UNIQUE,
	[head_employee_id]	INTEGER UNIQUE,
	[foundation_year]	INTEGER,
	PRIMARY KEY([department_id])
);
CREATE TABLE IF NOT EXISTS [Employees] (
	[employee_id]	INTEGER,
	[full_name]	TEXT NOT NULL,
	[hire_date]	DATE,
	[department_id]	INTEGER,
	[contact_id]	INTEGER UNIQUE,
	PRIMARY KEY([employee_id]),
	FOREIGN KEY([contact_id]) REFERENCES [Contacts]([contact_id]),
	FOREIGN KEY([department_id]) REFERENCES [Departments]([department_id])
);
CREATE TABLE IF NOT EXISTS [ProjectAssignments] (
	[employee_id]	INTEGER,
	[project_id]	INTEGER,
	[assigned_date]	DATE,
	PRIMARY KEY([employee_id],[project_id]),
	FOREIGN KEY([employee_id]) REFERENCES [Employees]([employee_id]),
	FOREIGN KEY([project_id]) REFERENCES [Projects]([project_id])
);
CREATE TABLE IF NOT EXISTS [Projects] (
	[project_id]	INTEGER,
	[project_name]	TEXT NOT NULL UNIQUE,
	[status]	TEXT NOT NULL,
	PRIMARY KEY([project_id])
);
CREATE TABLE IF NOT EXISTS [Tasks] (
	[task_id]	INTEGER,
	[project_id]	INTEGER,
	[task_description]	TEXT NOT NULL,
	[priority]	TEXT,
	[deadline]	DATE,
	PRIMARY KEY([task_id]),
	FOREIGN KEY([project_id]) REFERENCES [Projects]([project_id])
);
INSERT INTO [Contacts] VALUES (101,'ivanov.i@corp.com','555-0101');
INSERT INTO [Contacts] VALUES (102,'petrov.p@corp.com','555-0102');
INSERT INTO [Contacts] VALUES (103,'sidorova.s@corp.com','555-0103');
INSERT INTO [Contacts] VALUES (104,'kozlov.k@corp.com','555-0104');
INSERT INTO [Contacts] VALUES (105,'novikova.n@corp.com','555-0105');
INSERT INTO [Contacts] VALUES (106,'levin.l@corp.com','555-0106');
INSERT INTO [Contacts] VALUES (107,'fedorov.f@corp.com','555-0107');
INSERT INTO [Contacts] VALUES (108,'gromova.g@corp.com','555-0108');
INSERT INTO [Contacts] VALUES (109,'zhukov.z@corp.com','555-0109');
INSERT INTO [Contacts] VALUES (110,'mishin.m@corp.com','555-0110');
INSERT INTO [DepartmentLocations] VALUES (1,'Москва','Россия');
INSERT INTO [DepartmentLocations] VALUES (2,'Санкт-Петербург','Россия');
INSERT INTO [DepartmentLocations] VALUES (5,'Лондон','Великобритания');
INSERT INTO [Departments] VALUES (1,'Разработка',NULL,2010);
INSERT INTO [Departments] VALUES (2,'Маркетинг',NULL,2012);
INSERT INTO [Departments] VALUES (3,'Финансы',NULL,2008);
INSERT INTO [Departments] VALUES (4,'Продажи',NULL,2015);
INSERT INTO [Departments] VALUES (5,'HR',NULL,2018);
INSERT INTO [Employees] VALUES (1,'Иванов И.И.','2020-01-15',1,101);
INSERT INTO [Employees] VALUES (2,'Петров П.П.','2021-03-20',1,102);
INSERT INTO [Employees] VALUES (3,'Сидорова С.А.','2019-11-10',2,103);
INSERT INTO [Employees] VALUES (4,'Козлов К.В.','2022-06-01',3,104);
INSERT INTO [Employees] VALUES (5,'Новикова Н.Ю.','2023-01-25',4,105);
INSERT INTO [Employees] VALUES (6,'Левин Л.Л.','2018-08-14',1,106);
INSERT INTO [Employees] VALUES (7,'Федоров Ф.Т.','2020-04-01',5,107);
INSERT INTO [Employees] VALUES (8,'Громова Г.В.','2022-10-10',2,108);
INSERT INTO [Employees] VALUES (9,'Жуков З.И.','2023-05-18',NULL,109);
INSERT INTO [Employees] VALUES (10,'Мишин М.Н.','2021-07-07',4,NULL);
INSERT INTO [Employees] VALUES (11,'Васильев В.Е.','2024-01-01',1,NULL);
INSERT INTO [Employees] VALUES (12,'Егорова Е.М.','2024-02-02',NULL,110);
INSERT INTO [ProjectAssignments] VALUES (1,201,'2025-03-01');
INSERT INTO [ProjectAssignments] VALUES (2,201,'2025-03-01');
INSERT INTO [ProjectAssignments] VALUES (2,202,'2025-03-10');
INSERT INTO [ProjectAssignments] VALUES (3,203,'2024-11-01');
INSERT INTO [ProjectAssignments] VALUES (4,204,'2025-01-01');
INSERT INTO [ProjectAssignments] VALUES (5,205,'2025-02-15');
INSERT INTO [ProjectAssignments] VALUES (6,201,'2025-03-05');
INSERT INTO [ProjectAssignments] VALUES (7,203,'2024-11-01');
INSERT INTO [ProjectAssignments] VALUES (8,202,'2025-03-10');
INSERT INTO [ProjectAssignments] VALUES (9,205,'2025-02-15');
INSERT INTO [Projects] VALUES (201,'Мобильное приложение','Active');
INSERT INTO [Projects] VALUES (202,'Обновление сайта','Active');
INSERT INTO [Projects] VALUES (203,'Рекламная кампания','Completed');
INSERT INTO [Projects] VALUES (204,'Бюджетирование Q4','On Hold');
INSERT INTO [Projects] VALUES (205,'Система аналитики','Active');
INSERT INTO [Projects] VALUES (206,'Проект-Заглушка','New');
INSERT INTO [Tasks] VALUES (301,201,'Разработка интерфейса','High','2025-05-30');
INSERT INTO [Tasks] VALUES (302,201,'Тестирование бэкенда','High','2025-06-15');
INSERT INTO [Tasks] VALUES (303,202,'Дизайн главной страницы','Medium','2025-04-30');
INSERT INTO [Tasks] VALUES (304,202,'Написание контента','Medium','2025-05-05');
INSERT INTO [Tasks] VALUES (305,203,'Анализ результатов','Low','2024-12-31');
INSERT INTO [Tasks] VALUES (306,205,'Сбор требований','High','2025-04-10');
INSERT INTO [Tasks] VALUES (307,205,'Настройка ETL','Medium','2025-05-20');
INSERT INTO [Tasks] VALUES (308,201,'Fix bug #123','High','2025-04-10');
INSERT INTO [Tasks] VALUES (309,206,'Проверка конфигурации','Low','2025-06-01');
INSERT INTO [Tasks] VALUES (310,NULL,'Административная задача','Low','2025-04-15');
COMMIT;
