import pandas as pd
#key_Name.xlsx
#key_DispName.xlsx
exel = pd.read_excel('key_DispName.xlsx', sheet_name='Лист1')

column = exel.shape[1]
row = exel.shape[0]
tupleColumn = exel.columns.tolist() #Кортеж с заготовками столбцов

for i in range(row):
    print(f"{exel[tupleColumn[0]][i]}_{exel[tupleColumn[1]][i]}")
