import requests
r = requests.get("https://www.gosuslugi.ru")
r = r.text
print(r)