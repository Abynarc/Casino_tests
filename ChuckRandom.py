import requests

class TestNewJoke:
    def test_create_new_random_joke(self):
        # Создание случайной шутки
        url = "https://api.chucknorris.io/jokes/random"
        print(url)
        result = requests.get(url)
        print('Статус код: ' + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print('Успешно. Статус код равен 200')
        else:
            print('Ошибка. Статус код не равен 200')
        result.encoding = 'utf-8'
        print(result.text)


random_joke = TestNewJoke()
random_joke.test_create_new_random_joke()