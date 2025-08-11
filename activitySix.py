class PersonInformaton:
    def __init__(self):
        self.personal_details = []

    def display_details(self):
        return f"Person Information is Name: {self.personal_details[0]}, Age: {self.personal_details[1]}, Address: {self.personal_details[2]}."

    def update_age(self):
        year_add = int(input("Added year: "))
        self.personal_details[1] = year_add + int(self.personal_details[1])

if __name__ == "__main__":
    objPerson = PersonInformaton()

    for i in range(3):
        item = input("Enter an element: ")
        objPerson.personal_details.append(item)

    print(objPerson.display_details())
    objPerson.update_age()
    print(objPerson.display_details())