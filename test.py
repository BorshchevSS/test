import requests

t = requests.get("https://www.gosuslugi.ru/")
t = t.text
print(t)