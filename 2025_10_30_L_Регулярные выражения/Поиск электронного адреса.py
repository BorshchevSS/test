import re

text = "Напишите мне по адресу: example@example.com или support.user@domain.co.uk. А также contact+alias@email.org."
regex = r'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}'

emails = re.findall(regex, text)
print(emails)