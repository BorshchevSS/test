import xml.etree.ElementTree as ET # Загружаем библиотеку
import pandas as pd
import shutil

tree = ET.parse('TST_толькоВетви.xml') #дерево. метод parse() принимает путь к XML-файлу в качестве параметра и возвращает объект ElementTree, который представляет проанализированные данные.
root = tree.getroot() #Получение корневого элемента

# for i in range(len(root[0][0])):
#     print(f"{root[0][0][i].get("NODE_BEG")}_{root[0][0][i].get("NODE_END")}_name: {root[0][0][i].get("NAME")}_DN: {root[0][0][i].get("DISP_NAME_OIK")}")

#______
#key_Name.xlsx
#key_DispName.xlsx
exel = pd.read_excel('key_DispName.xlsx', sheet_name='Лист1')

column = exel.shape[1]
row = exel.shape[0]
tupleColumn = exel.columns.tolist() #Кортеж с заготовками столбцов

# for i in range(row):
#     print(f"{exel[tupleColumn[0]][i]}_{exel[tupleColumn[1]][i]}")

#Создание резервной копии файла xml
source = 'TST_толькоВетви.xml'
destination = f'new_{source}'
shutil.copy(source, destination)

# Основной алгоритм
for i in range(len(root[0][0])): #Перебор в xml
    #print(f"{root[0][0][i].get("NODE_BEG")}_{root[0][0][i].get("NODE_END")}_name: {root[0][0][i].get("NAME")}_DN: {root[0][0][i].get("DISP_NAME_OIK")}")
    nodeXML_BEG_END = f"{root[0][0][i].get("NODE_BEG")}_{root[0][0][i].get("NODE_END")}"
    #print(nodeXML_BEG_END)
    for j in range(row): #Перебор в xcel
        #print(f"{exel[tupleColumn[0]][i]}_{exel[tupleColumn[1]][i]}")
        nodeXLSX_BEG_END = exel[tupleColumn[0]][j]
        #print(f"i={nodeXML_BEG_END} j={nodeXLSX_BEG_END}")
        if nodeXML_BEG_END == nodeXLSX_BEG_END:
            print(f"i={nodeXML_BEG_END} j={nodeXLSX_BEG_END}__{root[0][0][i].get("DISP_NAME_OIK")}")
            print(f"i={nodeXML_BEG_END} j={nodeXLSX_BEG_END}")
            # test_2 = ET.SubElement(root[0][0][i], 'DISP_NAME_OIK')
            # test_2.text = "Еуые"
            # print(root[0][0][i])
            # print(root[0][0][i].text)
            #print(f"i={nodeXML_BEG_END} j={nodeXLSX_BEG_END}__{root[0][0][i].get("DISP_NAME_OIK")}")



