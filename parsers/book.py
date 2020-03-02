import re
import logging
from locators.book_locators import BookLocators

logger = logging.getLogger("scraping.book_parser")


class BookParser:
    """
    Given one of the specific Book divs, find out the data about the Book
    """

    RATINGS = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

    def __init__(self, parent):
        logger.debug(f"New book parser created from `{parent}`.")
        self.parent = parent

    def __repr__(self):
        return f"Book {self.title} priced at {self.price}$ and Ratings: {self.rating}"

    @property
    def title(self):
        logger.debug("Finding the book name...")
        locator = BookLocators.TITLE
        item_name = self.parent.select_one(locator).attrs["title"]
        logger.debug(f"Found book name: `{item_name}`.")
        return item_name

    @property
    def link(self):
        logger.debug("Finding the book link...")
        locator = BookLocators.LINK
        return self.parent.select_one(locator).attrs["href"]

    @property
    def price(self):
        logger.debug("Finding the book price...")
        locator = BookLocators.PRICE
        item_price = self.parent.select_one(locator).string

        pattern = "£([0-9]+\.[0-9]+)"
        matcher = re.search(pattern, item_price)
        book_price = float(matcher.group(1))
        logger.debug(f"Found book price: `{book_price}`.")
        return book_price

    @property
    def rating(self):
        logger.debug("Finding the book rating...")
        locator = BookLocators.RATING
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs["class"]
        rating_classes = [r for r in classes if r != "star-rating"]
        rating_number = BookParser.RATINGS.get(rating_classes[0])
        logger.debug(f"Found book rating: `{rating_number}`.")
        return rating_number
