from book_repository import BookRepository
from book_service import BookService
from interface import main_menu


def main() -> None:
    """
    Entry point for the Library Management System.
    Initializes dependencies and starts the main menu.
    """
    # Path to the JSON file for storing book data
    file_path = "data.json"

    # Initialize repository and service
    repository = BookRepository(file_path)
    service = BookService(repository)

    # Start the main menu
    main_menu(service)


if __name__ == "__main__":
    main()
