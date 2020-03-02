import re
import logging
from bs4 import BeautifulSoup
from locators.books_page_locators import BooksPageLocator
from parsers.book import BookParser

logger = logging.getLogger("scraping.books_page")


class BooksPage:
    def __init__(self, page):
        logger.debug("Parsing the page content with BeautifulSoup HTML Parser")
        self.soup = BeautifulSoup(page, "html.parser")

    @property
    def books(self):
        locator = BooksPageLocator.BOOKS
        book_tags = self.soup.select(locator)
        logger.debug(f"Finding all books in the page using `{BooksPageLocator.BOOKS}`.")
        return [BookParser(e) for e in book_tags]

    @property
    def page_count(self):
        logger.debug("Finding the number of catalogue pages available...")
        content = self.soup.select_one(BooksPageLocator.PAGER).string
        logger.info(f"Found number of catalogue pages available: `{content.strip()}`")
        pattern = "Page [0-9]+ of ([0-9]+)"
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        logger.debug(f"Extracted no. of pages as integers: `{pages}`.")
        return pages
