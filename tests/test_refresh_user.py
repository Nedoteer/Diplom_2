import allure

from Urls import Urls
from data.login_user import LoginUser

import requests

from data.refresh_user import RefreshUser


class TestRefreshUser:

    @allure.title('Изменение данных пользователя')
    @allure.description('Изменение данных авторизированного пользователя')
    def test_refresh_user_auth(self):

        payload = {
                   "password": "pass1"
                   }
        login = LoginUser()
        response = login.login_user()
        result = requests.patch(Urls.URL_HTTPS + Urls.URL_AUTH_USER,
                                headers={'Authorization': response.json()['accessToken']}, json=payload)
        assert result.status_code == 200
        assert result.json()['success'] == True

    @allure.title('Изменение данных пользователя')
    @allure.description('Изменение данных не авторизированного пользователя')
    def test_refresh_user_not_auth(self):

        payload = {
            "password": "pass1"
            }
        auth = RefreshUser()
        response = auth.refresh_user_not_auth()
        exittoken = {
            "token": response.json()['refreshToken']
        }
        requests.post(Urls.URL_HTTPS + Urls.URL_AUTH_LOGOUT, json=exittoken)
        result = requests.patch(Urls.URL_HTTPS + Urls.URL_AUTH_USER,
                                headers={'Authorization': None}, json=payload)
        assert result.json()['success'] == False
        assert result.status_code == 401


