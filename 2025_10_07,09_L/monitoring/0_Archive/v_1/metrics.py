from validators import PercentageValidator
from abc import ABC, abstractmethod
import psutil

class ResourceMetric(ABC):
    current_usage = PercentageValidator()

    def __init__(self, name: str):
        self.name = name
        self.current_usage = 0.0

    @abstractmethod
    def update(self) -> None:
        pass

    @property
    def value(self) -> float:
        return self.current_usage

    def __str__(self):
        return f"{self.name}: {self.value}%"

# print(psutil.cpu_percent())
# print(psutil.virtual_memory().percent)
# print(psutil.disk_usage('/').percent)

class CPUMetric(ResourceMetric):
    def __init__(self):
        super().__init__("CPU")
        psutil.cpu_percent() #для инициализации

    def update(self):
        self.current_usage = psutil.cpu_percent()

class RAMMetric(ResourceMetric):
    def __init__(self):
        super().__init__("RAM")

    def update(self):
        self.current_usage = psutil.virtual_memory().percent

class DiskMetrics(ResourceMetric):
    def __init__(self, path: str):
        super().__init__(f"Disk {path}")
        self.path = path

    def update(self) -> None:
        self.current_usage = psutil.disk_usage(self.path).percent

# ram = RAMMetric()
# print(ram)
# print(psutil.net_io_counters().bytes_recv)