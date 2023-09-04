import pytest
from api_store.petstore import ApiPetStore
from api_store.store import Store
from helpers.order import OrderJSON
import allure


@allure.epic("Тесты к эндпоинтам Store")
class TestStoreApi:

    store = Store()

    def test_order_pet(self):
        response = self.store.order_pet(OrderJSON.new_order(465151561865132, 1, 'placed', True))
        ApiPetStore.LOGGER.info(f"Код ответа - {response.status_code},тело ответа {response.json()}")
        with allure.step("HTTP статус код ответа =200"):
            assert response.status_code == 200

    def test_find_order(self, create_order):
        order_id = create_order["id"]
        response = self.store.find_order(order_id)
        ApiPetStore.LOGGER.info(f"Код ответа - {response.status_code},тело ответа {response.json()}")

        with allure.step("HTTP статус-код ответа = 200"):
            assert response.status_code == 200, 'HTTP статус-код ответа не равен 200'
        with allure.step("ID айденного заказа равен созданному"):
            assert response.json()["id"] == create_order["id"], f'ID айденного заказа не равен созданному'
        with allure.step("petId питомцав в заказе равен созданному"):
            assert response.json()["petId"] == create_order["petId"], f'petId питомцав в заказе не равен созданному'
        with allure.step("Количество питомцев в заказе равено созданному"):
            assert response.json()["quantity"] == create_order["quantity"], f'Количество питомцев в заказе не равено созданному'
        with allure.step("Дата отправки айденного заказа равна созданной"):
            assert response.json()["shipDate"] == create_order["shipDate"], f'Дата отправки айденного заказа не равна созданной'
        with allure.step("Статус айденного заказа равен созданному'"):
            assert response.json()["status"] == create_order["status"], f'Статус айденного заказа не равен созданному'

    def test_delete_order(self, create_order):
        order_id = create_order["id"]
        response = self.store.delete_order(order_id)
        ApiPetStore.LOGGER.info(f"Код ответа - {response.status_code},тело ответа {response.json()}")

        with allure.step("HTTP статус код ответа =200"):
            assert response.status_code == 200, f'Фактический статус код {response.status_code}'
        with allure.step("Код ответа в теле ответа = 200"):
            assert response.json()['code'] == 200, f'Код в теле ответа не равен 200.'
        with allure.step("Type в теле ответа = unknown"):
            assert response.json()['type'] == "unknown", f'Type в теле ответа не равен ожидаемому'
        with allure.step("ID удаленного питомца равен ID созданному"):
            assert int(create_order['id']) == int(
                response.json()['message']), f"ID удаленного  питомца не равен ID созданному"

    def test_inventory(self, ):

        response = self.store.inventory()
        ApiPetStore.LOGGER.info(f"Код ответа - {response.status_code},тело ответа {response.json()}")

        with allure.step("HTTP статус код ответа =200"):
            assert response.status_code == 200
        with allure.step("Тело ответа не пустое"):
            assert response.json() != ""


