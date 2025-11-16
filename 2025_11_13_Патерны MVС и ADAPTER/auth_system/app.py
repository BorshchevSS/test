from auth_controller import AuthController
from auth_view import AuthView
from user_storage import UserStorage

class Application:
    def __init__(self):
        self.storage = UserStorage()
        self.controller = AuthController(self.storage)
        self.view = AuthView()

    def run(self):
        while True:
            if self.controller.is_authenticated():
                user = self.controller.get_current_user()
                self.view.display_message(f"Авторизован {user.username}")

            self.view.display_menu()
            choice = self.view.get_user_choice()
            if  choice == "1":
                username, email, password = self.view.get_reg_data()
                result = self.controller.register(username, email, password)

                if result is True:
                    self.view.display_message("Регистрация прошла успешно")
                else:
                    self.view.display_message(result, is_error=True)

            elif choice == "2":
                if self.controller.is_authenticated():
                    self.view.display_message("Вы уже авторизированы")
                    continue
                username, password = self.view.get_reg_data()
                result = self.controller.login(username, password)

                if result is True:
                    self.view.display_welcome(username)
                    self.view.display_message(result)

            elif choice == "3":
                if self.controller.is_authenticated():
                    self.controller.logout()
                    self.view.display_message("Выход выполнен")
                break

if __name__ == "__main__":
    app = Application()
    app.run()
