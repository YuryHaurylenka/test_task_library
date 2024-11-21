from book_service import BookService
from exceptions import LibraryException


def display_menu() -> str:
    """
    Display the main menu for the library management system.
    :return: User's menu choice.
    """
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Delete Book")
    print("3. Search Book")
    print("4. List All Books")
    print("5. Update Book Status")
    print("6. Exit")
    return input("Enter your choice: ").strip()


def handle_add_book(service: BookService) -> None:
    """
    Handle adding a new book to the library.
    :param service: BookService instance for managing books.
    """
    try:
        title = input("Enter title: ").strip()
        author = input("Enter author: ").strip()

        year_input = input("Enter year: ").strip()
        if not year_input.isdigit() or int(year_input) <= 0:
            print("Invalid year. Please enter a positive integer.")
            return

        year = int(year_input)
        book = service.add_book(title, author, year)
        print(f"Book added: {book.to_dict()}")

    except LibraryException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def handle_delete_book(service: BookService) -> None:
    """
    Handle deleting a book from the library.
    :param service: BookService instance for managing books.
    """
    try:
        book_id = int(input("Enter book ID to delete: ").strip())
        service.delete_book(book_id)
        print("Book deleted successfully.")
    except ValueError:
        print("Invalid ID. Please enter a valid integer.")
    except LibraryException as e:
        print(f"Error: {e}")


def handle_search_books(service: BookService) -> None:
    """
    Handle searching for books in the library.
    :param service: BookService instance for managing books.
    """
    try:
        title = input("Enter title to search (or leave blank): ").strip()
        author = input("Enter author to search (or leave blank): ").strip()
        year_input = input("Enter year to search (or leave blank): ").strip()
        year = int(year_input) if year_input else None
        books = service.search_books(title, author, year)
        print("Books found:")
        for book in books:
            print(book.to_dict())
    except ValueError:
        print("Invalid year. Please enter a valid integer.")
    except LibraryException as e:
        print(f"Error: {e}")


def handle_list_books(service: BookService) -> None:
    """
    Handle listing all books in the library.
    :param service: BookService instance for managing books.
    """
    try:
        books = service.list_books()
        print("All books:")
        for book in books:
            print(book.to_dict())
    except LibraryException as e:
        print(f"Error: {e}")


def handle_update_book_status(service: BookService) -> None:
    """
    Handle updating the status of a book.
    :param service: BookService instance for managing books.
    """
    try:
        book_id = int(input("Enter book ID: ").strip())
        new_status = input("Enter new status ('available' or 'checked_out'): ").strip()
        service.update_book_status(book_id, new_status)
        print("Book status updated successfully.")
    except ValueError:
        print("Invalid ID. Please enter a valid integer.")
    except LibraryException as e:
        print(f"Error: {e}")


def main_menu(service: BookService) -> None:
    """
    Main menu loop for the library management system.
    :param service: BookService instance for managing books.
    """
    while True:
        choice = display_menu()
        if choice == "1":
            handle_add_book(service)
        elif choice == "2":
            handle_delete_book(service)
        elif choice == "3":
            handle_search_books(service)
        elif choice == "4":
            handle_list_books(service)
        elif choice == "5":
            handle_update_book_status(service)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
