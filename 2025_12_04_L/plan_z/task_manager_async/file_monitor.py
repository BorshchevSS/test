import logging
from threading import Thread, Event
from config import EXCEL_FILE, MONITOR_INTERVAL
import time
from pathlib import Path

logger = logging.getLogger(__name__)

class FileMonitor(Thread):
    def __init__(self, async_event: Event):
        super().__init__()
        self.async_event = async_event
        self.file_path = Path(EXCEL_FILE)
        self.stop_event = Event() #для остановки потока
        self.name = 'MonitorThread'
        self._last_size = 0

    def get_file_size(self):
        try:
            return self.file_path.stat().st_size #размер файла
        except FileNotFoundError:
            logger.error(f'Файл {EXCEL_FILE} не найден')
            return -1

    def run(self):
        logger.info(f'Мониторинг файла {EXCEL_FILE} запущен.'
                    f'Интервал {MONITOR_INTERVAL}')
        self._last_size = self.get_file_size()
        while not self.stop_event.is_set():
            time.sleep(MONITOR_INTERVAL)
            curr_size = self.get_file_size()
            if curr_size == -1:
                self._last_size = 0
                continue
            if curr_size > self._last_size:
                logger.warning(f'Обнаружены изменения в файле {EXCEL_FILE}')
                self.async_event.set() #подаем сигнал основному циклу
                self._last_size = curr_size
            elif curr_size < self._last_size:
                logger.warning(f'Файл {EXCEL_FILE} уменьшился в размере')
                self.async_event.set()
                self._last_size = curr_size

    def stop(self):
        self.stop_event.set() #устанавливаем флаг для корректного завершения


