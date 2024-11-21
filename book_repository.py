from abc import ABC, abstractmethod
from typing import List, Optional

from book_models import Book
from file_utils import load_books, save_books


class BookRepositoryInterface(ABC):
    """
    Interface for book repository to define CRUD operations.
    """

    @abstractmethod
    def get_all_books(self) -> List[Book]:
        pass

    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def delete_book(self, book_id: int) -> bool:
        pass

    @abstractmethod
    def search_books(
        self, title: Optional[str], author: Optional[str], year: Optional[int]
    ) -> List[Book]:
        pass

    @abstractmethod
    def update_book_status(self, book_id: int, new_status: str) -> bool:
        pass


class BookRepository(BookRepositoryInterface):
    """
    Concrete implementation of the BookRepositoryInterface.
    Manages CRUD operations for books stored in a JSON file.
    """

    def __init__(self, file_path: str):
        """
        Initialize the repository with a file path for storing data.
        :param file_path: Path to the JSON file.
        """
        self.file_path = file_path

    def get_all_books(self) -> List[Book]:
        """
        Retrieve all books from the JSON file.
        :return: List of books.
        """
        return load_books(self.file_path)

    def add_book(self, book: Book) -> None:
        """
        Add a new book to the repository.
        :param book: Book instance to add.
        :raises ValueError: If a book with the same ID already exists.
        """
        books = self.get_all_books()
        if any(b.id == book.id for b in books):
            raise ValueError(f"Book with ID {book.id} already exists.")
        books.append(book)
        save_books(self.file_path, books)

    def delete_book(self, book_id: int) -> bool:
        """
        Delete a book by its ID.
        :param book_id: ID of the book to delete.
        :return: True if the book was deleted, False otherwise.
        """
        books = self.get_all_books()
        filtered_books = [book for book in books if book.id != book_id]
        if len(filtered_books) == len(books):
            return False
        save_books(self.file_path, filtered_books)
        return True

    def search_books(
        self,
        title: Optional[str] = None,
        author: Optional[str] = None,
        year: Optional[int] = None,
    ) -> List[Book]:
        """
        Search for books by title, author, or year.
        :param title: Title to search for (optional).
        :param author: Author to search for (optional).
        :param year: Year to search for (optional).
        :return: List of books matching the criteria.
        """
        books = self.get_all_books()
        return [
            book
            for book in books
            if (not title or title.lower() in book.title.lower())
            and (not author or author.lower() in book.author.lower())
            and (not year or book.year == year)
        ]

    def update_book_status(self, book_id: int, new_status: str) -> bool:
        """
        Update the status of a book by its ID.
        :param book_id: ID of the book to update.
        :param new_status: New status to set.
        :return: True if the book was updated, False otherwise.
        """
        books = self.get_all_books()
        for book in books:
            if book.id == book_id:
                book.set_status(new_status)
                save_books(self.file_path, books)
                return True
        return False
