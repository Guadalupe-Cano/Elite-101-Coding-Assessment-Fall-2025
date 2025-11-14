
Guadalupe Cano
1:29 AM (17 hours ago)
to me

from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author

def acess_avaliable_books():
    #for loop will look through each dictionary to see if condition is met
    for availableBooks in library_books:
        # if statement will make sure book information is only outputed if the book is avaliable
        if availableBooks["available"] == True:
            # prints the organized information for books avaliable 
            print("Book ID: " + (availableBooks["id"]) + " Title: " + (availableBooks["title"]) + " Author: " + (availableBooks["author"]))
# calls function
print(" ")

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

def search_Genre_or_Author():
    termSearched = input("Would you like to search books with same Genre or Author?\n")
    if termSearched.lower() == "genre":
        genreTerm = input("What type of genre are you looking for: ")
        for availableBooks in library_books:
            if availableBooks["genre"].lower() == (genreTerm.lower()):
                print(" Title: " + (availableBooks["title"]))
    elif termSearched.lower() == "author":
        authorTerm = input("What type of Author are you looking for: ")
        for availableBooks in library_books:
            if availableBooks["author"].lower() == (authorTerm.lower()):
                print(" Title: " + (availableBooks["title"]))
    else:
        print("You have submitted an invalid answer. Try again.")





# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out


def checkOutBook():
    UserBookID = input("Please enter Book ID for prefered book to checkout: ")
    for availableBooks in library_books:
            if availableBooks["id"] == UserBookID:
                if availableBooks["available"] == True:
                    availableBooks["available"]== False
                    availableBooks["checkouts"] +=1
                    today = datetime.today()
                    due_date = today + timedelta(weeks=2)
                    availableBooks['due_date'] = due_date.strftime("%Y-%m-%d")
                    print("You have succesfully checkout " + availableBooks["title"])
                else: 
                    print("Unfortunately, this book is already checked out.")



# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out

def returnBook():
    UserBookID = input("Please enter Book ID for prefered book to return: ")
    for availableBooks in library_books:
            if availableBooks["id"] == UserBookID:
                if availableBooks["available"] == False:
                    availableBooks["available"]== True
                    due_date = None
                    availableBooks['due_date'] = None
                    print("You have succesfully returned " + availableBooks["title"])
                else: 
                    print("This book has already been returned! ")


def overdueBook():
    print("This will list all overDue books! ")
    today = datetime.today()
    for book in library_books:
        if book["due_date"] is not None:
            if book["due_date"] < today:
                print(f"Title: book['title'] ")
             
overdueBook()
