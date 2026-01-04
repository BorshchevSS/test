import asyncio
import logging
from threading import Thread, Event as ThreadEvent
from multiprocessing import Queue, Event as MP_Event
from config import setup_logging
from file_monitor import FileMonitor
from task_manager import TaskManager
from category_analyzer import CategoryAnalyzer
import signal
import sys

class TaskPlanner:
    def __init__(self):
        setup_logging()
        self.logger = logging.getLogger(__name__)
        self.shutdown_event = MP_Event()
        self.analyzer_in_queue = Queue()
        self.analyzer_out_queue = Queue()

        self.file_event = asyncio.Event()

        self.file_monitor = None
        self.task_manager = None
        self.ana

    def setup_signal_handlers(self):
        """Настройка обработчика сигналов (для корректного завершения)"""
        def signal_handler(sig, frame):
            """Обработчик сигналов"""

            self.logger.info(f"Получен сигнал о завершении {sig}. Завершение работы.")
            self.shutdown()
            sys.exit(0)
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SI)


    def shutdown(self):