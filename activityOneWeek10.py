from abc import ABC, abstractmethod

class TextAnalyzer(ABC):
    @abstractmethod
    def get_length(self):
        pass

    @abstractmethod
    def count_uppercase(self):
        pass

class StringAnalyzer(TextAnalyzer):
    def __init__(self, input_string):
        if not isinstance(input_string, str):
            raise TypeError("Input must be a string")
        self.input_string = input_string

    def get_length(self):
        return len(self.input_string)

    def count_uppercase(self):
        return sum(1 for char in self.input_string if char.isupper())

class ListAnalyzer(TextAnalyzer):
    def __init__(self, input_list):
        if not isinstance(input_list, list) or not all(isinstance(item, str) for item in input_list):
            raise TypeError("Input must be a list of strings")
        self.input_list = input_list

    def get_length(self):
        return sum(len(item) for item in self.input_list)

    def count_uppercase(self):
        return sum(sum(1 for char in item if char.isupper()) for item in self.input_list)

def analyze_input(input_data):
    try:
        if isinstance(input_data, str):
            analyzer = StringAnalyzer(input_data)
        elif isinstance(input_data, list):
            analyzer = ListAnalyzer(input_data)
        else:
            raise TypeError("Input must be a string or a list of strings")

        return {
            "length": analyzer.get_length(),
            "uppercase_count": analyzer.count_uppercase()
        }
    except TypeError as e:
        return {"error": str(e)}

if __name__ == "__main__":
    result1 = analyze_input("Hello World!")
    print("String analysis:", result1)

    result2 = analyze_input(["Hello", "WORLD", "Python"])
    print("List analysis:", result2)

    result3 = analyze_input(123)
    print("Invalid input analysis:", result3)