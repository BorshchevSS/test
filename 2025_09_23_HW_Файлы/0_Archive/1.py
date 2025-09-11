import random
import datetime

def get_random_quote():
    try:
        with open('quotes.txt', 'r', encoding='utf-8') as f:
            quotes = f.readlines()
        if quotes:
            return random.choice(quotes)
        return 'файл пустой'

    except FileNotFoundError:
        return 'Файл не найден'

def save_quote_of_the_day():
    quote = get_random_quote()
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('quotes_of_the_day.txt', 'w', encoding='utf8') as f:
        f.write(f'{current_time}')
        f.write('\n')
        f.write(quote)
    return 'цитата сохранена'

print(get_random_quote())
print(save_quote_of_the_day())

# print(datetime.datetime.now())