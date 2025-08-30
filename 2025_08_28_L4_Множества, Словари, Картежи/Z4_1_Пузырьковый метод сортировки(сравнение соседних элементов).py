text = "Привет, мир! Мир, мир прекрасен, привет всем."
text = text.lower()
#print(text)

#Замена символов на пустоту
for char in ".,!!@#$%^&*{}[]()":
    text = text.replace(char, "")


words = text.split()
#print(words)
count_words = {}
for word in words:
    if word in count_words:
        count_words[word] += 1
    else:
        count_words[word] = 1

#Пузырьковый метод (сравнение соседних элементов и ...
items = list(count_words.items())
n = len(items) # длина списка
# [("a",2), ("b", 1), ("c", 3)]
for i in range(n):   # i - номер текущей операции
    # i = items[i] = ("a",2)
    for j in range(0, n-i-1): #j - индекс картежа;
        # items[j][1] = 2
        if items[j][1] < items[j+1][1]:
            # Сравниваем по количеству и меняем местами если условие верное
            items[j], items[j+1] = items[j+1], items[j]
        print(f"j={j}, i={i}(номер текущей операции), items[j]={items[j]}, items[j][1]={items[j][1]}")

for word, count in items[:5]:
    print(f"{word}: {count}")