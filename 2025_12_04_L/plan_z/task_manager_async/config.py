
EXCEL_FILE = 'tasks.xlsx'
LOG_FILE = 'planner.log'
NOTIFY_FILE = 'notification.wav'

MONITOR_INTERVAL = 10

COLUMNS = {
    'TIME': 'Время',
    'TASK': 'Задача',
    'CATEGORY': 'Категория',
    'STATUS': 'Статус'
}

CATEGORIES = ['Работа', 'Учеба', 'Личное', 'Не определена']
STATUS_PENDING = 'Pending'
STATUS_DONE = 'Done'

CATEGORY_KEYWORDS = {
    'Работа': ['отчет', 'созвон', 'клиенту', 'заказ', 'встреча'],
    'Учеба': ['экзамен', 'курс', 'проект', 'домашка', 'лабораторная'],
    'Личное': ['врач', 'покупки', 'ужин', 'спортзал', 'прогулка']
}
# логирование
import logging
LOG_CONFIG = {
    'level': logging.INFO,
    'format': '%(asctime)s - %(levelname)s - %(threadName)s - %(message)s',
    'logfile': LOG_FILE,
    'filemode': 'a',
}