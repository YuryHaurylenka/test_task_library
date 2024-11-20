from enum import Enum
from typing import Any

from exceptions import InvalidBookStatusError


class BookStatus(Enum):
    """Enum for book statuses."""
    AVAILABLE = "available"
    CHECKED_OUT = "checked_out"


class Book:
    """
    Class representing a book in the library.
    """

    def __init__(self, book_id: int, title: str, author: str, year: int, status: str = "available"):
        """
        Initialize a new book instance.
        :param book_id: Unique identifier for the book.
        :param title: Title of the book.
        :param author: Author of the book.
        :param year: Year of publication.
        :param status: Status of the book ("available" or "checked_out").
        """
        self.id = book_id
        self.title = title.strip()
        self.author = author.strip()
        self.year = self.validate_year(year)
        self.set_status(status)

    def set_status(self, status: str) -> None:
        """
        Set the status of the book, ensuring it's valid.
        :param status: New status of the book.
        :raises InvalidBookStatusError: If the status is invalid.
        """
        try:
            self.status = BookStatus(status.lower())
        except ValueError:
            raise InvalidBookStatusError(status)

    @staticmethod
    def validate_year(year: int) -> int:
        """
        Validate the publication year.
        :param year: Year to validate.
        :return: Validated year.
        :raises ValueError: If the year is not positive or not an integer.
        """
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Year must be a positive integer.")
        return year

    def to_dict(self) -> dict[str, Any]:
        """
        Convert the book instance to a dictionary format.
        :return: A dictionary representation of the book.
        """
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status.value,
        }

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "Book":
        """
        Create a book instance from a dictionary.
        :param data: Dictionary containing book data.
        :return: A Book instance.
        """
        return Book(
            book_id=data["id"],
            title=data["title"],
            author=data["author"],
            year=data["year"],
            status=data["status"],
        )


    def __repr__(self) -> str:
        """
        Representation of the book instance.
        :return: String representation of the book.
        """
        return f"Book(id={self.id}, title='{self.title}', author='{self.author}', year={self.year}, status='{self.status.value}')"