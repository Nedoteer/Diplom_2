import allure
import requests

from Urls import Urls
from data.data_for_test import DataForTest
from metods.login_user import LoginUser


class GetOrder:


    @allure.step('Создание заказа с авторизацией и ингридиентами')
    def add_order_login(self):

        login = LoginUser()
        response = login.login_user()
        ingridients = DataForTest.ingridients

        order = requests.post(Urls.url_https + Urls.url_order, json=ingridients,
                              headers={'Authorization': response.json()['accessToken']})

        return order


    @allure.step('Создание заказа без авторизации')
    def add_order_logout(self):

        ingridients = DataForTest.ingridients

        order = requests.post(Urls.url_https + Urls.url_order, json=ingridients)

        return order


    @allure.step('Создание заказа без ингридиентов')
    def add_order_without_ingridients(self):

        login = LoginUser()
        response = login.login_user()
        ingridients = {
            "ingredients": []
        }

        order = requests.post(Urls.url_https + Urls.url_order, json=ingridients,
                              headers={'Authorization': response.json()['accessToken']})
        return order

    @allure.step('Создание заказа с неверным хешем ингридиентов')
    def add_order_error_ingridients(self):

        login = LoginUser()
        response = login.login_user()
        ingridients = {
            "ingredients": 'iuytre'
        }

        order = requests.post(Urls.url_https + Urls.url_order, json=ingridients,
                              headers={'Authorization': response.json()['accessToken']})
        return order


