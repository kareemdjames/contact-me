class Person:
    def __init__(self, first_name, last_name, age, phone_number, address):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
        self.address = address

    def full_name(self):
        print(f'{self.first_name} {self.last_name}')