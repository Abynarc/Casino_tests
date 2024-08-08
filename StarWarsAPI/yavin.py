import requests

url = 'https://swapi.dev/api/planets/3/'
print(url)

result = requests.get(url)
print('Статус код: ' + str(result.status_code))
assert result.status_code == 200
if result.status_code == 200:
    print('Статус код равен 200')
else:
    print('Статус код не равен 200')

check = result.json()
check_name = check.get("name")
if check_name == "Yavin IV":
    print('Планета Явин 3')
else:
    print('Планета не Явин 3')

print(result.text)