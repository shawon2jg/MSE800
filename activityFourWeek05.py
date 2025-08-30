# Develop Python code that demonstrates inheritance in a Zoo project using two classes, Color and Transparent-Color; applied to an Animal.

class Color:
    def __init__(self, red, green, blue):
        self.red = max(0, min(255, red))
        self.green = max(0, min(255, green))
        self.blue = max(0, min(255, blue))

    def get_color(self):
        return f"RGB({self.red}, {self.green}, {self.blue})"

    def describe(self):
        return f"Color: {self.get_color()}"

class TransparentColor(Color):
    def __init__(self, red, green, blue, alpha):
        super().__init__(red, green, blue)
        self.alpha = max(0, min(1.0, alpha))

    def get_color(self):
        return f"RGBA({self.red}, {self.green}, {self.blue}, {self.alpha})"

    def describe(self):
        return f"Transparent Color: {self.get_color()}"

class Animal():
    def __init__(self, name, species, color):
        self.name = name
        self.species = species
        self.color = color

    def display_info(self):
        return f"{self.name} is a {self.species} with {self.color.describe()}"

if __name__ == "__main__":
    # Create a regular color for a lion
    lion_color = Color(139, 69, 19)  # Brown
    lion = Animal("Leo", "Lion", lion_color)

    # Create a transparent color for a jellyfish
    jellyfish_color = TransparentColor(0, 0, 255, 0.7)   # Slightly transparent blue
    jellyfish = Animal("Fluffel", "Jellyfish", jellyfish_color)

    print(lion.display_info())
    print(jellyfish.display_info())