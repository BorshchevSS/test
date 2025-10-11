import os
import sys
from random import choice
from metrics import CPUMetric, RAMMetric, DiskMetric, ResourceMetric
from manager import MonitorManager

def main():
    manager = MonitorManager()
    manager.add_metrics(CPUMetric())
    manager.add_metrics(RAMMetric())

    root_path = '/'
    if sys.platform == 'win32': # C:\
        root_path = os.getenv('SystemDrive', 'C:') + '\\'
    manager.add_metrics(DiskMetric(path=root_path))

    while True:
        print('\nВыберите действие:')
        print('1. Запустить мониторинг в реальном времени')
        print('2. Сгенерировать графический отчет')
        print('3. Выйти')

        choice = int(input())

        if choice == 1:
            manager.run_console()
        elif choice == 2:
            manager.generate_image_report()
        elif choice == 3:
            break
        else:
            print('неверный ввод')
if __name__ == '__main__':
    main()