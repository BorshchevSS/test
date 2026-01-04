import sqlite3
from contextlib import contextmanager
from linecache import updatecache

DB_FILE = 'company.db'

class DBManagerSingleton:
    # для хранения единственного экземпляра класса
    _instance = None
    # для хранения единственного объекта соединения с БД
    _connection = None
    _db_path = None

    def __new__(cls, db_path=DB_FILE):
        '''перехватывает создание экземпляра и обеспечивает
        возврат единственного объекта'''
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._db_path = db_path
        return cls._instance
    # метод для получения единственного экземпляра
    @staticmethod
    def get_instance():
        '''метод для получения единственного экземпляра.
        используется для доступа к методу connection'''
        if DBManagerSingleton._instance is None:
            DBManagerSingleton()
        return DBManagerSingleton._instance

    @contextmanager
    def connection(self):
        ''' контекстный менеджер для получения и управления соединением с БД.'''
        if DBManagerSingleton._connection is None:
            try: # 1. Подключение к БД
                DBManagerSingleton._connection = sqlite3.connect(self._db_path)
            except sqlite3.Error as e:
                print(f'Ошибка подключения к БД: {e}')
                raise
        conn = DBManagerSingleton._connection
        try:
            yield conn #Зафиксировать изменения если блок with выполнится без ошибок
            conn.commit() # фиксируем изменения# возможно rollback
        except Exception as e:
            print(f"Oшибка транзакции. Выполнен откат: {e}")
            conn.rollback() #Откат одной транзакции
            raise

class HRConsole:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.menu_options = {
            "1": ("Полный список сотрудников", self.show_all_employees),
            "2": ("Сотрудники без отдела/контакта",self.show_employees_without_details),
            "3": ("Информация о проектах", self.show_employee_project),
            '4': ('Сводка по отделам', self.show_department_summary),
            '5': ('Назначить сотрудника на отдел', self.assign_employee_to_dep),
            '6': ('Выход', None)

        }

    def show_menu(self):
        print("\nГлавное меню:")
        for key, (desc, _) in self.menu_options.items():
            print(f"[{key}] {desc}")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Выберите действие: ").strip()
            if choice == '6':
                print("Завершение")
                #Закрытие подключения к БД
                if DBManagerSingleton._connection:
                    DBManagerSingleton._connection.close()
                break
            if choice in self.menu_options:
                action = self.menu_options[choice][1]
                if action:
                    print("-"*75)
                    action()
                    print("-"*75)
                else:
                    pass
            else:
                print("Неверный ввод")


    def show_all_employees(self):
        print("1. Отчет: Полный список сотрудников, отделов и email")
        query = """
            SELECT e.full_name, d.department_name, c.email
            FROM Employees as e
            LEFT JOIN Departments as d
            on e.department_id = d.department_id
            LEFT JOIN Contacts as c
            on e.contact_id = c.contact_id
            ORDER by e.employee_id;
        """
        try:
             with self.db_manager.connection() as conn:
                 cursor = conn.execute(query)
                 result = cursor.fetchall()
                 print(f"| {"ФИО":<25} | {"Отдел":<20} | {"Email":<30} |")
                 for name, dept, email in result:
                     dept_display = dept if dept is not None else "Нет"
                     email_display = email if email is not None else "Нет"
                     print(f"| {name:<25} | {dept_display:<20} | {email_display:<30} |")
        except Exception as e:
            print(f"Не удалось выполнить запрос: {e}")


    def show_employees_without_details(self):
        print("2. Отчет: Сотрудники без контактов или департамента")
        query = """
                    SELECT e.employee_id, e.full_name
                    FROM Employees as e
                    LEFT JOIN Departments as d
                    on e.department_id = d.department_id
                    LEFT JOIN Contacts as c
                    on e.contact_id = c.contact_id
                    where d.department_name is null or c.email is null
                    ORDER by e.employee_id;
                """
        try:
             with self.db_manager.connection() as conn:
                 cursor = conn.execute(query)
                 result = cursor.fetchall()
                 if not result:
                     print("Все сотрудники отдела имеют контактные данные")
                     return
                 print(f"| {"ID":<4} | {"ФИО":<25} |")
                 for i, name in result:
                     print(f"| {i:<4} | {name:<25} |")
        except Exception as e:
            print(f"Не удалось выполнить запрос: {e}")


    def show_employee_project(self):
        id_empl = input("Введите id или ФИО для поиска: ").strip()
        print(f"3. Отчет: Проекты сотрудника {id_empl}")
        query = """
            SELECT p.project_name, p.status
            FROM Projects as p
            JOIN ProjectAssignments as pa
            on p.project_id = pa.project_id
            JOIN Employees as e
            on pa.employee_id = e.employee_id
            WHERE e.employee_id = ? or e.full_name like ?;
        """
        try:
             with self.db_manager.connection() as conn:
                 try:
                     emp_id = int(id_empl)
                     params = (emp_id, f"%{id_empl}%")
                 except ValueError:
                     params = (None, f"%{id_empl}%")
                 cursor = conn.execute(query, params)
                 result = cursor.fetchall()
                 if not result:
                     print("Сотрудник не найден")
                     return

                 print(f"| {"Название проекта":<30} | {"Статус":<15} |")
                 for project_name, statu in result:
                    print(f"| {project_name:<30} | {statu:<15} |")
        except Exception as e:
            print(f"Не удалось выполнить запрос: {e}")


    def show_department_summary(self):
        print(f"Отчет 4. Сводка по отделам")
        query = """
            SELECT d.department_name, count(e.employee_id) as employee_count
            FROM Departments as d
            LEFT JOIN  Employees as e
            on d.department_id = e.department_id
            GROUP by d.department_name
            ORDER by employee_count DESC, d.department_name;
        """
        try:
             with self.db_manager.connection() as conn:
                 cursor = conn.execute(query)
                 result = cursor.fetchall()
                 print(f"| {"Отдел":<25} | {"Кол-во сотрудников":<20} |")
                 for dep, count in result:
                    print(f"| {dep:<25} | {count:<20} |")
        except Exception as e:
            print(f"Не удалось выполнить запрос: {e}")

    def assign_employee_to_dep(self):
        try:
            employee_id = int(input("Введите id сотрудника: ").strip())
            dep_id = int(input("Введите id отдела: ").strip())
        except ValueError:
            print("Должны быть целыми числами")
            return

        update_query="""
            UPDATE Employees SET department_id = ?
            WHERE employee_id = ?
        """
        try:
            with self.db_manager.connection() as conn:
                conn.execute(update_query, (dep_id, employee_id))
        except Exception as e:
            print(f"Не удалось выполнить запрос: {e}")


if __name__ == '__main__':
    try:
        db_manager = DBManagerSingleton.get_instance()
        app = HRConsole(db_manager)
        app.run()
    except Exception as e:
        print(f"Фатальная ошибка: {e}")


# db_manager = DBManagerSingleton.get_instance() #
# app = HRConsole(db_manager)

# app.show_all_employees()
# app.show_employees_without_details()
# app.show_employee_project()
# app.show_department_summary()
# app.assign_employee_to_dep()

