# set1 = {1, 5, 6, 5, 6, 8, 9}
# set2 = set()
# print(set1)
# # print(set1[4])
# for i in set1:
#     print(i)
#
# set3 = {1 ,2 , 3, 4, 5}
# set4 = {4, 5, 6, 7, 8}
# print(set3.union(set4)) #объединение
# print(set3.intersection(set4))#пересечение
# print(set3.difference(set4))#разность
# print(set4.difference(set3))#разность
# print(set3.symmetric_difference(set4))#симметричная разность
# print(set3 | set4) #union
# print(set3 & set4) #intersection
# print(set3 - set4) #difference
# print(set3 ^ set4) #symmetric_difference

a = {1, 2, 3, 4}
a.add(5)
print(a)
# a.remove(8)
a.discard(8)
print(a)
# a.clear()
a_copy = a.copy()
print(id(a))
print(id(a_copy))
for i in a_copy:
    a.add(9)

b = {1, 2}
c = {1, 2, 3, 4, 5}
print(b.issubset(c)) #подмножество
print(c.issubset(b))
print(c <= b)
print(c.issuperset(b)) #надмножество
print(b.issuperset(c))
print(c >= b)
d = {2, 1}
print(b == d)
e = {1, 2, (1, 2)}
v = {[4, 6], 7, 8}
