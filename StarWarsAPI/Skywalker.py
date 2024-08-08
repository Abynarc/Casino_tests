import requests

url = "https://swapi.dev/api/people/1/"
print(url)

result = requests.get(url)
print('Статус код: ' + str(result.status_code))

assert 200 == result.status_code
if result.status_code == 200:
    print ('Успешно. Статус код равен 200')
else:
    print('Ошибка. Статус код не равен 200')

check = result.json()
check_name = check.get("name")
assert check_name == "Luke Skywalker"
print('Люк Скайуокер распознан')

result.encoding = 'utf-8'
print(result.text)