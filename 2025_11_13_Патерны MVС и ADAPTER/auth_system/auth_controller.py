#Инициализация объекта контроллера и хранилища

import re
from user import User

class AuthController:
    def __init__(self, user_storage):
        self._user_storage = user_storage
        self._current_user = None

    def is_authenticated(self):
        return self._current_user is not None

    def get_current_user(self):
        return self._current_user

    def validate_data(self, username, email, password):
        if not(4 <= len(username) <= 20):
            return "Имя должно быть от 4 до 20 символов"

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return "Не выерный формат email"

        if len(password) < 8:
            return "Должен содержать не менее 8 символов"
        if not re.search(r"[A-Z]]", password):
            return f"Должен содержать хотя бы одну заглавную букву {password}"
        if not re.search(r"[a-z]]", password):
            return "Должен содержать хотя бы одну строчную букву"
        if not re.search(r"[0-9]]", password):
            return "Должен содержать хотя бы одну 1 цифру"
        return None

    def register(self, username, email, password):
        valid_error = self.validate_data(username, email, password)
        if  valid_error:
            return valid_error

        if self._user_storage.get_user(username):
            return "Пользователь уже существует"
        try:
            password_hash = User.hash_password(password)
            new_user = User(username, email, password_hash)
            self._user_storage.add_user(new_user)
            return True
        except Exception as e:
            return f"Ошибка: {e}"

    def login(self, username, password):
        user = self._user_storage.get_user(username)
        if not user:
            return "Пользователь не существует"
        if user.check_password(password):
            self._current_user = user
            return True
        else:
            return "Неверный пароль"

    def logout(self):
        if self._user_storage:
            self._current_user = None
            return True
        return False
