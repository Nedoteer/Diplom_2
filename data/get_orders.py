import allure
import requests

from Urls import Urls
from data.login_user import LoginUser


class GetOrder:


    @allure.title('Создание заказа с авторизацией и ингридиентами')
    def add_order_login(self):

        login = LoginUser()
        response = login.login_user()
        ingridients = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
        }

        order = requests.post(Urls.URL_HTTPS + Urls.URL_ORDER, json=ingridients,
                      headers={'Authorization': response.json()['accessToken']})

        return order


    @allure.title('Создание заказа без авторизации')
    def add_order_logout(self):

        ingridients = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
        }

        order = requests.post(Urls.URL_HTTPS + Urls.URL_ORDER, json=ingridients)

        return order


    @allure.title('Создание заказа без ингридиентов')
    def add_order_without_ingridients(self):

        login = LoginUser()
        response = login.login_user()
        ingridients = {
            "ingredients": []
        }

        order = requests.post(Urls.URL_HTTPS + Urls.URL_ORDER, json=ingridients,
                      headers={'Authorization': response.json()['accessToken']})
        return order

    @allure.title('Создание заказа с неверным хешем ингридиентов')
    def add_order_error_ingridients(self):

        login = LoginUser()
        response = login.login_user()
        ingridients = {
            "ingredients": ["60d3b41abdacab0026a732c6", "609646e4dc916e00276b2870", "609646e4dc916e00276b2871"]
        }

        order = requests.post(Urls.URL_HTTPS + Urls.URL_ORDER, json=ingridients,
                      headers={'Authorization': response.json()['accessToken']})
        return order


