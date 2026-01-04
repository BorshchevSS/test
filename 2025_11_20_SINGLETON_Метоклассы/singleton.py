class Singleton(type):
    #Метоклас под крышей котогоро мы будем создавать синглтоны
    #Вызывается только один раз. Может понадобиться для создания уникального доступа.
    _instances = {} #словарь экземпляров
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            #Создаем новый экземпляр
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

#Применяем синглтон к лассу и проверяем
class App(metaclass=Singleton):
    def __init__(self, debug_mode = False):
        if not hasattr(self, "_initialized"):
            self.debug_mode = debug_mode
            self._initialized = False
            print("Инициализация конфигурации")
        else:
            print("Вторая попытка проигнорирована")

    def set_db(self, path):
        self.db_path = path
        print("Путь к БД установлен")

config1 = App(debug_mode=True)
config1.set_db("data/db")
print(config1.debug_mode)

config2 = App(debug_mode=False) #Попытка второй инициализации будет проигнорирована
print(config2.debug_mode)
print(config2.db_path)
print(config1 is config2)
print(id(config1), id(config2))
