import os
import csv
from visuallizers import ConsoleVisuallizer
from metrics import CPUMetric, RAMMetric, DiskMetrics, ResourceMetric
import time


class MonitorManager:
    def __init__(self):
        self.metrics = []

    def __add__(self, metric):
        self.metrics.append(metric)

    def update_all_metriccs(self):
        for metric in self.metrics:
            metric.update()

    def _clear_console(self):
        os.system("cls" if os.name == "nt" else "clear")

    def display_console(self):
        self._clear_console()

        for metric in self.metrics:
            if isinstance(metric, ResourceMetric):
                ConsoleVisuallizer.draw_bar(metric.value, metric.name)

    def run_console(self, interval: int = 1):
        while True:
            self.update_all_metriccs()
            self.display_console()
            time.sleep(interval)

def main():
    manager = MonitorManager()
    manager.add_metrics(CPUMetric)