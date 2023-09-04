from faker import Faker

fake = Faker('ru_RU')
username = fake.profile(['username'])['username']
password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
phone = fake.phone_number()


class UserJSON:

    @staticmethod
    def new_user():
        json = {
          "username": username,
          "firstName": first_name,
          "lastName": last_name,
          "email": email,
          "password": password,
          "phone": phone,
          "userStatus": 0
        }

        return json

    @staticmethod
    def new_list_users(count):
        return [UserJSON.new_user() for _ in range(count)]




