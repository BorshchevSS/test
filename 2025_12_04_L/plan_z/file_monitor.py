import logging
from threading import Thread, Event
from config import EXCEL_FILE, MONITOR_INTERVAL # файл эксель будем проверять каждые 10 секунд
import time
from pathlib import Path

logger = logging.getLogger(__name__)

class FileMonitor(Thread):
    def __init__(self, async_event: Event):
        super().__init__()
        self.async_event = async_event
        self.file_path = Path(EXCEL_FILE)
        self.stop_event = Event() # для остановки потока
        self.name = "MonitorThread"
        self._last_size = 0
        self.daemon=True

    def get_file_size(self):
        try:
            if self.file_path.exists():
                return self.file_path.stat().st_size # размер файла
            return -1
        except Exception as e:
            logger.error(f"Ошибка при получении размера файла '{e}'")
            return -1

    def run(self):
        logger.info(f"Мониторинг файла '{EXCEL_FILE}' запущен. Интервал '{MONITOR_INTERVAL}'")
        self._last_size = self.get_file_size()
        while not self.stop_event.is_set():
            try:
                time.sleep(MONITOR_INTERVAL)
                curr_size = self.get_file_size()
                if curr_size == -1:
                    self._last_size = 0

                    continue
                if curr_size > self._last_size:
                    logger.warning(f"Обнаружены изменения в файле {EXCEL_FILE}")
                    self.async_event.set() #Подаем сигнал основному циклу
                    self._last_size = curr_size
                elif curr_size < self._last_size:
                    logger.warning(f"Файл {EXCEL_FILE} уменьшился в размере")
                    self.async_event.set()
                    self._last_size = curr_size
                else:
                    logger.warning(f"Файл {EXCEL_FILE} был изменён")
                self.async_event.set() #Событие для уведомления основного цикла
            except Exception as e:
                logger.error(f"Ошибка в потоке мониторинга: {e}")

    def stop(self):
        self.stop_event.set() # Установка флага для корректного завершения


















