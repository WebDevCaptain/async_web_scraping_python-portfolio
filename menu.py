import logging
from app import books

logger = logging.getLogger("scraping.menu")

USER_CHOICE = """Enter any one of the following 
- b : to look at top 10 five star books,
- c : to look at the top 10 cheapest books
- n : to view the next book in the catalogue
- q : to Quit the Application
Enter your choice : 
"""


def print_best_books():
    logger.info("Finding best books by rating...")
    best_books = sorted(books, key=lambda x: x.rating, reverse=True)[:10]
    for book in best_books:
        print(book)


def print_cheapest_books():
    logger.info("Finding cheapest books...")
    cheapest_books = sorted(books, key=lambda x: x.price, reverse=False)[:10]
    for book in cheapest_books:
        print(book)


books_generator = (x for x in books)


def get_next_book():
    logger.info("Finding next book in the catalogue...")
    print(next(books_generator))


user_choices = {"b": print_best_books, "c": print_cheapest_books, "n": get_next_book}


def menu():
    user_input = input(USER_CHOICE)

    while user_input != "q":
        if user_input in ("b", "c", "n"):
            user_choices[user_input]()
        else:
            print("Please give a valid input")
        user_input = input(USER_CHOICE)

    if user_input == "q":
        print("\nQuitting the Application")
    logger.debug("Terminating Program")


menu()
