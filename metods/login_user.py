import allure
import requests

from Urls import Urls
from metods.add_user import AddUser


class LoginUser:

    @allure.step('Данные для входа под существующим пользователем')
    def login_user(self):

        us = AddUser.generate_random_string(5)
        payload = {"email": f'{us}@yopmail.com',
                   "password": "password",
                   "name": "Username"
                   }
        login = {
            "email": f'{us}@yopmail.com',
            "password": "password"
        }
        requests.post(Urls.url_https + Urls.url_register, json=payload)
        response = requests.post(Urls.url_https + Urls.url_auth_login, json=login)
        return response

    @allure.step('Данные для входа под не существующим пользователем')
    def login_error(self):

        login = {
            "email": f'{AddUser.generate_random_string(5)}@yopmail.com',
            "password": "password"
        }
        response = requests.post(Urls.url_https + Urls.url_auth_login, json=login)
        return response
