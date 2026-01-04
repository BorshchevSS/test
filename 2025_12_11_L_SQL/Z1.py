import sqlite3
from datetime import datetime, timedelta
from time import daylight

DATABASE = "users.db"
def create_table():
    with sqlite3.connect(DATABASE) as conn: #Подключаемся к таблице
        cursor = conn.cursor() #Создаем область для выполнения запроса (описание столбцов таблицы)
        cursor.execute("""
            create table if not exists users(
                CustomerID integer primary key autoincrement,
                FirstName text,
                LastName text,
                Email text,
                Phone text,
                RegistrationDate text,
                IsActive INTEGER default 1)
                """)
        conn.commit()
        print("Таблица users создалась")

def insert_user(data):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.executemany("""
        insert into users(FirstName, LastName, Email, Phone, RegistrationDate)
        values(?, ?, ?, ?, ?)
        """, data)
        conn.commit()
        print("Данные успешно вставлены")

def get_not_active():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        days_ago = datetime.now() - timedelta(days=30)
        cursor.execute("""
        select * fromm users
        where RegistrationDate < ? and IsActive = 0
        """, (days_ago.strftime("%Y-%m-%d"), ))
    return cursor.fetchall()


def update_user(customerId, status):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        update users set IsActive = ?
        where CustomerID = ?
        """, (customerId, status))
        conn.commit()

def delete_user():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        days_ago = datetime.now() - timedelta(days=60)
        cursor.execute("""
        delete from users
        where RegistrationDate < ? and IsActive = 0
        """, (days_ago.strftime("%Y-%m-%d"), ))
        conn.commit()
