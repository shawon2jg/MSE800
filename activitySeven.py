class Employee:
    def __init__(self):
        self.employee_list = []

    def insert_employee_details(self):
        no_of_employees = int(input("Enter the number of employees: "))
        for i in range(no_of_employees):
            self.employee_list.append(input("Enter the employee's name: "))
            self.employee_list.append(input("Enter the employee's salary: "))
            self.employee_list.append(input("Enter the employee's job tile: "))

    def display_details(self):
        print("All Employee Information: ")
        for index, item in enumerate(self.employee_list):
            print(item, end=" ")
            if index == 2:
                print("")

if __name__ == "__main__":
    objPerson = Employee()
    objPerson.insert_employee_details()
    objPerson.display_details()