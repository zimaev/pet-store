import pytest
from api_store.petstore import ApiPetStore
from api_store.pet import Pet
from helpers.pet import PetJSON
import allure
import os.path



@allure.epic("Тесты к эндпоинтам Pet")
class TestPetApi:

    pet = Pet()

    @allure.story('Загрузка файла')
    def test_upload_pet_image(self):
        response = self.pet.upload_image(pet_id='-92221579',
                                         additional_metadata='Lorem',
                                         files=os.path.abspath("../dog.png"))
        ApiPetStore.LOGGER.info(f"Код ответа - {response.status_code}")

        with allure.step(f"HTTP статус код ответа {response.status_code == 200}"):
            assert response.status_code == 200, f'Фактический статус код {response.status_code}'
        with allure.step(f"Код ответа в теле ответа = {response.json()['code']}"):
            assert response.json()['code'] == 200, f'Код в теле ответа не равен 200.'
        with allure.step(f"Type в теле ответа = {response.json()['type']}"):
            assert response.json()['type'] == "unknown", f'Type в теле ответа не равен ожидаемому'
        with allure.step(f"message в теле ответа {response.json()['message']}"):
            assert response.json()['message'] == "additionalMetadata: Lorem\nFile uploaded to ./dog.png, 815170 bytes", f'Type в теле ответа не равен ожидаемому'

    @allure.story('Добавление питомца в магазин')
    def test_add_new_pet_to_store(self):
        new_pet = PetJSON.new_pet()
        response = self.pet.add_new_pet_to_store(new_pet)
        ApiPetStore.LOGGER.info(f"Код ответа - {response.status_code} - {response.json()}")

        with allure.step(f"HTTP статус код ответа {response.status_code}"):
            assert response.status_code == 200, f'Фактический статус код {response.status_code}'
        with allure.step(f"Имя созданного питомца равно переданному имени {new_pet['name']}"):
            assert new_pet['name'] == response.json()['name'], f'Имя созданного питомца не равно переданному имени'
        with allure.step(f"URL фотографий питомца равны переданным URL {new_pet['photoUrls']}"):
            assert new_pet['photoUrls'] == response.json()['photoUrls'], f'URL фотографий питомца не равны переданным URL'
        with allure.step(f"Статус созданного питомца равен переданному статусу"):
            assert new_pet['status'] == response.json()['status'], f'Статус созданного питомца не равен переданному статусу'

    def test_update_pet(self,create_pet):
        response = self.pet.update_pet(PetJSON.update_pet(id=create_pet['id']))
        ApiPetStore.LOGGER.info(f"Код ответа - {response.status_code} - {response.json()}")

        with allure.step(f"HTTP статус код ответа {response.status_code == 200}"):
            assert response.status_code == 200, f'Фактический статус код {response.status_code}'
        with allure.step(f"ID созданного питомца равен ID найденному {create_pet['id']}"):
            assert create_pet['id'] == response.json()['id'], f"ID созданного питомца не равен ID найденному"
        with allure.step(f"Имя созданного питомца не равно переданному имени {create_pet['name']}"):
            assert create_pet['name'] != response.json()['name'], f'Имя созданного питомца равно переданному имени'
        with allure.step(f"URL фотографий питомца равны переданным URL {create_pet['photoUrls']}"):
            assert create_pet['photoUrls'] != response.json()['photoUrls'], f'URL фотографий  питомца не равны переданным URL'
        with allure.step(f"Статус созданного питомца не равен переданному статусу {create_pet['status']}"):
            assert create_pet['status'] != response.json()['status'], f'Статус созданного питомца не равен переданному статусу'


    @allure.story('Поиск питомца по статусу')
    @pytest.mark.parametrize('status', ['available', 'pending', 'sold'])
    def test_find_pet_by_status(self, status):
        response = self.pet.find_by_status(status)
        ApiPetStore.LOGGER.info(f"Код ответа - {response.status_code}")

        with allure.step(f"HTTP статус код ответа {response.status_code}"):
            assert response.status_code == 200, f'Фактический статус код {response.status_code}'

    @allure.story('Поиск питомца по id')
    def test_find_pet_by_id(self, create_pet):
        response = self.pet.find_by_id(create_pet['id'])
        ApiPetStore.LOGGER.info(f"Код ответа - {response.status_code},тело ответа {response.json()}")

        with allure.step(f"HTTP статус код ответа {response.status_code}"):
            assert response.status_code == 200, f'Фактический статус код {response.status_code}'
        with allure.step(f"ID созданного питомца равен ID найденному {create_pet['id']}"):
            assert create_pet['id'] == response.json()['id'], f"ID созданного питомца не равен ID найденному"
        with allure.step(f"Имя созданного питомца равенj имени найденному {create_pet['name']}"):
            assert create_pet['name'] == response.json()['name'], f"Имя созданного питомца не равено имени найденному"
        with allure.step(f"Urls созданного питомца  равен Urls найденному {create_pet['photoUrls']}"):
            assert create_pet['photoUrls'] == response.json()['photoUrls'], f"Urls созданного питомца не равен Urls найденному"
        with allure.step(f"Urls созданного питомца  равен Urls найденному {create_pet['status']}"):
            assert create_pet['status'] == response.json()['status'], f"status ссзданного питомца не равен status найденному"

    @allure.story('Удаение питомца ')
    def test_delete_pet(self, create_pet):
        response = self.pet.delete_pet(create_pet['id'])
        ApiPetStore.LOGGER.info(f"Код ответа - {response.status_code},тело ответа {response.json()}")

        with allure.step(f"HTTP статус код ответа =200"):
            assert response.status_code == 200, f'Фактический статус код {response.status_code}'
        with allure.step(f"Код ответа в теле ответа = {response.json()['code']}"):
            assert response.json()['code'] == 200, f'Код в теле ответа не равен 200.'
        with allure.step(f"Type в теле ответа = unknown"):
            assert response.json()['type'] == "unknown", f'Type в теле ответа не равен ожидаемому'
        with allure.step(f"ID удаленного питомца равен ID созданному {response.json()['message']}"):
            assert int(create_pet['id']) == int(response.json()['message']), f"ID удаленного  питомца не равен ID созданному"



