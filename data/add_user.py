import random
import string

import allure


class AddUser:

    @staticmethod
    @allure.title('Создание случайных комбинаций логина и пароля')
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string