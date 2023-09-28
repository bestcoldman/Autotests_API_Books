from requests import Response
from utils.api import Books_api
from utils.cheking import Checking
import allure

"""Создание,изменение и удаление новой книги"""

@allure.epic("Test create new book")
class Test_books():

    @allure.description("Test create, update and delete book")
    def test_create_new_book(self):

        print("Метод POST FOR TOKEN")
        result_post_for_token: Response = Books_api.create_new_token()
        Checking.check_status_code(result_post_for_token, 200)
        Checking.check_json_fields(result_post_for_token, ['token'])
        # Значение поля 'token' при отправке запроса каждый раз новое

        print("Метод POST FOR CREATE NEW BOOK")
        result_post: Response = Books_api.create_new_book()
        check_id = result_post.json()
        id = check_id.get("bookingid")
        Checking.check_status_code(result_post, 200)
        Checking.check_json_fields(result_post, ['bookingid', 'booking'])
        Checking.check_json_values(result_post, 'bookingid', id)

        print("Метод GET AN EXISTING BOOK TO CHECK")
        result_get: Response = Books_api.check_new_book(id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_fields(result_get, ['firstname', 'lastname', 'totalprice', 'depositpaid',
                                                'bookingdates', 'additionalneeds'])
        Checking.check_json_values(result_get, 'firstname', 'Pop')


        print("МЕТОД PUT")
        result_put: Response = Books_api.put_new_book(id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_fields(result_put, ['firstname', 'lastname', 'totalprice', 'depositpaid',
                                                'bookingdates', 'additionalneeds'])
        Checking.check_json_values(result_put, 'firstname', 'Ol')

        print("Метод GET AN EXISTING BOOK AFTER PUT")
        result_get: Response = Books_api.check_new_book(id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_fields(result_get, ['firstname', 'lastname', 'totalprice', 'depositpaid',
                                                'bookingdates', 'additionalneeds'])
        Checking.check_json_values(result_get, 'firstname', 'Ol')

        print("Метод PATCH")
        result_patch: Response = Books_api.patch_new_book(id)
        Checking.check_status_code(result_patch, 200)
        Checking.check_json_fields(result_patch, ['firstname', 'lastname', 'totalprice', 'depositpaid',
                                                  'bookingdates', 'additionalneeds'])
        Checking.check_json_values(result_patch, 'lastname', 'Black')


        print("Метод GET AN EXISTING BOOK AFTER PATCH")
        result_get: Response = Books_api.check_new_book(id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_fields(result_get, ['firstname', 'lastname', 'totalprice', 'depositpaid',
                                                'bookingdates', 'additionalneeds'])
        Checking.check_json_values(result_get, 'lastname', 'Black')

        print("Метод DELETE")
        result_delete: Response = Books_api.delete_new_book(id)
        Checking.check_status_code(result_delete, 201)
        # В методе Delete отсутствуют поля в Response

        print("Метод GET AN EXISTING BOOK AFTER DELETE")
        result_get: Response = Books_api.check_new_book(id)
        Checking.check_status_code(result_get, 404)





