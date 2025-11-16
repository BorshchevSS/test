# 3
class CacheManager:
    def __init__(self, cache_dict):
        self.cache = cache_dict
        print('кэш-менеджер инициализирован')

    def __enter__(self):
        print(f'текущий размер кэша {len(self.cache)}')
        return self.cache

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'очищаем кэш:  {len(self.cache)}')
        self.cache.clear()
        print(f'новый размер:  {len(self.cache)}')
        return False #если есть исключение будет переброшено
app_cache = {
    'user_1': 'data_a',
    'user_2': 'data_b',
    'session_id': 12345,
}
# print(f'кэш до {app_cache}')
# with CacheManager(app_cache) as cur_cache:
#     print(f'кэш внутри блока {cur_cache}')
#     cur_cache['new_key'] = 'new_value'
#     print(f'кэш после добавления: {cur_cache}')
# print(app_cache)

# 4
class ConfigManager:
    def __init__(self, config_object, new_value):
        self.config_object = config_object
        self.new_value = new_value
        self.initial_value = None

    def __enter__(self):
        self.initial_value = self.config_object.config_attr
        self.config_object.config_attr = self.new_value
        print(f'конфигурация временно изменена на {self.config_object.config_attr}')
        return self.config_object

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.config_object.config_attr = self.initial_value
        print(f'конфигурация восстановлена {self.config_object.config_attr}')
        return False

class AppConfig:
    def __init__(self, initial_config):
        self.config_attr = initial_config

# app_config = AppConfig(initial_config='production mode')
# print(f'before {app_config.config_attr}')
# with ConfigManager(app_config, 'development mode') as temp:
#     print(f'внутри {temp.config_attr}')
# print(f'after {app_config.config_attr}')

# 5
import time
import random

# для имитации исключения соединения
class ConnectionError(Exception):
    pass

class ApiConnectionRetry:
    def __init__(self, max_attempts=3):
        self.max_attempts = max_attempts
        self.connection = None #объект соединения если установлено

    def attempt_connection(self):

        # с вероятностью 70% выдает ошибку (проверить логику повторов)
        # random.random() float [0.0, 1.0)
        if random.random() < 0.7:
            #70% шанс на сбой
            raise ConnectionError('сбой соединения с API')
        return 'API connected successfully'

    def __enter__(self):
        attempts = 0
        while attempts < self.max_attempts:
            attempts += 1
            print(f'попытка соединения №{attempts}...')
            try:
                self.connection = self.attempt_connection()
                print('соединение успешно установлено')
                return self.connection
            except ConnectionError as e:
                print(f'не удалось соединиться: {e}')
                if attempts < self.max_attempts:
                    wait_time = random.uniform(0.5, 1.5)#случайная
                    print(f'ожидание {wait_time:.2f} сек')
                    time.sleep(wait_time)
                else:
                    print('попытки исчерпаны')
                    raise #повторно выбросит последнее исключение
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            print('соединение закрыто')
            self.connection = None
        return False


print('сценарий 1')
try:
    with ApiConnectionRetry(max_attempts=5) as api:
        print(f'внутри. {api}')
except ConnectionError as e:
    print(f'{e} (не должно случиться)')

print('сценарий 2')
try:
    with ApiConnectionRetry(max_attempts=1) as api:
        print(f'внутри. {api}')
except ConnectionError as e:
    print(f'{e} ожидаемый сбой перехвачен')

