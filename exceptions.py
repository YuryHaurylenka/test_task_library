class LibraryException(Exception):
    """
    Base exception class for library-related errors.
    """

    def __init__(self, message: str):
        """
        Initialize a library exception.
        :param message: Error message describing the exception.
        """
        super().__init__(message)


class BookNotFoundError(LibraryException):
    """
    Raised when a book with the specified criteria does not exist.
    """

    def __init__(self, details: str):
        """
        Initialize the exception with specific details.
        :param details: Description of the search criteria.
        """
        super().__init__(f"Book not found: {details}")


class DuplicateBookError(LibraryException):
    """
    Raised when attempting to add a book that already exists.
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Initialize the exception with details of the duplicate book.
        :param title: Title of the book.
        :param author: Author of the book.
        :param year: Year of publication.
        """
        super().__init__(f"Book '{title}' by {author} ({year}) already exists.")


class EmptyLibraryError(LibraryException):
    """
    Raised when attempting to perform operations on an empty library.
    """

    def __init__(self):
        """
        Initialize the exception for an empty library.
        """
        super().__init__("The library is empty. Add books to perform this operation.")


class InvalidBookStatusError(LibraryException):
    """
    Raised when an invalid status is provided for a book.
    """

    def __init__(self, status: str):
        """
        Initialize the exception for an invalid status.
        :param status: Provided invalid status.
        """
        valid_statuses = ["available", "checked_out"]
        super().__init__(
            f"Invalid book status '{status}'. Valid statuses are: {', '.join(valid_statuses)}."
        )


class InvalidSearchCriteriaError(LibraryException):
    """
    Raised when invalid search criteria are provided.
    """

    def __init__(self):
        """
        Initialize the exception for invalid search criteria.
        """
        super().__init__(
            "Invalid search criteria. Provide at least one valid search parameter (title, author, or year)."
        )


class BookAlreadyAvailableError(LibraryException):
    """
    Raised when attempting to set a book's status to 'available' when it's already available.
    """

    def __init__(self, book_id: int):
        """
        Initialize the exception for a book already being available.
        :param book_id: ID of the book.
        """
        super().__init__(f"Book with ID {book_id} is already available.")


class BookAlreadyCheckedOutError(LibraryException):
    """
    Raised when attempting to set a book's status to 'checked_out' when it's already checked out.
    """

    def __init__(self, book_id: int):
        """
        Initialize the exception for a book already being checked out.
        :param book_id: ID of the book.
        """
        super().__init__(f"Book with ID {book_id} is already checked out.")
