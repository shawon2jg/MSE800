import numpy as np

class StringManipulator:
    def __init__(self, text):
        self.text = text

    def find_character(self, char):
        return self.text.find(char)

    def find_length(self, text):
        length = len(self.text)
        return length

name = StringManipulator("Example")
# result_char = name.find_character("X")
# result_length = name.find_length(name)
result_upper = name
print(result_upper) # Output: 1