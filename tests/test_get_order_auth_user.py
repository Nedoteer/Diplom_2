import allure
import requests

from Urls import Urls
from data.data_for_test import DataForTest
from metods.login_user import LoginUser


class TestGetOrderAuthUser:

    @allure.title('Получение заказа конкретного пользователя')
    @allure.description('Получение заказа авторизированного пользователя')
    def test_get_order_auth_user(self):

        auth_user = LoginUser()
        auth = auth_user.login_user()

        ingridients = DataForTest.ingridients

        requests.post(Urls.url_https + Urls.url_order, json=ingridients,
                      headers={'Authorization': auth.json()['accessToken']})

        user_order =  requests.get(Urls.url_https + Urls.url_order, headers={"Authorization": auth.json()['accessToken']})
        assert user_order.json()['orders'][0]['status'] == 'done'
        assert user_order.json()['success'] == True

    @allure.title('Получение заказа конкретного пользователя')
    @allure.description('Получение заказа не авторизированного пользователя')
    def test_get_order_not_auth_user(self):
        auth_user = LoginUser()
        auth = auth_user.login_user()

        ingridients = DataForTest.ingridients

        requests.post(Urls.url_https + Urls.url_order, json=ingridients,
                      headers={'Authorization': auth.json()['accessToken']})

        user_order = requests.get(Urls.url_https + Urls.url_order)
        assert user_order.json()['message'] == 'You should be authorised'
        assert user_order.json()['success'] == False