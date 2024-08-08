import requests

url = 'https://swapi.dev/api/people/1/'
print(url)

result = requests.get(url)
print('Статус код: ' + str(result.status_code))
assert result.status_code == 200
if result.status_code == 200:
    print('Статус код реально 200')
else:
    print('Вышла ошибочка со статусом кода')

check = result.json()
check_name = check.get("name")
# assert check_name == "C-3PO"
if check_name == "C-3PO":
    print('Это действительно С3РО')
else:
    print('Ха, это не С3РО')

result.encoding = 'utf-8'
print(result.text)