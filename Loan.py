from Car import *

class Loan():
    def __init__(self,car,customer, start_date ,period,pickup_loc,dropoff_loc):
 
        self._car=car
        self._customer=customer
        self._start_date = start_date
        self._period = period
        self._pickup_loc=pickup_loc
        self._dropoff_loc=dropoff_loc

    def get_start_date(self):
        return self._start_date

    def get_peroid(self):
        return self._period

    def get_customer(self):
        return self._customer

    def get_end_loan(self):
        return self._end_loan

    def get_start_loan(self):
        return self._start_loan

    def get_pickup_loc(self):
        return self._pickup_loc

    def get_dropoff_loc(self):
        return self._dropoff_loc

    def get_price(self):
        price= self._car.get_rental_price() * self._period
        car_type = type(self._car)

        # apply discount
        if (car_type is LargeCar or car_type is PremiumCar) and self._period >=7:
            price *=0.95

        # apply tarrif
        if car_type is PremiumCar:
            price *=1.15

        return round(price, 2)

    def __str__(self):
        cus = self._customer
        car = self._car
        email =     "Congratulations {}! Booking Successful!\n\n{}\n\nGrand Total: {}\n------\n""".format(cus.get_name(), car.__str__(), self.get_price())

        return textwrap.dedent(email)


