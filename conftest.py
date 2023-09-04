import pytest
from api_store.petstore import ApiPetStore
from api_store.pet import Pet
from api_store.user import User
from api_store.store import Store
from helpers.pet import PetJSON
from helpers.user import UserJSON
from helpers.order import OrderJSON
import allure


@pytest.fixture()
def create_pet():
    pet = Pet()
    new_pet = PetJSON.new_pet()
    with allure.step("Создание тестового питомца"):
        response = pet.add_new_pet_to_store(new_pet)
    ApiPetStore.LOGGER.info(f"Код ответа - {response.status_code} - {response.json()}")
    return response.json()


@pytest.fixture()
def create_user():
    user = User()
    new_user = UserJSON.new_user()
    with allure.step("Создание тестового пользователя"):
        response = user.create_user(new_user)
    ApiPetStore.LOGGER.info(f"Код ответа - {response.status_code},тело ответа {response.json()}")
    return new_user

@pytest.fixture()
def create_order():
    store = Store()
    with allure.step("Создание тестового заказа"):
        response = store.order_pet(OrderJSON.new_order(465151561865132, 1, 'placed', True))
    return response.json()
