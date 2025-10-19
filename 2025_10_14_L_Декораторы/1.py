import json
import os
import time

class Cache:
    def __init__(self, func=None, filename='cache.json', max_size=5, ttl=60):
        self.filename = filename
        self.max_size = max_size
        self.ttl = ttl
        self.func = func
        self._init_cache()

    def _init_cache(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump({}, f)

    def _load_cache(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}

    def _save_cache(self, cache_data):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(cache_data, f, indent=4)


    def _clean_cache_expire(self, cache_data):
        current_time = time.time()

        valid_cache = {}

        for key, value in cache_data.items():
            if current_time - value['timestamp'] <= self.ttl:
                valid_cache[key] = value

        return valid_cache

    def _max_size_cache(self, cache_data):
        if len(cache_data) <= self.max_size:
            return cache_data

        sorted_data = sorted(cache_data.items(),
                             key=lambda x: x[1]['timestamp'],
                             reverse=True)
        return dict(sorted_data[:self.max_size])

    def __call__(self, *args, **kwargs):
        cache_data = self._load_cache()
        cache_data = self._clean_cache_expire(cache_data)
        key = f'{self.func.__name__}{args}{kwargs}'
        if key in cache_data:
            return cache_data[key]['result']
        result = self.func(*args, **kwargs)
        cache_data[key] = {
            'result': result,
            'timestamp': time.time(),
            'function': self.func.__name__,
            'args': str(args),
            'kwargs': str(kwargs)
        }
        cache_data = self._max_size_cache(cache_data)
        self._save_cache(cache_data)

        print(f'вычислен результат для {self.func.__name__}{args}')
        return result

    def _clear_cache(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump({}, f)

@Cache
def example(a, b, op='mul'):
    # if op == 'mul':
    #     return a * b
    # elif op == 'add':
    #     return a + b
    # else:
    #     return None
    return [i for i in range(0, b, a)]

print('вызов 1 (3, 5000, mul)')
start_time = time.time()
res1 = example(3, 50000, 'mul')
time_taken = time.time() - start_time
print(f'Res 1: {res1}')
print(f'{time_taken} sec')

print('вызов 2 (3, 5, mul) из кэша')
start_time = time.time()
res2 = example(3, 50000, 'mul')
time_taken2 = time.time() - start_time
print(f'Res 2: {res2}')
print(f'{time_taken} sec')
print(f'{time_taken2} sec')

example._clear_cache()