import datetime
from Car import *
from Customer import *
from Loan import *


class BookingSystem:
    def __init__(self):
        self._cars = []
        self._loans = []
        self._staff = []

    def book_car(self, car, name, age, licence, email, date, period, pickup, dropoff):
        customer = Customer(name, age, email, licence)
        loan = Loan(car, customer, date, period, pickup, dropoff)

        self._loans.append(loan)

        print(loan)


if __name__ == "__main__":
    small_car = SmallCar("Go!", "Volkswagen", "2017", 20, "LUK 888")
    large_car = LargeCar("Cherokee", "Jepp", "2010", 30, "LUK 777")
    premium_car = PremiumCar("Model T", "Ford", "1920", 40, "LUK 666")

    bs = BookingSystem()
    # this shouldn't be allowed, but for purposes of demonstration
    bs._cars.extend([small_car, large_car, premium_car])

    pickup_date = datetime.date(2002, 3, 11)
    bs.book_car(small_car, "Ilan Musk", "20", "dev666sat", "juicyboy@mailme.com", pickup_date, 10, "UNSW", "ScrapYard")
    bs.book_car(large_car, "Ilan Musk", "20", "dev666sat", "juicyboy@mailme.com", pickup_date, 10, "UNSW", "ScrapYard")
    bs.book_car(premium_car, "Ilan Musk", "20", "dev666sat", "juicyboy@mailme.com", pickup_date, 10, "UNSW", "ScrapYard")

