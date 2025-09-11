# file = open('text.txt')
# file.close()
# with open('book.txt', 'r', encoding='utf-8') as f:
# #     r - ошибка если не найден
# #     w - перезапись - создает файл
# #     a - дозапись   - создает файл
# # rb, wb, ab
# #     content = f.read()
# # print(content)
# #     for line in f:
# #         print(line.strip())
# #     print(f.readline())
# #     print(f.readline())
#         print(f.readlines())

with open('text.txt', 'w', encoding='utf-8') as f:
    f.write('hello\n')
    f.write('seal')

