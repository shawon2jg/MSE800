class StringManipulator:
    def __init__(self, text):
        self.text = text

    def find_character(self, char):
        return self.text.find(char)

    def get_length(self, text):
        length = len(self.text)
        return length

    def convert_uppercase(self, text):
        uppercase = self.text.upper()
        return uppercase

name = StringManipulator("Example")

index = name.find_character("x")
print(f"The index of the character: {index}")

length = name.get_length(name)
print(f"The length of the character: {length}")

upper = name.convert_uppercase(name)
print(f"The uppercase of the character: {upper}")