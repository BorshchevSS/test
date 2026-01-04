import json
import os

class ConfigError(Exception):
    pass

class Config:
    _instance = None
    _configurations = {} #Для хранения профилей конфиг.
    _current_config = {} #Активный профиль конф.
    _read_only = False #Режим только для чтения
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._is_initialized = False
        return cls._instance

    def __init__(self):
        if self._is_initialized:
            return
        self._is_initialized = True

    def load_config(self, file, profile = "default"):
        if not os.path.exists(file):
            raise ConfigError("Файл конф. не найден")
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

            self._configurations[profile] = data
            print(f"конфиг. для {profile} загружен")

    def set_profile(self, profile):
        if profile not in self._configurations:
            raise ConfigError(f"{profile} не найден")
        self._current_config = self._configurations[profile]
        print("актив. проф. установлен")
        self.set_read_only(False)

    def set_read_only(self, is_read_only):
        self._read_only = is_read_only

    #Перехват доступа к атрибуту
    def __getattr__(self, name):
        if name.startswith("_"):
            return object.__getattribute__(self, name)

        if name in self._current_config:
            return self._current_config[name]
        raise AttributeError(f"{name} настройка не найдена")
    # перехват установки атибута (запись/обновление)
    def __setattr__(self, name, value):
        if name.startswith("_"):
            return  object.__setattr__(self, name, value)

        if self._read_only:
            raise ConfigError("Режим только для чтения")
        self._current_config[name] = value

    def has_setting(self, name):
        return name in self._current_config
