class Person:
    # Represents a general person
    def __init__(self, id, name, address, age):
        self.id = id
        self.name = name
        self.address = address
        self.age = age

class Student(Person):
    def __init__(self, id, name, address, age, academic_record):
        super().__init__(id, name, address, age)  # Call the parent class's constructor
        self.academic_record = academic_record

class Teacher(Person):
    def __init__(self, id, name, address, age, tax_code, salary):
        super().__init__(id, name, address, age)  # Call the parent class's constructor
        self.tax_code = tax_code
        self.salary = salary

class Staff(Person):
    def __init__(self, id, name, address, age, tax_code, pay_rate):
        super().__init__(id, name, address, age)  # Call the parent class's constructor
        self.tax_code = tax_code
        self.pay_rate = pay_rate
