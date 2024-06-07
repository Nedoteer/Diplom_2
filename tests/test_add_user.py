import allure
import requests

from data.data_for_test import DataForTest
from metods.add_user import AddUser
from Urls import Urls


class TestAddUser:


    @allure.title("Создание пользователя")
    @allure.description('Создание уникального пользователя')
    def test_add_user(self):

        payload = {"email": f'{AddUser.generate_random_string(5)}@yopmail.com',
                   "password": "password",
                   "name": "Username"
                   }
        response = requests.post(Urls.url_https + Urls.url_register, json=payload)
        assert response.json()['success'] == True
        assert response.status_code == 200

    @allure.title('Создание пользователя')
    @allure.description('Создание пользователя который уже зарегестрирован')
    def test_already_registered_user(self):
        payload = {"email": f'{AddUser.generate_random_string(5)}@yopmail.com',
                   "password": "password",
                   "name": "Username"
                   }
        copy = payload
        requests.post(Urls.url_https + Urls.url_register, json=payload)
        response = requests.post(Urls.url_https + Urls.url_register, json=copy)
        assert response.json()['success'] == False
        assert response.status_code == 403

    @allure.title('Создание пользователя')
    @allure.description('Создание пользователя и не заполнить email')
    def test_add_user_without_email(self):
        payload = DataForTest.name_password
        response = requests.post(Urls.url_https + Urls.url_register, json=payload)
        assert response.status_code == 403
        assert response.json()['message'] == 'Email, password and name are required fields'