import re

# re.search (pattern, text)  - первое совпадение
# re.findall (pattern, text)  - все совпадения возвращает (в виде списка)
# re.sub(pattern, replacement, text)  - заменяет

s = "Сегодня 25 апреля 2023 года"
pattern = r"\d+"
matches = re.findall(pattern, s)
print(matches)

text = "Мой телеграмм - @username. Но лучше свяжитесь со мной по email: гыук@example.com или support@domain.org"
# pattern_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
"""^: Начало строки.
[a-zA-Z0-9._%+-]+: Одна или несколько букв (верхний и нижний регистр), цифр или специальных символов (., _, %, +, -) в локальной части адреса.
@: Символ "собака".
[a-zA-Z0-9.-]+: Одна или несколько букв (верхний и нижний регистр), цифр, точек или дефисов в доменной части.
\.: Точка перед доменной зоной верхнего уровня (TLD).
[a-zA-Z]{2,}: Минимум две буквы верхнего или нижнего регистра в доменной зоне верхнего уровня (например, .com, .org).
$: Конец строки. """
pattern_email = r'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}'

matches_mail = re.findall(pattern_email, text)
print(matches_mail)