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
        print{f"{book} has been added to the booklist"}

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
    books= Library(['Python', 'Rich Dad Poor Dad', 'c++ Basics', 'Harry Potter', 'Algorithms by CLRS', "Lets's upskill"])
    user_name = input("Welcome to our library! Please enter your name:")

    while True :
        print(f"Hello{user_name}, welcome to the{books.name} library. Please choose an option:")
        print("1. Display books/ n2. Lend a book/ n3.  ")