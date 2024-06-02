import allure

from data.get_orders import GetOrder


class TestAddOrderLogin:

    @allure.title('Создание заказа')
    @allure.description('Создание заказа с авторизацией и ингридиентами')
    def test_add_order_login(self):

        order = GetOrder()
        response = order.add_order_login()
        assert response.status_code == 200
        assert response.json()['success'] == True

    @allure.title('Создание заказа')
    @allure.description("Создание заказа без авторизации")
    def test_order_without_login(self):

        order = GetOrder()
        response = order.add_order_logout()
        assert response.status_code == 200
        assert response.json()['success'] == True

    @allure.title('Создание заказа')
    @allure.description('Создание заказа без ингридиентов')
    def test_order_without_ingridients(self):

        order = GetOrder()
        response = order.add_order_without_ingridients()
        assert response.status_code == 400
        assert response.json()['success'] == False

    @allure.title('Создание заказа')
    @allure.description('Создание заказа с неверным хешем ингридиетов')
    def test_order_error_ingridients(self):
        order = GetOrder()
        response = order.add_order_error_ingridients()
        assert response.status_code == 500




