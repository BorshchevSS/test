import os
import csv
from visuallizers import ConsoleVisuallizer, ImageVisuallizer
from metrics import  ResourceMetric
import time


class MonitorManager:

    def __init__(self):
        self.metrics = []

    def add_metrics(self, metric):
        self.metrics.append(metric)


    def update_all_metrics(self):
        for metric in self.metrics:
            metric.update()

    def _clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_console(self):
        self._clear_console()
        for metric in self.metrics:
            if isinstance(metric, ResourceMetric):
                ConsoleVisuallizer.draw_bar(metric.value, metric.name)

    def run_console(self, interval: int = 1):
        try:
            while True:
                self.update_all_metrics()
                self.display_console()
                time.sleep(interval)
        except KeyboardInterrupt:
            print('\n\nМониторинг остановлен')

    def generate_image_report(self):
        self.update_all_metrics()
        visualizer = ImageVisuallizer()
        visualizer.create_report(self.metrics)

