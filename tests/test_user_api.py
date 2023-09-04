import pytest
from api_store.petstore import ApiPetStore
from api_store.user import User
from helpers.user import UserJSON

import allure


@allure.epic("Тесты к эндпоинтам User")
class TestUserApi:

    user = User()

    @allure.story('Создание нового пользователя')
    def test_create_user(self):
        new_user = UserJSON.new_user()
        response = self.user.create_user(new_user)
        ApiPetStore.LOGGER.info(f"Код ответа - {response.status_code},тело ответа {response.json()}")

        with allure.step(f"HTTP статус код ответа ={response.status_code}"):
            assert response.status_code == 200, f'Фактический статус код {response.status_code}'
        with allure.step(f"Код ответа в теле ответа {response.json()['code']}"):
            assert response.json()['code'] == 200
        with allure.step(f"Type в теле ответа = {response.json()['type']}"):
            assert response.json()['type'] == "unknown"
        with allure.step(f"message в теле ответа {response.json()['message']}"):
            assert response.json()['message'] != ""

    @allure.story('Поиск пользователя по username')
    def test_get_user_by_username(self, create_user):
        fix_user = create_user['username']
        response = self.user.get_user(fix_user)
        ApiPetStore.LOGGER.info(f"Код ответа - {response.status_code},тело ответа {response.json()}")

        with allure.step(f"HTTP статус код ответа = {response.status_code == 200}"):
            assert response.status_code == 200, f'Фактический статус код {response.status_code}'
        with allure.step(f"username в теле  ответа = {response.json()['username']}"):
            assert response.json()['username'] == create_user['username']
        with allure.step(f"firstName у найденного пользователя равен {response.json()['firstName']}"):
            assert response.json()['firstName'] == create_user['firstName']
        with allure.step(f"lastName у найденного пользователя равен {response.json()['lastName']}"):
            assert response.json()['lastName'] == create_user['lastName']
        with allure.step(f"email у найденного пользователя равен {response.json()['email']}"):
            assert response.json()['email'] == create_user['email']
        with allure.step(f"password у найденного пользователя равен {response.json()['password']}"):
            assert response.json()['password'] == create_user['password']
        with allure.step(f"phone у найденного пользователя равен {response.json()['phone']}"):
            assert response.json()['phone'] == create_user['phone']

    @allure.story('Обновление данных пользователя')
    def test_update_user(self, create_user):
        username = create_user['username']
        response = self.user.update_user(username=username, json=create_user)
        ApiPetStore.LOGGER.info(f"Код ответа - {response.status_code},тело ответа {response.json()}")

        with allure.step(f"HTTP статус код ответа = {response.status_code == 200}"):
            assert response.status_code == 200, f'Фактический статус код {response.status_code}'
        with allure.step(f"code в теле ответа равен {response.json()['code']}"):
            assert response.json()['code'] == 200
        with allure.step(f"type в теле ответа равен {response.json()['type']}"):
            assert response.json()['type'] == "unknown"
        with allure.step(f"message в теле ответа {response.json()['message']}"):
            assert response.json()['message'] != ""

    @allure.story('Удаление  пользователя')
    def test_delete_user(self, create_user):
        fix_user = create_user['username']
        response = self.user.delete_user(fix_user)
        ApiPetStore.LOGGER.info(f"Код ответа - {response.status_code},тело ответа {response.json()}")

        with allure.step(f"HTTP статус код ответа = {response.status_code}"):
            assert response.status_code == 200, f'Фактический статус код {response.status_code}'
        with allure.step(f"username в теле ответа равен username {response.json()['message']}"):
            assert response.json()['message'] == create_user['username'], f'Имя удаленного не свпадает с именем созданного юзера'
        with allure.step(f"type в теле ответа равен {response.json()['type']}"):
            assert response.json()['type'] == "unknown", f'Тип сообщение не "unknown"'
        with allure.step(f"code в теле ответа равен {response.json()['code']}"):
            assert response.json()['code'] == 200, f'Тип сообщение не 200'

    @allure.story('Логин пользователя в систему')
    def test_login_user(self, create_user):
        response = self.user.login(username=create_user['username'], password=create_user['password'])
        ApiPetStore.LOGGER.info(f"Код ответа - {response.status_code},тело ответа {response.json()}")

        with allure.step(f"HTTP статус код ответа = {response.status_code}"):
            assert response.status_code == 200, f'Фактический статус код {response.status_code}'
        with allure.step(f"Код в теле ответа равен {response.json()['code']}"):
            assert response.json()['code'] == 200
        with allure.step(f"type в теле ответа равен {response.json()['type']}"):
            assert response.json()['type'] == "unknown"
        with allure.step(f"message в теле ответа {response.json()['message']}"):
            assert response.json()['message'] != ""

    @allure.story('Выход пользователя из системы')
    def test_logout_user(self, create_user):
        response = self.user.logout()
        ApiPetStore.LOGGER.info(f"Код ответа - {response.status_code},тело ответа {response.json()}")

        with allure.step(f"HTTP статус код ответа =200"):
            assert response.status_code == 200, f'Фактический статус код {response.status_code}'
        with allure.step(f"Код в теле ответа равен {response.json()['code']}"):
            assert response.json()['code'] == 200
        with allure.step(f"type в теле ответа равен {response.json()['type']}"):
            assert response.json()['type'] == "unknown"
        with allure.step(f"message в теле ответа равен {response.json()['message']}"):
            assert response.json()['message'] == "ok"

    @allure.story('Создание массива новых  пользователей')
    def test_list_new_user(self, create_user):
        response = self.user.create_wit_list(UserJSON.new_list_users(5))
        ApiPetStore.LOGGER.info(f"Код ответа - {response.status_code},тело ответа {response.json()}")

        with allure.step(f"HTTP статус код ответа = {response.status_code}"):
            assert response.status_code == 200, f'Фактический статус код {response.status_code}'
        with allure.step(f"Код в теле ответа равен {response.json()['code']}"):
            assert response.json()['code'] == 200, f'Код в теле ответа не равен 200.'
        with allure.step(f"type в теле ответа {response.json()['type']}"):
            assert response.json()['type'] == "unknown", 'type в теле ответа равен unknown'
        with allure.step(f"message в теле ответа {response.json()['message']}"):
            assert response.json()['message'] == "ok"















