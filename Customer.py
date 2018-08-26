class Customer:
    def __init__(self, name, age, email, licence):
        self._name = name
        self._age = age
        self._email = email
        self._license = licence

    def get_name(self):
        return self._name

    def get_age(self):
        return self.age

    def get_email(self):
        return self._email

    def get_licence(self):
        return self._license
