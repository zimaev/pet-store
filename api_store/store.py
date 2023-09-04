import requests
import allure
from api_store.petstore import ApiPetStore


class Store(ApiPetStore):

    def order_pet(self, json):
        """
        Создаеть заказ на питомца
        Parameters:
                    json (json): данные заказа в json формате
        """
        endpoint = ApiPetStore.BASE_URL + 'store/order'
        headers = {'Content-Type': 'application/json', 'Accept': '*/*'}
        with allure.step(f'POST запрос к эндпоинту: {endpoint} c телом запроса {json}'):
            ApiPetStore.LOGGER.info(f"POST {endpoint} - {json}")
            return requests.request("POST", endpoint, headers=headers, json=json)

    def find_order(self, order_id):
        """
        Поиск заказа по ID
        Parameters:
                    order_id (int): ID заказа
        """
        endpoint = ApiPetStore.BASE_URL + f'store/order/{order_id}'
        with allure.step(f'GET запрос к эндпоинту: {endpoint}'):
            ApiPetStore.LOGGER.info(f"GET {endpoint}")
            return requests.request("GET", endpoint)

    def delete_order(self, order_id):
        """
        Удаление питомца по ID
        Parameters:
                    order_id (int): ID заказа
        """
        endpoint = ApiPetStore.BASE_URL + f'store/order/{order_id}'
        with allure.step(f'DELETE запрос к эндпоинту: {endpoint}'):
            ApiPetStore.LOGGER.info(f"DELETE {order_id}")
            return requests.request("DELETE", endpoint)

    def inventory(self):
        """
        Инвентаризация.
        """
        endpoint = ApiPetStore.BASE_URL + 'store/inventory'
        with allure.step(f'GET запрос к эндпоинту: {endpoint}'):
            ApiPetStore.LOGGER.info(f"GET {endpoint}")
            return requests.request("GET", endpoint)

