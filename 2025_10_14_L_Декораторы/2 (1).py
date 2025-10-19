import json
import os
from datetime import datetime

FILE_LOG = 'log_func.json'

def log_calls(level='info'):

    levels = ['info', 'warning', 'error']

    def decorator(func):
        def wrapper(*args, **kwargs):
            call_time = datetime.now().isoformat()
            log_str = {
                'func_name': func.__name__,
                'arguments': {
                    'args': args,
                    'kwargs': kwargs
                },
                'call_time': call_time,
                'level': level
            }
            if os.path.exists(FILE_LOG):
                with open(FILE_LOG, 'r', encoding='utf-8') as f:
                    try:
                        logs = json.load(f)
                    except json.JSONDecodeError:
                        logs = []
            else:
                logs = []
            logs.append(log_str)

            with open(FILE_LOG, 'w', encoding='utf-8') as f:
                json.dump(logs, f, indent=4)
            return func(*args, **kwargs) # вызов исходной функции

        return wrapper
    return decorator

def filter_logs(start_time=None, end_time=None, func_name=None,
                level=None):
    if not os.path.exists(FILE_LOG):
        print('Файл не существует')
        return []

    with open(FILE_LOG, 'r', encoding='utf-8') as f:
        try:
            logs = json.load(f)
        except json.JSONDecodeError:
            print('ошибка чтения файла')
            return []

    result = []
    for log in logs:
        include_log = True #какие данные пойдут в результат

        if func_name is not None and include_log:
            if log['func_name'] != func_name:
                include_log = False

        if level is not None and include_log:
            if log['level'] != level:
                include_log = False

        if start_time is not None and include_log:
            if log['call_time'] < start_time:
                include_log = False

        if end_time is not None and include_log:
            if log['call_time'] > end_time:
                include_log = False

        if include_log:
            result.append(log)

    return result

def print_logs(logs):

    if not logs:
        print('логи не найдены')
        return

    print(f'Logs: {len(logs)}')

    for i, log in enumerate(logs, 1):
        print(f'Log # {i}')
        print(log)
        print('-'*30)


@log_calls(level='info')
def example(a, b):
    return a * b

@log_calls(level='warning')
def another(x, y, name='test'):
    return f'{x + y}, {name}'

if __name__ == '__main__':
    example(1, 2)
    example(3, 4)
    another(10, 20, name='demo')
    another(5, 15)

    print('все логи')
    print_logs(filter_logs())

    print('функция example')
    print_logs(filter_logs(func_name='example'))

    print('уровень')
    print_logs(filter_logs(level='warning'))

    print('время')
    cur_t = datetime.now().isoformat()
    print_logs(filter_logs(end_time=cur_t))

