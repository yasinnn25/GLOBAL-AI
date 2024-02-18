class Library:
    def __init__(self):
        try:
            self.file = open("books.txt", "a+")  # Open or create the file
        except FileNotFoundError:
            print("Error: Could not open books.txt")
            exit(1)  # Exit the program if file cannot be opened

    def __del__(self):
        self.file.close()  # Close the file when the program ends

    def list_books(self):
        self.file.seek(0)  # Move cursor to the beginning of the file
        book_lines = self.file.read().splitlines()
        for line in book_lines:
            book_info = line.split(",")
            book_title, book_author = book_info[0], book_info[1]
            print(f"Book: {book_title}, Author: {book_author}")

    def add_book(self):
        book_title = input("Enter book title: ")
        book_author = input("Enter author: ")
        release_year = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")

        book_line = f"{book_title},{book_author},{release_year},{num_pages}\n"
        self.file.write(book_line)
        print(f"Book '{book_title}' added successfully.")

    def remove_book(self):
        book_title_to_remove = input("Enter book title to remove: ")
        self.file.seek(0)  # Move cursor to the beginning of the file
        book_lines = self.file.read().splitlines()

        updated_books = [line for line in book_lines if book_title_to_remove not in line]
        self.file.seek(0)
        self.file.truncate()  # Clear the file contents
        for updated_line in updated_books:
            self.file.write(updated_line + "\n")

        print(f"Book '{book_title_to_remove}' removed successfully.")


# Create an object named "lib" with "Library" class
lib = Library()

# Create a menu to interact with the "lib" object
while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("q) Quit")

    choice = input("Enter your choice: ")
    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice.lower() == "q":
        break
    else:
        print("Invalid choice. Please try again.")
