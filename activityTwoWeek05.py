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

class Staff(Person):
    def __init__(self, id, name, address, age, tax_code):
        super().__init__(id, name, address, age)  # Call the parent class's constructor
        self.tax_code = tax_code

# Call the Multilevel inheritance
class Academic(Staff):
    def __init__(self, id, name, address, age, tax_code, salary):
        super().__init__(id, name, address, age, tax_code)  # Call the parent class's constructor
        self.tax_code = tax_code
        self.salary = salary

# Call the Multilevel inheritance
class General(Staff):
    def __init__(self, id, name, address, age, tax_code, pay_rate):
        super().__init__(id, name, address, age, tax_code)  # Call the parent class's constructor
        self.pay_rate = pay_rate

if __name__ == '__main__':
    objStudent = Student("John Doe", "123 Student St", 20, "S001", {"GPA": 3.8})
    objAcademic = Academic("Dr. Smith", "456 Prof Ave", 45, "A001", "T123", 75000)
    objGeneral = General("Jane Wilson", "789 Staff Rd", 35, "G001", "T456", 25.50)