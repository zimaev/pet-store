import datetime
import random


class OrderJSON:

    @staticmethod
    def new_order(pet_id, quantity, status, complete):
        json = {

            "petId": pet_id,
            "quantity": quantity,
            "shipDate": datetime.datetime.now().isoformat(),
            "status": status,
            "complete": complete
            }

        return json
