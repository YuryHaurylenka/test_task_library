from typing import List
from book_models import Book
from file_utils import load_books, save_books


class BookRepository:
    """
    Basic repository for managing books in a JSON file.
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
        """
        books = self.get_all_books()
        books.append(book)
        save_books(self.file_path, books)

    def delete_book(self, book_id: int) -> None:
        """
        Delete a book by its ID.
        :param book_id: ID of the book to delete.
        """
        books = self.get_all_books()
        books = [book for book in books if book.id != book_id]
        save_books(self.file_path, books)
