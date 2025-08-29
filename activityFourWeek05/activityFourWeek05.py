from MSE800.activityFourWeek05.activityFourPerson import Person

class Student(Person):
    def __init__(self, name, address, age, student_id):
        super().__init__(name, address, age)  # Call the parent class's constructor
        self.student_id = student_id

if __name__ == '__main__':
    objStudent = Student("Kamal Bin Shafiq ", "Avondale", 20, "S001")