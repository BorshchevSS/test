import xml.etree.ElementTree as ET
import pandas as pd
import shutil

tree = ET.parse('TST_толькоВетви.xml')
root = tree.getroot()

exel_data = pd.read_excel('key_DispName.xlsx', sheet_name='Лист1')
# словарь из excel для более быстрого поиска
disp_name_dict = dict(
    zip(exel_data['key'], exel_data['DispName']))  # преобразование две колонки в словарь: ключ -> значение


source = 'TST_толькоВетви.xml'
destination = f'backup_{source}'
shutil.copy(source, destination)
print(f"Создана резервная копия: {destination}")

# основной алгоритм обработки
lines_element = root[0][0]  # получение элемента <LINES>...</LINES> по вложенности
updated_count = 0

# здесь начинается перебор всех элементов <LINE> внутри элемента <LINES>
for line_elem in lines_element:  # каждый элемент <LINE>
    # формируется ключ для поиска в словаре на основе атрибутов из xml
    node_beg = line_elem.get("NODE_BEG")
    node_end = line_elem.get("NODE_END")
    current_key = f"{node_beg}_{node_end}"

    # поиск ключа из словаря excel
    new_disp_name = disp_name_dict.get(current_key)  # пытаемся получить значение по ключу, будет возвращать none если ключ не найден

    # проверяем найден ли ключ в словаре
    if new_disp_name is not None:  # если найден
        # если ключ найден, обновляем атрибут 'DISP_NAME_OIK'
        old_name = line_elem.get("DISP_NAME_OIK",
                                 "Атрибут отсутствовал")  # получаем старое значение атрибута или текст по умолчанию
        line_elem.set("DISP_NAME_OIK", new_disp_name)  # устанавливаем новое значение атрибута
        print(
            f"Обновлено: {current_key}. Было: '{old_name}'. Стало: '{new_disp_name}'")
        updated_count += 1

# сохранение дерева обратно
output_filename = 'new_TST_толькоВетви.xml'  # имя выходного файла
tree.write(output_filename, encoding='windows-1251')
print(f"\nОбновлено записей: {updated_count}. Сохранен в {output_filename}")