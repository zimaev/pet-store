import requests
import allure
from api_store.petstore import ApiPetStore


class User(object):

    def create_wit_array(self):
        pass

    def create_wit_list(self, list):
        """
       Создание пользователя
          Parameters:
                   list (list): данные пользователей в массиве
        """
        endpoint = ApiPetStore.BASE_URL + 'user/createWithList'
        headers = {'Content-Type': 'application/json', 'Accept': '*/*'}
        with allure.step(f'POST запрос к эндпоинту: {endpoint} c телом запроса {list}'):
            ApiPetStore.LOGGER.info(f"POST {endpoint} - {list}")
            return requests.request("POST", endpoint, headers=headers, json=list)

    def get_user(self, username):
        """
        Поиск пользовалетя по username
        Parameters:
                    username (str): имя пользователя

        """
        endpoint = ApiPetStore.BASE_URL + f'user/{username}/'
        with allure.step(f'GET запрос к эндпоинту: {endpoint}'):
            ApiPetStore.LOGGER.info(f"GET {endpoint}")
            return requests.request("GET", endpoint)

    def update_user(self, username, json):
        """
        Обновление данных у пользователя
        Parameters:
                    username (str): имя пользователя
                    json (json): данные для обновления в формате json
        """

        endpoint = ApiPetStore.BASE_URL + f'user/{username}'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        with allure.step(f'POST запрос к эндпоинту: {endpoint} c телом запроса {json}'):
            ApiPetStore.LOGGER.info(f"PUT {endpoint} - {json}")
            return requests.request("PUT", endpoint, headers=headers, json=json)

    def delete_user(self, username):
        """
        Удаление пользователя
        Parameters:
                    username (str): имя пользователя

        """
        endpoint = ApiPetStore.BASE_URL + f'user/{username}'
        with allure.step(f'DELETE запрос к эндпоинту: {endpoint}'):
            ApiPetStore.LOGGER.info(f"DELETE {endpoint}")
            return requests.request("DELETE", endpoint)

    def login(self, username, password):
        """
        Авторизация в систему пользователя
        Parameters:
                    username (str): имя пользователя
                    password (str): пароль пользователя
        """
        endpoint = ApiPetStore.BASE_URL + f'user/login?username={username}&password={password}'
        with allure.step(f'GET запрос к эндпоинту: {endpoint}'):
            ApiPetStore.LOGGER.info(f"GET {endpoint}")
            return requests.request("GET", endpoint)

    def logout(self):
        """
        Выход из системы пользователя
        """
        endpoint = ApiPetStore.BASE_URL + 'user/logout'
        with allure.step(f'GET запрос к эндпоинту: {endpoint}'):
            ApiPetStore.LOGGER.info(f"GET {endpoint}")
            return requests.request("GET", endpoint)

    def create_user(self, json):
        """
        Создание пользователя
           Parameters:
                    json (json): данные пользователя
        """
        endpoint = ApiPetStore.BASE_URL + 'user'
        headers = {'Content-Type': 'application/json', 'Accept': '*/*'}
        with allure.step(f'POST запрос к эндпоинту: {endpoint} c телом запроса {json}'):
            ApiPetStore.LOGGER.info(f"POST {endpoint} - {json}")
            return requests.request("POST", endpoint, headers=headers, json=json)

