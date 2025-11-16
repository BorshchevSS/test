import datetime
import re
from functools import wraps
import time

LOG_PATTERN = re.compile(
    r'^(\S+) \S+ \S+ \[(.+)\] \"(\S+) (\S+) (\S+)\" (\d+) (\S+) \"([^\"]*)\" \"([^\"]*)\"'
)
#138.162.138.102 - - [27/Oct/2025:00:00:05 +0300] "GET /index.html HTTP/1.1" 500 268 "http://carter.biz/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.0 (KHTML, like Gecko) Chrome/26.0.840.0 Safari/535.0"


#Дискриптор, проверка статуса кода
class StatusCodeValidator:
    def __init__(self, default_value = 0):
        self.name = None
        self.default_value = default_value

    def __set_name__(self, owner, name):
        """Стандартный метод дескриптора для сохранения имени атрибута."""
        self.name = name

    def __get__(self, instance, owner):
        if isinstance is None:
            return self
        return instance.__dict__.get(self.name, self.default_value) #по умолчанию имя, иначе 0

    def __set__(self, instance, value):
        """ ▪ Пытается преобразовать value в целое число.
            ▪ Проверяет, что число находится в диапазоне 100 до 599.
            ▪ В случае успеха устанавливает значение.
            ▪ В случае ошибки преобразования или невалидного диапазона, устанавливает значение 0 (как признак ошибки парсинга) и выводит предупреждение."""
        try:
            int_value = int(value)
            if 100 <= int_value <= 599:
                instance.__dict__[self.name] = int_value
            else:
                instance.__dict__[self.name] = self.default_value
        except (ValueError, TypeError):
            instance.__dict__[self.name] = self.default_value

def timing(func):
    """3.1.2. Декоратор @timing
• Назначение: Измерять и логировать время выполнения метода, к
которому он применен.
• Функционал:
◦ При вызове оборачиваемой функции, фиксирует время до и
после выполнения.
◦ Выводит в консоль имя функции и затраченное время в
секундах (например, Метод 'analyze' выполнен за 1.2345
сек.).
◦ Сохраняет измеренное время в атрибут analysis_time
первого аргумента (экземпляра класса LogAnalyzer)."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        #Первый агрумент - это self
        self = args[0]
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        self.analysis_time = end_time - start_time
        return result
    return wrapper

with open('../access.log', 'r') as log:
    iterrator = iter(log)
    for line in iterrator:
        line = line.strip()
        match = LOG_PATTERN.match(line)
        print(match)

class LogEntry:
    status_code = StatusCodeValidator()

    def __init__(self, ip, timestamp, method, url, protocol, status_code, size, referrer, user_agent):
        self.ip = ip
        #[27/Oct/2025:21:14:04 +0300]
        try:
            self.timestamp = datetime.datetime.strptime(timestamp.split(" ")[0], "%d/%b/%Y:%H:%M:%S")

        except ValueError:
            self.timestamp = None
        self.method = method
        self.url = url
        self.protocol = protocol
        self.status_code = status_code
        try:
            self.size = int(size)
        except ValueError:
            self.size = 0
        self.referrer = referrer #источник ссыилки
        self.user_agent = user_agent

    @property
    #Чистый путь из полного URL
    def request_path(self):
        #/
        # index.html
        pass

def log_parser():
    """3.2.3. Генератор log_parser(file_path)
• Назначение: Эффективно построчно читать лог-файл и
генерировать объекты LogEntry.
• Функционал:
◦ Использует FileContextManager для открытия файла.
◦ Итерирует по строкам файла.
◦ Для каждой строки вызывает LogEntry.from_log_line().
◦ Если получен объект LogEntry, генерирует его (yield).
◦ Игнорирует или логирует строки, которые не удалось распарсить."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                match = LOG_PATTERN.match(line)
                if  match:
                    data = match.group()
                    yield LogEntry(*data)
    except: FileNotFoundError:
        return
    except