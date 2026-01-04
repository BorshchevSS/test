import json
import os
# Singleton класс для управления конфигурацией (Config)
class ConfigError(Exception):
    '''Кастомное исключение для ошибок конфигурации'''
    pass

class Config:
    '''Singleton класс для хранения и управления глобальными настройками приложения
    Поддерживает профили (dev, prod) и режим "только для чтения"'''

    _instance = None # для хранения единственного экземпляра Singleton
    _configurations = {} # для хранения профилей конф.
    _current_config = {} # активный профиль конф.
    _read_only = False #режим только для чтения
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # Если экземпляра еще нет, создаем его
            cls._instance = super(Config, cls).__new__(cls)
            # Инициализация должна происходить только при первом создании
            cls._instance._is_initialized = False
        return cls._instance

    def __init__(self):
        # Предотвращаем повторную инициализацию при каждом обращении к конструктору
        if self._is_initialized:
            return
        self._is_initialized = True

    def load_config(self, file, profile='default'):
        '''Загружает настройки из json файла в указанный профиль'''
        if not os.path.exists(file):
            raise ConfigError('файл конф. не найден')
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Сохраняем загруженные данные в словарь профилей
        self._configurations[profile] = data
        print(f'конф. для {profile} загружена')

    def set_profile(self, profile):
        '''Устанавливает активный профиль конфигурации'''
        if profile not in self._configurations:
            raise ConfigError(f'{profile} не найден')
        self._current_config = self._configurations[profile]
        print('актив. проф. установлен')
        # Сбрасываем режим "только для чтения" при смене профиля
        self.set_read_only(False)

    # Управление режимом "только для чтения"
    def set_read_only(self, is_read_only):
        '''Устанавливает/снимает режим "только для чтения"'''
        self._read_only = is_read_only

    # перехват доступа к атрибуту(чтение)
    def __getattr__(self, name):
        '''Позволяет обращаться к настройкам напрямую: config.DATABASE_HOST'''
        # Сначала проверяем, не является ли запрашиваемый атрибут внутренним
        if name.startswith('_'):
            # Вызываем стандартный __getattribute__ для внутренних атрибутов (вроде _current_config)
            return object.__getattribute__(self, name)
        # Ищем ключ в активной конфигурации
        if name in self._current_config:
            return self._current_config[name]
        raise AttributeError(f'{name} настройка не найдена')

    # перехват установки атрибута (запись/обновление)
    def __setattr__(self, name, value):
        '''Безопасное обновление значений конфигурации и блокировка изменений'''
        # Если пытаемся установить внутренний атрибут (например, _read_only), пропускаем логику блокировки
        if name.startswith('_'):
            return object.__setattr__(self, name, value)
        # 1. Проверка режима "только для чтения"
        if self._read_only:
            raise ConfigError('режим только для чтения')
        # 2. Обновление значения в активной конфигурации
        self._current_config[name] = value

    # Добавление метода для проверки существования настройки
    def has_setting(self, name):
        '''Проверяет, существует ли настройка в активном профиле'''
        return name in self._current_config

config1 = Config()
config2 = Config()
print(config1 is config2)

config1.load_config("config_dev.json", profile="dev")
config1.load_config("config_prod.json", profile="prod")
print("использование профиля dev")
config1.set_profile("dev")
print(f"Текущий API_URL: {config1.API_URL}")
print(f"Текущий TIMEOUT: {config1.TIMEOUT}")
print("Обновление настройки dev")
config1.API_URL = "http://new.dev.api.com"
print(f"Новый API_URL: {config1.API_URL}")

print("Переключение на профиль prod")
config1.set_profile("prod")
config1.set_read_only(True)
print(f"API_URL: {config1.API_URL}")

try:
    config1.TIMEOUT = 60
except ConfigError as e:
    print(f"Исключение перехвачено {e}")