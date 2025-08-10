# class PersonInformaton:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
#     def display_details(self):
#         return f"My Name is {self.name}, I'm {self.age} years now and I live in {self.address}."

if __name__ == "__main__":
    personal_details = []
    num_elements = int(input("Enter the number of elements to add: "))

    for i in range(num_elements):
        element = input("Enter an element: ")
        personal_details.append(element)

    print(f"My Name is {personal_details[0]}, I'm {personal_details[1]} years now and I live in {personal_details[2]}.")

    upadate_age = int(input("Added year: "))
    new_age = upadate_age + int(personal_details[1])
    print(f"My Name is {personal_details[0]}, I'm {new_age} years now and I live in {personal_details[2]}.")