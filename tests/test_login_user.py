import allure

from metods.login_user import LoginUser


class TestLoginUser:

    @allure.title('Логин пользователя')
    @allure.description('Вход под существующим пользователем')
    def test_login_user(self):

        login = LoginUser()
        response = login.login_user()
        assert response.json()['success'] == True

    @allure.title('Логин пользователя')
    @allure.description('Вход под не существующим пользователем')
    def test_not_correct_login_and_password(self):

        login = LoginUser()
        response = login.login_error()
        assert response.json()['message'] == 'email or password are incorrect'
        assert response.status_code == 401