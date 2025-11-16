"""Задание 4
Задача: написать класс ConfigManager, который будет использоваться как менеджер контекста для временного
изменения конфигурации приложения. Класс должен содержать атрибут конфигурации (строку), а при инициализации
получать новое значение для него. Во время выполнения блока with конфигурация должна меняться на новую,
а при выходе из него принимать начальное значение."""

class ConfigManager:
    def __init__(self, config_object, new_value):
        self.config_object = config_object
        self.new_value = new_value
        self.initial_value = None

    def __enter__(self):
        self.initial_value = self.config_object.config_attr
        self.config_object.config_attr = self.new_value
        print(f"Конфигурация временно изменена на {self.config_object.config_attr}")
        return self.config_object

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.config_object.config_attr = self.initial_value
        print(f"Конфигурация востановлена {self.config_object.config_attr}")
        return False

class AppConfig:
    def __init__(self, initial_config):
        self.config_attr = initial_config

app_config = AppConfig(initial_config="producttion mode")
print(f"до {app_config.config_attr}")
with ConfigManager(app_config, "development mode") as temp:
    print(f"внутри {temp.config_attr}")
print(f"после {app_config.config_attr}")
