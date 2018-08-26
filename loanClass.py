class Loan():
    def __init__(self,name,age,email,has_insurance,start_loan,end_loan,pickup_loc,dropoff_loc):
 
        self._car=get_model
        self._customer=Customer(name,age,email) 
        self._has_insurance=bool
        self._start_loan=start_loan
        self._end_loan=end_loan
        self._pickup_loc=pickup_loc
        self._dropoff_loc=dropoff_loc
    
    def getcustomername():
        return self._customer._name

    def getcustomerage():
        return self._customer._age

    def getcustomeremail():
        return self._customer._email

    def getendloan():
        return self._end_loan

    def getstartloan():
        return self._start_loan

    def getpickuploc():
        return self._pickup_loc

    def getdropoffloc():
        return self._dropoff_loc

    def getprice(self,start_loan,end_loan):
        period=self._end_loan-self._start_loan
        self._price= get_rental_price *period
        if get_type==large or get_type==premium and period >=7:
            self._price *=0.95
        if get_type==premium:
            self._price *=1.15
        return self._price


class Customer():
    def __init__(self,name,age,email):
        self._name=name
        self._age=age
        self._email=email
        
