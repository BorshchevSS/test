# from collections import deque, Counter
#
# # LIFO (последний пришел первым ушел)
# #
# # FIFO (первым пришел первм ушел)
#
# # d = deque([1, 2, 3])
# # # append(value)
# # # appendleft(value)
# # d.append(4)
# # d.appendleft(0)
# # print(d)
# #
# # # pop()
# # # popleft()
# # print(d.pop())
# # print(d)
# # print(d.popleft())
# # print(d)
# # print(d[0])
# #
# # d = deque(maxlen=3)
# # d.append(1)
# # d.append(2)
# # d.append(3)
# # print(d)
# # d.append(4)
# # print(d)
# # print(d[0])
# # d.rotate(-5)
# # print(d)
# #
# # O(1)
# # O(n)
# # O(n^2)
# # from collections import Counter
# # c = Counter([1, 2, 2, 3, 3, 3])
# # print(c)
# # s = Counter('abracadabra')
# # print(s)
# # d = Counter({'a': 2, 'b': 1})
# # print(d)
#
# # data = ['a', 'b', 'a', 'a', 'c', 'b']
# # c = Counter(data)
# # print(c.most_common(2))
# # c.update(['c', 'f'])
# # print(c)
#
#
#
#
#
#
# from collections import defaultdict
#
# dd = defaultdict(list) #для группировки данных
# dd['a'].append(1)
# dd['b'].append(2)
# dd['a'].append(3)
# print(dd)
#
# dd1 = defaultdict(int) #для подсчета элементов
# data = ['apple', 'banana', 'apple',
#         'banana', 'orange', 'banana']
# for fruit in data:
#     dd1[fruit] += 1
# print(dd1)
#
# def default_value(): #только функции без аргументов
#     return 'значение по умолчанию'
#
# dd2 = defaultdict(default_value)
# print(dd2['key'])
#
# data1 = [('a', 1), ('b', 2), ('a', 3), ('b', 2)]
# grouped = defaultdict(list)
# for key, value in data1:
#     grouped[key].append(value)
# print(grouped)

from collections import Counter
counter = Counter({'a': 2, 'b': 1})
print(counter)







