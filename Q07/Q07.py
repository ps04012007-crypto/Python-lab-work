#QUESTION NUMBER 7
#Develop a Library management System using inheritance and
#polymorphism to manage differnt types of Library items
#(Book, Magazine and Journal) and perform issue and 
#return operation.

class LibraryItem:
    def __init__(self, item_id, title):
        self.item_id = item_id
        self.title = title
        self.issued = False

    def issue(self):
        if self.issued == False:
            self.issued = True
            print(self.title, "has been issued.")
        else:
            print(self.title, "is already issued.")

    def return_item(self):
        if self.issued == True:
            self.issued = False
            print(self.title, "has been returned.")
        else:
            print(self.title, "was not issued.")

    def display(self):
        print("ID:", self.item_id)
        print("Title:", self.title)
        if (self.issued):
          print("Status:", "Issued") 
        else:
          print("Available")


class Book(LibraryItem):
    def display(self):
        print("Type: Book")
        super().display()


class Magazine(LibraryItem):
    def display(self):
        print("Type: Magazine")
        super().display()


class Journal(LibraryItem):
    def display(self):
        print("Type: Journal")
        super().display()


# Creating objects
book = Book(101, "Python Programming")
magazine = Magazine(102, "Science Today")
journal = Journal(103, "Computer Science Journal")

items = [book, magazine, journal]


# Menu
while True:
    print("\n----- Library Management System -----")
    print("1. Display Items")
    print("2. Issue Item")
    print("3. Return Item")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\n----- Library Items -----")
        for item in items:
            item.display()
            print()

    elif choice == 2:
        item_id = int(input("Enter Item ID to issue: "))

        for item in items:
            if item.item_id == item_id:
                item.issue()
                break
        else:
            print("Item not found.")

    elif choice == 3:
        item_id = int(input("Enter Item ID to return: "))

        for item in items:
            if item.item_id == item_id:
                item.return_item()
                break
        else:
            print("Item not found.")

    elif choice == 4:
        print("Thank you for using Library Management System.")
        break

    else:
        print("Invalid choice.")
