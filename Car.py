from abc import ABC, abstractmethod
import textwrap


class Car(ABC):
    def __init__(self, model, make, year, rental_price, registration):
        self.model = model
        self.make = make
        self.year = year
        self.rental_price = rental_price
        self.registration = registration

    def get_type(self):
        return self.type

    def get_model(self):
        return self.model

    def get_make(self):
        return self.make

    def get_year(self):
        return self.year

    def get_rental_price(self):
        return self.rental_price

    def get_registration(self):
        return self.registration

    def __str__(self):
        return "Details:\nCar Make: {}\nCar Model: {}\nCar Year:{}\nRegistration: {}"\
            .format(self.make, self.model, self.year, self.registration)


class SmallCar(Car):
    def __init__(self, model, make, year, rental_price, registration):
        super().__init__(model, make, year, rental_price, registration)


class MediumCar(Car):
    def __init__(self, model, make, year, rental_price, registration):
        super().__init__(model, make, year, rental_price, registration)


class LargeCar(Car):
    def __init__(self, model, make, year, rental_price, registration):
        super().__init__(model, make, year, rental_price, registration)


class PremiumCar(Car):
    def __init__(self, model, make, year, rental_price, registration):
        super().__init__(model, make, year, rental_price, registration)
