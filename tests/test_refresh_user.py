import allure

from Urls import Urls
from data.data_for_test import DataForTest
from metods.login_user import LoginUser

import requests




class TestRefreshUser:

    @allure.title('Изменение данных пользователя')
    @allure.description('Изменение данных авторизированного пользователя')
    def test_refresh_user_auth(self):

        payload = DataForTest.payload
        login = LoginUser()
        response = login.login_user()
        result = requests.patch(Urls.url_https + Urls.url_auth_user,
                                headers={'Authorization': response.json()['accessToken']}, json=payload)
        assert result.status_code == 200
        assert result.json()['success'] == True

    @allure.title('Изменение данных пользователя')
    @allure.description('Изменение данных не авторизированного пользователя')
    def test_refresh_user_not_auth(self):

        payload = DataForTest.payload
        auth = LoginUser()
        response = auth.login_user()
        exittoken = {
            "token": response.json()['refreshToken']
        }
        requests.post(Urls.url_https + Urls.url_auth_logout, json=exittoken)
        result = requests.patch(Urls.url_https + Urls.url_auth_user,
                                headers={'Authorization': None}, json=payload)
        assert result.json()['success'] == False
        assert result.status_code == 401


