import requests
import allure

json_for_create_new_token = {
        "username": "admin",
        "password": "password123"
    }
post_url_for_token = "https://restful-booker.herokuapp.com/auth"
result_post_for_token = requests.post(post_url_for_token, json_for_create_new_token)
check_token = result_post_for_token.json()
tokens = check_token.get("token")

"""Список HTTP методов"""

class Http_methods():

    headers = {'Content-Type': 'application/json',
               'Cookie': 'token=' + tokens}

    @staticmethod
    def get(url):
        with allure.step("GET"):
            result = requests.get(url, headers=Http_methods.headers)
            return result

    @staticmethod
    def post(url, body):
        with allure.step("POST"):
            result = requests.post(url, json=body, headers=Http_methods.headers)
            return result

    @staticmethod
    def put(url, body):
        with allure.step("PUT"):
            result = requests.put(url, json=body, headers=Http_methods.headers)
            return result

    @staticmethod
    def patch(url, body):
        with allure.step("PATCH"):
            result = requests.patch(url, json=body, headers=Http_methods.headers)
            return result


    @staticmethod
    def delete(url):
        with allure.step("DELETE"):
            result = requests.delete(url, headers=Http_methods.headers)
            return result