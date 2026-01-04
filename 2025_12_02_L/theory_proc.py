# Process
# GIL (global interpreter lock)
from multiprocessing import Process
import time
from queue import Queue


def hey():
    print('hello from process')
    time.sleep(5)
    print('process end')

# if __name__ == '__main__':
#     process = Process(target=hey)
#     process.start()
#     time.sleep(2)
#     if process.is_alive():
#         print('все еще работает. прерываем')
#         process.terminate()
#     process.join()
#     print('process *end*')

# is_alive() - проверяет работает лм п в данный момент времени
# terminate() - принудительно завершает

# Queue FIFO (first in, first out)

from multiprocessing import Process, Queue
import time

def procedure(queue):
    for i in range(5):
        print(i)
        queue.put(i)
        time.sleep(1)

def consumer(queue):
    while True:
        item = queue.get()
        if item == 'DONE':
            break
        print(f'consumer {item}')

# if __name__ == '__main__':
#     queue = Queue()
#     p_process = Process(target=procedure, args=(queue,))
#     c_process = Process(target=consumer, args=(queue,))
#     p_process.start()
#     c_process.start()
#     p_process.join()
#     queue.put('DONE')
#     c_process.join()
#     print('done')

# Pipe на основе связи между двумя процессами

from multiprocessing import Process, Pipe
import time

def sender(conn):
    for i in range(5):
        conn.send(i) #отправляем данные через канал
        time.sleep(1)

def receiver(conn):
    while True:
        data = conn.recv()
        if data == 'done':
            break
        print(f'получатель получил {data}')

# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()
#
#     s_p = Process(target=sender, args=(parent_conn,))
#     r_p = Process(target=receiver, args=(child_conn,))
#     s_p.start()
#     r_p.start()
#     s_p.join()
#     parent_conn.send('done')
#     r_p.join()
#     print('end')

from multiprocessing import Process, Queue
import time

def square(n, queue):
    res = n ** 2
    print(res)
    queue.put(res)
    time.sleep(1)

if __name__ == '__main__':
    queue = Queue()
    processes = []
    for i in range(1, 4):
        process = Process(target=square, args=(i, queue))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()

    while not queue.empty():
        res = queue.get()
        print(f'res={res}')
    print('done')