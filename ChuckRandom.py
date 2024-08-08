import requests

class Test_new_joke():
# Создание новой шутки - класс
    def __init__(self):
        pass

    def test_create_new_random_joke(self):
        # Создание случайной шутки
        url = "https://api.chucknorris.io/jokes/random"
        # Вводим переменную URL
        print(url)
        # Выводим на печать эту URL
        result = requests.get(url)
        print('Статус код: ' + str(result.status_code))
        # Вывод статус кода
        assert 200 == result.status_code
        # Сравниваем наш полученный статус код со значением 200
        if result.status_code == 200:
            print('Успешно. Статус код равен 200')
        else:
            print('Ошибка. Статус код не равен 200')
        result.encoding = 'utf-8'
        # Ответ должен быть в кодирвке utf-8
        print(result.text)

random_joke = Test_new_joke()
random_joke.test_create_new_random_joke()