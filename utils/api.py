from utils.http_methods import Http_methods

base_url = "https://restful-booker.herokuapp.com"
books = "/booking"
auth = "/auth"

"""Методы для тестирования Books api"""

class Books_api():

    """Метод для создания токена"""

    @staticmethod
    def create_new_token():
        json_for_create_new_token = {
            "username": "admin",
            "password": "password123"
        }
        post_url_for_token = base_url + auth
        print(post_url_for_token)
        result_post_for_token = Http_methods.post(post_url_for_token, json_for_create_new_token)
        print(result_post_for_token.text)
        return result_post_for_token

    """Метод для создания новой книги"""

    @staticmethod
    def create_new_book():
        json_for_create_new_book = {
            "firstname": "Pop",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": "",
            "bookingdates": {
                "checkin": "2020-01-01",
                "checkout": "2021-01-01"
            },
            "additionalneeds": "Breakfast"
        }

        post_url = base_url + books
        print(post_url)
        result_post = Http_methods.post(post_url, json_for_create_new_book)
        print(result_post.text)
        return result_post

    """Метод для проверки новой или измененной книги"""

    @staticmethod
    def check_new_book(id):
        get_url = base_url + books + "/" + str(id)
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    """Метод для изменения книги"""

    @staticmethod
    def put_new_book(id):
        json_for_put_new_book = {
            "firstname": "Ol",
            "lastname": "Gree",
            "totalprice": 111,
            "depositpaid": "",
            "bookingdates": {
                "checkin": "2021-01-01",
                "checkout": "2023-01-01"
            },
            "additionalneeds": "Breakfast"
        }
        put_url = base_url + books + "/" + str(id)
        print(put_url)
        result_put = Http_methods.put(put_url, json_for_put_new_book)
        print(result_put.text)
        return result_put

    """Метод для частичного изменения книги"""

    @staticmethod
    def patch_new_book(id):
        json_for_patch_new_book = {
            "firstname": "Olga",
            "lastname": "Black"
        }
        patch_url = base_url + books + "/" + str(id)
        print(patch_url)
        result_patch = Http_methods.patch(patch_url, json_for_patch_new_book)
        print(result_patch.text)
        return result_patch

    """Метод для удаления книги"""

    @staticmethod
    def delete_new_book(id):
        delete_url = base_url + books + "/" + str(id)
        print(delete_url)
        result_delete = Http_methods.delete(delete_url)
        print(result_delete.text)
        return result_delete








