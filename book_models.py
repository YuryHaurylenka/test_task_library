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
        :param status: Status of the book.
        """
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> dict:
        """
        Convert the book instance to a dictionary format.
        :return: A dictionary representation of the book.
        """
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data: dict) -> "Book":
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
