#region Activity 07
# You are tasked with developing a simple program for the Human Resources (HR) department to store and display basic employee information, including each employee’s name, salary, and job title.
# Requirements:
# 1.Create at least two Employee objects with different data.
# 2.Call the display_info() method to show each employee’s details.
# 3.Call the give_raise() method to increase an employee’s salary and display the updated amount.
#endregion

class Employee:
    def __init__(self):
        self.employee_list = []

    def insert_employee_details(self):
        no_of_employees = int(input("Enter the number of employees: "))
        for i in range(no_of_employees):
            self.employee_list.append(input("Enter the employee's name: "))
            self.employee_list.append(input("Enter the employee's salary: "))
            self.employee_list.append(input("Enter the employee's job tile: "))

    def display_info(self):
        count = 2
        print("All Employee Information: ")
        for index, item in enumerate(self.employee_list):
            print(item, end=" ")
            if index == count:
                count += 3
                print("")

    def give_raise(self):
        count = 1
        increment = int(input(f"\nEnter the percentage increase for an employee's salary: "))
        for index, item in enumerate(self.employee_list):
            if index == count:
                self.employee_list[index] = int(self.employee_list[index]) + (increment / 100)
                count += 3

if __name__ == "__main__":
    objPerson = Employee()

    objPerson.insert_employee_details()
    objPerson.display_info()

    objPerson.give_raise()
    objPerson.display_info()