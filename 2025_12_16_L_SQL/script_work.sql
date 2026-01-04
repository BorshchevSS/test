-- Включение поддержки внешних ключей в SQLite
PRAGMA foreign_keys = ON;

-- 1. Таблица 'Сотрудники' (Employees)
-- Сторона 'Один' в 1:М с Отделами и 1:1 с Контактами
CREATE TABLE Employees (
    employee_id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    hire_date DATE,
    department_id INTEGER, -- Внешний ключ 1:М к 'Отделы'
    contact_id INTEGER UNIQUE, -- Внешний ключ 1:1 к 'Контакты' (UNIQUE для 1:1)
    FOREIGN KEY (department_id) REFERENCES Departments(department_id),
    FOREIGN KEY (contact_id) REFERENCES Contacts(contact_id)
);

-- 2. Таблица 'Отделы' (Departments)
-- Сторона 'Один' в 1:М с Сотрудниками
CREATE TABLE Departments (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT NOT NULL UNIQUE,
    head_employee_id INTEGER UNIQUE, -- 1:1 к Сотрудники  
    foundation_year INTEGER
);

-- 3. Таблица 'Контакты' (Contacts)
-- Сторона 'Один' в 1:1 с Сотрудниками
CREATE TABLE Contacts (
    contact_id INTEGER PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    phone_number TEXT
);

-- 4. Таблица 'Проекты' (Projects)
-- Сторона 'Один' в 1:М с Задачи, Сторона 'Многие' в М:М с Сотрудниками
CREATE TABLE Projects (
    project_id INTEGER PRIMARY KEY,
    project_name TEXT NOT NULL UNIQUE,
    status TEXT NOT NULL -- Например: 'Active', 'Completed', 'On Hold'
);

-- 5. Таблица 'Задачи' (Tasks)
-- Сторона 'Многие' в 1:М с Проектами
CREATE TABLE Tasks (
    task_id INTEGER PRIMARY KEY,
    project_id INTEGER, -- Внешний ключ 1:М к 'Проекты'
    task_description TEXT NOT NULL,
    priority TEXT,
    deadline DATE,
    FOREIGN KEY (project_id) REFERENCES Projects(project_id)
);

-- 6. Таблица 'Назначения_Проектов' (ProjectAssignments)
-- Стыковочная таблица для связи Многие_Ко_Многим (Employees <-> Projects)
CREATE TABLE ProjectAssignments (
    employee_id INTEGER,
    project_id INTEGER,
    assigned_date DATE,
    PRIMARY KEY (employee_id, project_id), -- Составной первичный ключ
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id),
    FOREIGN KEY (project_id) REFERENCES Projects(project_id)
);

-- 7. Таблица 'Локации_Отделов' (DepartmentLocations)
CREATE TABLE DepartmentLocations (
    department_id INTEGER PRIMARY KEY, -- 1:1 по ключу 'department_id'
    city TEXT NOT NULL,
    country TEXT NOT NULL,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);
 
-- 2. Отделы (Departments) - 5 строк
INSERT INTO Departments (department_id, department_name, foundation_year) VALUES
(1, 'Разработка', 2010),
(2, 'Маркетинг', 2012),
(3, 'Финансы', 2008),
(4, 'Продажи', 2015),
(5, 'HR', 2018);

-- 3. Контакты (Contacts) - 10 строк
INSERT INTO Contacts (contact_id, email, phone_number) VALUES
(101, 'ivanov.i@corp.com', '555-0101'),
(102, 'petrov.p@corp.com', '555-0102'),
(103, 'sidorova.s@corp.com', '555-0103'),
(104, 'kozlov.k@corp.com', '555-0104'),
(105, 'novikova.n@corp.com', '555-0105'),
(106, 'levin.l@corp.com', '555-0106'),
(107, 'fedorov.f@corp.com', '555-0107'),
(108, 'gromova.g@corp.com', '555-0108'),
(109, 'zhukov.z@corp.com', '555-0109'),
(110, 'mishin.m@corp.com', '555-0110');

-- 1. Сотрудники (Employees) - 12 строк

INSERT INTO Employees (employee_id, full_name, hire_date, department_id, contact_id) VALUES
(1, 'Иванов И.И.', '2020-01-15', 1, 101), 
(2, 'Петров П.П.', '2021-03-20', 1, 102),  
(3, 'Сидорова С.А.', '2019-11-10', 2, 103),  
(4, 'Козлов К.В.', '2022-06-01', 3, 104),  
(5, 'Новикова Н.Ю.', '2023-01-25', 4, 105), 
(6, 'Левин Л.Л.', '2018-08-14', 1, 106),  
(7, 'Федоров Ф.Т.', '2020-04-01', 5, 107), 
(8, 'Громова Г.В.', '2022-10-10', 2, 108),  
(9, 'Жуков З.И.', '2023-05-18', NULL, 109), 
(10, 'Мишин М.Н.', '2021-07-07', 4, NULL), 
(11, 'Васильев В.Е.', '2024-01-01', 1, NULL), 
(12, 'Егорова Е.М.', '2024-02-02', NULL, 110); 

-- 4. Проекты (Projects) - 6 строк
INSERT INTO Projects (project_id, project_name, status) VALUES
(201, 'Мобильное приложение', 'Active'),
(202, 'Обновление сайта', 'Active'),
(203, 'Рекламная кампания', 'Completed'),
(204, 'Бюджетирование Q4', 'On Hold'),
(205, 'Система аналитики', 'Active'),
(206, 'Проект-Заглушка', 'New');  

-- 5. Задачи (Tasks) - 10 строк
-- Связь 1:М с Проектами.  
INSERT INTO Tasks (task_id, project_id, task_description, priority, deadline) VALUES
(301, 201, 'Разработка интерфейса', 'High', '2025-05-30'),
(302, 201, 'Тестирование бэкенда', 'High', '2025-06-15'),
(303, 202, 'Дизайн главной страницы', 'Medium', '2025-04-30'),
(304, 202, 'Написание контента', 'Medium', '2025-05-05'),
(305, 203, 'Анализ результатов', 'Low', '2024-12-31'),
(306, 205, 'Сбор требований', 'High', '2025-04-10'),
(307, 205, 'Настройка ETL', 'Medium', '2025-05-20'),
(308, 201, 'Fix bug #123', 'High', '2025-04-10'),
(309, 206, 'Проверка конфигурации', 'Low', '2025-06-01'),
(310, NULL, 'Административная задача', 'Low', '2025-04-15');  

-- 6. Назначения_Проектов (ProjectAssignments) - 10 строк
-- Связь М:М (Employee <-> Project).
INSERT INTO ProjectAssignments (employee_id, project_id, assigned_date) VALUES
(1, 201, '2025-03-01'),
(2, 201, '2025-03-01'),
(2, 202, '2025-03-10'), -- Сотрудник 2 в 2 проектах (М:М)
(3, 203, '2024-11-01'),
(4, 204, '2025-01-01'),
(5, 205, '2025-02-15'),
(6, 201, '2025-03-05'),
(7, 203, '2024-11-01'),
(8, 202, '2025-03-10'),
(9, 205, '2025-02-15'); -- Сотрудник 9 назначен, но без отдела

-- 7. Локации_Отделов (DepartmentLocations) - 3 строки
-- 1:1 с Отделами, но не для всех отделов  
INSERT INTO DepartmentLocations (department_id, city, country) VALUES
(1, 'Москва', 'Россия'),
(2, 'Санкт-Петербург', 'Россия'),
(5, 'Лондон', 'Великобритания');