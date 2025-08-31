class LibraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}")

class Book(LibraryItem):
    def __init__(self, title, author, isbn):
        super().__init__(title, author)
        self.__isbn = isbn  # Private attribute

    def display_details(self):
        print(f"Book Title: {self.title}, Author: {self.author}, ISBN: {self.__isbn}")

class Magazine(LibraryItem):
    def __init__(self, title, author, issue_frequency):
        super().__init__(title, author)
        self.__issue_frequency = issue_frequency  # Private attribute

    def display_details(self):
        # Overridden method for magazine details.
        print(f"Magazine Title: {self.title}, Author: {self.author}, Issue Frequency: {self.__issue_frequency}")


class Library:
    def __init__(self):
        self.items = []  # Private list to encapsulate the collection.

    def add_item(self, item):
        self.items.append(item)
        print(f"Added: {item.title}")

    def remove_item(self, title):
        for item in self.items:
            if item.title == title:
                self.items.remove(item)
                print(f"Removed: {title}")
                return
        print(f"Item with title '{title}' not found")

    def display_all_items(self):
        if not self.items:
            print("No items in the library")
        else:
            print("Library Items:")
            for item in self.items:
                item.display_details()

if __name__ == "__main__":
    library = Library()
    book = Book("Python Programming", "John Doe", "9780134852898")
    magazine = Magazine("Tech Monthly", "Jane Smith", 12)
    library.add_item(book)
    library.add_item(magazine)
    library.display_all_items()
    library.remove_item("Python Programming")
    library.display_all_items()