"""Методы для проверки ответов запросов"""

from requests import Response
import json

class Checking():

    """Метод для проверки статус кода"""

    @staticmethod
    def check_status_code(response: Response, status_code):
        if status_code == response.status_code:
            print("Успешно! Статус код = " + str(response.status_code))
        else:
            print("Провал! Статус код = " + str(response.status_code))
        assert status_code == response.status_code, 'Статус код не совпадает с status_code'

    """Метод для проверки наличия полей в ответе запроса"""

    @staticmethod
    def check_json_fields(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")

    """Метод для проверки значения обязательных полей в ответе запроса"""

    @staticmethod
    def check_json_values(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " верен!")
