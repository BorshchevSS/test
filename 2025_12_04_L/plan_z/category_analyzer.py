# Процесс (загрузка, ..)
import logging
from multiprocessing import Process, Queue
from config import CATEGORIES, CATEGORY_KEYWORDS
import time

logger = logging.getLogger(__name__)

class CategoryAnalyzer(Process):
    """Наследуем класс процессы"""
    def __init__(self, input_queue: Queue, output_queue: Queue):
        super().__init__()
        self.input_queue = input_queue
        self.output_queue = output_queue
        self.name = "AnalyzerProcess"
        self.daemon = True

    def analyze_task(self, task_desc: str)->str:
        task_lower = task_desc.lower()
        for category, keywords in CATEGORY_KEYWORDS.items():
            #Перебор слов, поиск совпадений
            for keyword in keywords:
                if keyword in task_lower:
                    time.sleep(0.2)
                    return category
        return "Не определена"

    def run(self):
        # основной цикл для работы процесса
        logger.info(f"Процесс Анализатор запущен и ожидает задач в очереди")
        while True:
            try:
                task_data = self.input_queue.get() # блокирующее ожидание
                #    task_data (row_index, task_data) - кортеж
                if task_data is None:
                    logger.info("Получен сигнал о завершении. Процесс Анализатора завершает работу")
                    break
                row_index, task_desc = task_data
                logger.info(
                    f'Задача "{task_desc}" (строка {row_index}) передача в процесс для анализа')
                new_category = self.analyze_task(task_desc)
                logger.info(f"Процесс определил категорию для задачи '{task_desc}': {new_category}")
                self.output_queue.put((row_index, new_category)) #Передаем картеж
            except KeyboardInterrupt: # Если прерывание, выходим из цикла
                break
            except Exception as e:
                logger.error(f"Ошибка в Процессе-Анализаторе: {e}")



