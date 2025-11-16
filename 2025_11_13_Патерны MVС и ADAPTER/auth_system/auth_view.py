#Вывод или запрос данных

class AuthView:
    def display_menu(self):
        print("1. Регистрация")
        print("2. Авторизация")
        print("3. Выход")

    def get_user_choice(self):
        while True:
            try:
                choice = input("> ")
                if choice in ["1", "2", "3"]:
                    return choice
                else:
                    self.display_message("Неверный ввод", True)
            except Exception as e:
                print(f"ERROR: {e}")
                return "3"

    def get_reg_data(self):
        print("\nРегистрация: ")
        username = input("Введите username: ")
        email = input("Введите email: ")
        import getpass
        password = getpass.getpass("Введите password: ")
        return username, email, password

    def get_login_data(self):
        print("\nАвторизация: ")
        username = input("Введите username: ")
        import getpass
        password = getpass.getpass("Введите password: ")
        return username, password

    def display_message(self, massage, is_error=False):
        if is_error:
            print(f"Ошибка: {massage}")
        else:
            print(f"Успех: {massage}")

    def display_welcome(self, username):
        print(f"\nДобро пожаловать, {username}")