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
                with open(FILE_LOG, 'r') as f:
                    logs = json.load(f)
            else:
                logs = []
            logs.append(log_str)

            with open(FILE_LOG, 'w') as f:
                json.dump(logs, f, indent=4)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_calls(level='info')
def example(a, b):
    return a * b

# example(1, 2)
# example(3, 4)



print(ord('B'))
print(chr(68))