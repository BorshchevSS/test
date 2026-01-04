import queue
import threading
import os

def process_file(q, result, lock):
    '''для обработки файла'''
    while not q.empty():
        file_path = q.get()
        try:
            if not os.path.exists(file_path):
                print(f'file not found: {file_path}')
                q.task_done()
                continue

            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                line_count = len(lines)
            with lock:
                result['total_lines'] += line_count
                result['file_res'][file_path] = line_count
            print(f'processed {file_path}: {line_count}')
        except Exception as e:
            print(f'error processing file {file_path}: {e}')
        finally:
            q.task_done()

def main():
    file_path = ['f1.txt', 'f2.txt', 'f3.txt']
    task_queue = queue.Queue()
    for path in file_path:
        task_queue.put(path)
    result = {'total_lines': 0,
              'file_res': {}
              }
    res_lock = threading.Lock()
    num = 3
    threads = [
        threading.Thread(target=process_file,
                         args=(task_queue, result, res_lock))
        for _ in range(num)
    ]
    for t in threads:
        t.start()
    task_queue.join()
    for file, count in result['file_res'].items():
        print(f'{file}: {count}')
    print(f'total: {result['total_lines']}')

if __name__ == '__main__':
    main()