import requests
import allure
from api_store.petstore import ApiPetStore


class Pet(ApiPetStore):

    def upload_image(self, pet_id, additional_metadata, files):
        """
        Загрузка изображения питомца
        Parameters:
                    pet_id (str): id питомца
                    additional_metadata (str): описание к загружаемому изображению

        """
        endpoint = ApiPetStore.BASE_URL + f'pet/{pet_id}/uploadImage'
        payload = {'additionalMetadata': additional_metadata}
        files = {'file': open(files, 'rb')}
        headers = {'Accept': 'application/json'}
        with allure.step(f'POST запрос к эндпоинту: {endpoint} c телом запроса {payload} {files}'):
            ApiPetStore.LOGGER.info(f"POST {endpoint} - {payload} - {files}")
            return requests.request("POST", endpoint, headers=headers, data=payload, files=files)

    def add_new_pet_to_store(self, json):
        """
        Питомец, которого надо добавить в магазин.
        Parameters:
                    json (json): данные о питомце в json формате
        """
        endpoint = ApiPetStore.BASE_URL + 'pet'
        headers = {'Content-Type': 'application/json'}
        with allure.step(f'POST запрос к эндпоинту: {endpoint} c телом запроса {json}'):
            ApiPetStore.LOGGER.info(f"POST {endpoint} - {json}")
            return requests.request("POST", endpoint, headers=headers, json=json)

    def update_pet(self, json):
        """
        Питомец, у которого надо обновить данные в магазине.
        Parameters:
                    json (json): данные о питомце в json формате
        """
        endpoint = ApiPetStore.BASE_URL + 'pet'
        headers = {'Content-Type': 'application/json'}
        with allure.step(f'PUT запрос к эндпоинту: {endpoint} c телом запроса {json}'):
            ApiPetStore.LOGGER.info(f"PUT {endpoint} - {json}")
            return requests.request("PUT", endpoint, headers=headers, json=json)

    def find_by_status(self, status):
        """
        Поиск питомца по статусу.
        Parameters:
                    status (str): статус питомца
        """
        endpoint = ApiPetStore.BASE_URL + f'pet/findByStatus?status={status}'
        with allure.step(f'GET запрос к эндпоинту: {endpoint}'):
            ApiPetStore.LOGGER.info(f"GET {endpoint}")
            return requests.request("GET", endpoint)

    def find_by_id(self, pet_id):
        """
        Поиск питомца по ID
        Parameters:
                    pet_id (int): id питомца
        """
        endpoint = ApiPetStore.BASE_URL + f'pet/{pet_id}'
        with allure.step(f'GET запрос к эндпоинту: {endpoint}'):
            ApiPetStore.LOGGER.info(f"GET {endpoint}")
            return requests.request("GET", endpoint)

    def delete_pet(self, pet_id ):
        """
        Удаление питомца
        Parameters:
                    pet_id (int): id питомца
        """
        endpoint = ApiPetStore.BASE_URL + f'pet/{pet_id}'
        with allure.step(f'DELETE запрос к эндпоинту: {endpoint}'):
            ApiPetStore.LOGGER.info(f"DELETE {endpoint}")
            return requests.request("DELETE", endpoint)






