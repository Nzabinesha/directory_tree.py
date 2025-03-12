#!/usr/bin/python3
# Library Catalog Search
class LibraryCatalog:
    def __init__(self):
        self.books = {
            "Introduction to Python": "1234567890",
            "Data Structures and Algorithms": "2345678901",
            "Database Management Systems": "3456789012",
            "Operating Systems Concepts": "4567890123",
            "Discrete Mathematics": "5678901234",
            "Computer Networks": "6789012345"
        }

    def search_book(self, title):
        if title in self.books:
            print("Book found!")
        else:
            print("Book not found.")

# Directory Tree Structure
class DirectoryNode:
    def __init__(self, name):
        self.name = name
        self.subdirectories = []

    def add_subdirectory(self, subdirectory):
        self.subdirectories.append(subdirectory)

    def remove_subdirectory(self, subdirectory_name):
        for subdirectory in self.subdirectories:
            if subdirectory.name == subdirectory_name:
                self.subdirectories.remove(subdirectory)
                return True
            if subdirectory.remove_subdirectory(subdirectory_name):
                return True
        return False

    def display(self, indent=0):
        print("  " * indent + self.name)
        for subdirectory in self.subdirectories:
            subdirectory.display(indent + 1)


# === Library Book Search Execution ===
library = LibraryCatalog()
search_title = input("Enter the book title you are looking for: ")
library.search_book(search_title)

# === Directory Tree Execution ===
root = DirectoryNode("Pictures")

# Creating directories
saved_pictures = DirectoryNode("Saved Pictures")
web_images = DirectoryNode("Web Images")
chrome = DirectoryNode("Chrome")
opera = DirectoryNode("Opera")
firefox = DirectoryNode("Firefox")

# Adding subdirectories
root.add_subdirectory(saved_pictures)
saved_pictures.add_subdirectory(web_images)
web_images.add_subdirectory(chrome)
web_images.add_subdirectory(opera)

# Display initial directory structure
print("\nCurrent Directory Structure:")
root.display()

# Add "Firefox" to "Web Images"
web_images.add_subdirectory(firefox)
print("\nDirectory Structure After Adding 'Firefox':")
root.display()

# Remove "Web Images"
root.remove_subdirectory("Web Images")
print("\nDirectory Structure After Removing 'Web Images':")
root.display()

