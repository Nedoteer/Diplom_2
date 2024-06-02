import allure
import requests

from Urls import Urls
from data.add_user import AddUser


class RefreshUser:

    @allure.title('Изменение данных пользователя')
    def refresh_user_not_auth(self):
        us = AddUser.generate_random_string(5)
        payload = {"email": f'{us}@yopmail.com',
                   "password": "password",
                   "name": "Username"
                   }
        login = {
            "email": f'{us}@yopmail.com',
            "password": "password"
        }
        requests.post(Urls.URL_HTTPS + Urls.URL_REGISTER, json=payload)
        result = requests.post(Urls.URL_HTTPS + Urls.URL_AUTH_LOGIN, json=login)

        return result