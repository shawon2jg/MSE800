from MSE800.activityFiveWeek05.Person import Person

class Student(Person):
    def __init__(self, name, address, age, student_id):
        super().__init__(name, address, age)
        self.student_id = student_id

if __name__ == '__main__':
    objStudent = Student("S M Shawon", "Avondale", 35, "270702380")