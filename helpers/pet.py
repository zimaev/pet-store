import random
from faker import Faker


fake = Faker('ru_RU')
name = fake.first_name()
photo_urls = [fake.url() for _ in range(5)]
status = random.choice(("available", "pending"))


class PetJSON:

    @staticmethod
    def new_pet():
        json = {
            "name": name,
            "photoUrls": photo_urls,
            "status": status
        }
        return json

    @staticmethod
    def update_pet(id):
        json = {
            "id": id,
            "name": fake.first_name(),
            "photoUrls": [fake.url() for _ in range(2)],
            "status": "sold"
        }
        return json


