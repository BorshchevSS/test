import time
from functools import  wraps
import os

class Timing:
    def __init__(self, log_file = "time_log.txt", duration = 0.5):
        self.log_file = log_file
        self.duration = duration

    def __call__(self, func):
        @wraps(func)
        def wrapper (*args, **kwargs): #любое количество именованных (неизменяемый список-кортеж) и неименованных параметров (словарь)
            #def func(a, b, *args, l=None, **kwargs)
            start_time = time.time()
            res = func(*args, **kwargs)
            end_time = time.time()
            dur = end_time - start_time
            warning_message = ''
            if dur > self.duration:
                warning_message = f"ВНИМАНИЕ! Слишком долго; {dur}"
            print(f"Функция {func.__name__} выполнилась за {dur} сек")
            if warning_message:
                print(warning_message)
            print("_"*30)

            log_str = [
                f"Func: {func.__name__}",
                f"Duration: {dur}",
                f"Warning: {warning_message}\n",
            ]

            try:
                with open(self.log_file, "a", encoding="utf-8") as f:
                    f.writelines(log_str)
            except IOError as e:
                return f"ошибка записи: {e}"

            return res
        return wrapper



@Timing()
def fast(n):
    print("начало ")
    time.sleep(0.01)
    return  n*2

@Timing(duration=0.2)
def slow(n):
    print("начало")
    time.sleep(n)
    return "готово"

res1 = fast(10)
print(res1)




print(time.time())
print(time.perf_counter())
print(time.localtime(time.time()))