from typing import List, Optional

from book_models import Book, BookStatus
from book_repository import BookRepositoryInterface
from exceptions import (
    BookAlreadyAvailableError,
    BookAlreadyCheckedOutError,
    BookNotFoundError,
    DuplicateBookError,
    EmptyLibraryError,
    InvalidBookStatusError,
)


class BookService:
    """
    Handles business logic for book operations.
    """

    def __init__(self, repository: BookRepositoryInterface):
        """
        Initialize the book service with a repository.
        :param repository: Repository instance for data management.
        """
        self.repository = repository

    def add_book(self, title: str, author: str, year: int) -> Book:
        """
        Add a new book to the library.
        :param title: Title of the book.
        :param author: Author of the book.
        :param year: Year of publication.
        :return: The added book instance.
        :raises DuplicateBookError: If a book with the same title, author, and year already exists.
        """
        books = self.repository.get_all_books()
        if any(
            book.title == title and book.author == author and book.year == year
            for book in books
        ):
            raise DuplicateBookError(title, author, year)

        book_id = max((book.id for book in books), default=0) + 1
        new_book = Book(book_id, title, author, year)
        self.repository.add_book(new_book)
        return new_book

    def delete_book(self, book_id: int) -> None:
        """
        Delete a book by its ID.
        :param book_id: ID of the book to delete.
        :raises BookNotFoundError: If the book does not exist.
        :raises EmptyLibraryError: If the library is empty.
        """
        books = self.repository.get_all_books()
        if not books:
            raise EmptyLibraryError()
        if not any(book.id == book_id for book in books):
            raise BookNotFoundError(f"ID {book_id}")

        self.repository.delete_book(book_id)

    def search_books(
        self,
        title: Optional[str] = None,
        author: Optional[str] = None,
        year: Optional[int] = None,
    ) -> List[Book]:
        """
        Search for books by title, author, or year.
        :param title: Title of the book (optional).
        :param author: Author of the book (optional).
        :param year: Year of publication (optional).
        :return: List of books matching the search criteria.
        :raises EmptyLibraryError: If the library is empty.
        :raises BookNotFoundError: If no books match the search criteria.
        """
        books = self.repository.get_all_books()
        if not books:
            raise EmptyLibraryError()

        results = self.repository.search_books(title, author, year)
        if not results:
            criteria = []
            if title:
                criteria.append(f"title='{title}'")
            if author:
                criteria.append(f"author='{author}'")
            if year:
                criteria.append(f"year={year}")
            raise BookNotFoundError(", ".join(criteria))
        return results

    def list_books(self) -> List[Book]:
        """
        List all books in the library.
        :return: List of all books.
        :raises EmptyLibraryError: If the library is empty.
        """
        books = self.repository.get_all_books()
        if not books:
            raise EmptyLibraryError()
        return books

    def update_book_status(self, book_id: int, new_status: str) -> None:
        """
        Update the status of a book.
        :param book_id: ID of the book to update.
        :param new_status: New status to set ("available" or "checked_out").
        :raises InvalidBookStatusError: If the status is invalid.
        :raises EmptyLibraryError: If the library is empty.
        :raises BookNotFoundError: If the book does not exist.
        :raises BookAlreadyAvailableError: If the book is already available.
        :raises BookAlreadyCheckedOutError: If the book is already checked out.
        """
        if new_status not in [status.value for status in BookStatus]:
            raise InvalidBookStatusError(new_status)

        books = self.repository.get_all_books()
        if not books:
            raise EmptyLibraryError()

        for book in books:
            if book.id == book_id:
                if book.status == new_status:
                    if new_status == BookStatus.AVAILABLE.value:
                        raise BookAlreadyAvailableError(book_id)
                    else:
                        raise BookAlreadyCheckedOutError(book_id)

                self.repository.update_book_status(book_id, new_status)
                return

        raise BookNotFoundError(f"ID {book_id}")
