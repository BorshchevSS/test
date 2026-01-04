import sqlite3
# Подключение
conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("""
    create table if not exists users(
        id integer primary key autoincrement,
        username text not null unique,
        password text not null,
        email text)
""")

#Способ 1
# data = {"username": "Kate",
#         "password": 1234,
#         "email": "k@g.com"}
#
# cursor.execute("""
#     insert into users(username, password, email)
#     values (?, ?, ?)
# """, (data["username"], data["password"], data["email"]))

#Способ 2
data = [("Alice", "123", "A@g.com"), ("Bob", "234", "b@g.com")] # Список картежей
cursor.executemany("""
    insert into users(username, password, email)
    values (?, ?, ?)
""", data)

conn.commit() #Сохранить изменение

users = cursor.execute("select * from users")
print(users.fetchall()) #
cursor.close()
conn.close()