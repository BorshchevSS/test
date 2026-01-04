#логирование

EXCEL_FILE = "tasks.xlsx"
LOG_FILE = "planner.log"
NOTIFY_FILE = "notification.wav"

MONITOR_INTERVAL = 10

COLUMNS = {
    "TIME": "Время",
    "TASK": "Задача",
    "CATEGORY": "Категоря",
    "STATUS": "Статус"
}

CATEGORIES = ["Работа", "Учеба", "Личное", "Не определена"]
STATUS_PENDING = "Pending"
STATUS_DONE = "Done"

CATEGORY_KEYWORDS = {
    "Работа": ["отчет", "созвон", "клиенту", "заказ", "встреча"],
    "Учеба": ["экзамен", "курс", "проект", "домашка", "лабораторная"],
    "Личное": ["врач", "покупки", "ужин", "спортзал", "прогулка"]
}

# Логированиие
import logging
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name) - %(levelname)s - %(threadName)s - %(message)s',
        handlers=[logging.FileHandler(LOG_FILE, mode="a", encoding="utf-8"),
            logging.StreamHandler()]
    )