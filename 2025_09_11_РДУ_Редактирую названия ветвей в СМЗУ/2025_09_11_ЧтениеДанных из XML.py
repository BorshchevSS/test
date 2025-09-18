import xml.etree.ElementTree as ET # Загружаем библиотеку
# https://habr.com/ru/articles/757180/
# ET.dump(tree) # Посмотрим содержимое xml
tree = ET.parse('TST_толькоВетви.xml') #дерево. метод parse() принимает путь к XML-файлу в качестве параметра и возвращает объект ElementTree, который представляет проанализированные данные.
root = tree.getroot() #Получение корневого элемента

# print(root.iter())
#Обход элементов:
for elem in root.iter():
    pass
    #print(elem.tag, elem.attrib)  # Выведет название и атрибуты каждого элемента в дереве
    # print(root.iter())
    #print(elem.attrib[elem][["NODE_BEG"]])
print(root)
print(root[0])
print(root[0][0])
print(root[0][0][0])
print(root[0][0][0].text)
print(root[0][0][0].get("NODE_BEG"))
print(len(root[0][0]))

for i in range(len(root[0][0])):
    # print(i)
    # print(root[0][0][i].get("NODE_BEG"))
    print(f"{root[0][0][i].get("NODE_BEG")}_{root[0][0][i].get("NODE_END")}_name: {root[0][0][i].get("NAME")}_DN: {root[0][0][i].get("DISP_NAME_OIK")}")

    root[0][0][i].text = "tesT"
    print(f"{root[0][0][i].get("NODE_BEG")}_{root[0][0][i].get("NODE_END")}_name: {root[0][0][i].get("NAME")}_DN: {root[0][0][i].get("DISP_NAME_OIK")}")
