#Работа с данными

import json
import os

from psutil import users

from user import User

class UserStorage:
    def __init__(self, filename="user.json"):
        self.filename = filename
        self._users = {} #{"username": User_obj}
        self.long_users()

    def long_users(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for user_data in data:
                        user = User.to_object(user_data)
                        self._users[user.username] = user
            except json.JSONDecodeError:
                print(f"Файл поврежден или список пуст")
                self._users = {}

    def save_users(self):
        data_to_save = [user.to_dict() for user in self._users.values()] #Преобразуем объекты user в список словарей через Списковое включение
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, indent=4)

    def add_user(self, user):
        self._users[user.username] = user
        self.save_users()

    def get_user(self, username):
        return self._users.get(username)

    def get_all_users(self):
        return list(self._users.values())