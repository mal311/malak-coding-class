class Library:
    def __init__(self, list_of_books, Lname) : #constructor
        self.booklist = list_of_books
        self.name = Lname #library name
        self.lendDict = {}
    
    def displayBooks(self):
        print(f"we have the following books in our library: {self.name}")
        for book in self.booklist:
            print(book)

    def addbook(self, book):
        self.booklist.append(book)
        print(f"{book} has been added to the booklist")

    def lendbook(self,user,book):
        if book not in self.booklist:
            print("Sorry, we do not have that book")
        elif book in self.lendDict:
            print(f"The book is already being used by{self.lendDict[book]}")
        else:
            self.lendDict[book]: user
            print("Lender-book database has been updated. You can take the book now.")

    def return_book(self, book):
        if book in self.lendDict:
            del self.lendDict[book]
            print("Book has been returned")
        else:
            print("That book wasn't borrowed from us")

if __name__ =='__main__':
    books = Library(['Python', 'Rich Dad Poor Dad', 'c++ Basics', 'Harry Potter', 'Algorithms by CLRS'],
     "Lets's upskill")
    
    user_name = input("Welcome to our library! Please enter your name:")


    while True :
        print(f"Hello {user_name}, welcome to the {books.name} library. Please choose an option:")
        print("1. Display books\n2. Lend a book\n3. Add a book\n4. Return a book\n5. Quit ")
        user_choice = input("Enter your choice to continue: ")

        if user_choice not in ['1', '2', '3', '4', '5']:
            print("Please enter a valid option")
            continue
            print()

        if user_choice == '1':
            books.displayBooks()
            print()
        elif user_choice =='2':
            borrow_book = input("Enter the name of the book you want to lend: ")
            books.lendbook(user_name, borrow_book)
            print()
        elif user_choice =='3':
            insert_book = input("Enter the name of the book you want to add: ")
            books.addbook(insert_book)
            print()
        elif user_choice == '4':
            give_book = input("Enter the name of the book you want to return: ")
            books.return_book(give_book)
            print()
        elif user_choice == '5':
            print(f"Thank you for using the library, {user_name}. Goodbye!")
            break # stop the process and get out of loop
