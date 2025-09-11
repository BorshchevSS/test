student = []

while True:
    choice = input('''
    1. добавить студента
    2. показать статистику
    3. выйти
    ''')

    if choice == '1':
        name = input('имя:')
        age = int(input('возраст:'))
        subjects_input = input('любимые предметы:')
        subject = [ch.strip() for ch in subjects_input.split()]