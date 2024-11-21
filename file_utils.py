import json
from typing import List

from book_models import Book


def load_books(file_path: str) -> List[Book]:
    """
    Load all books from a JSON file.
    :param file_path: Path to the JSON file.
    :return: List of Book instances.
    :raises IOError: If there is an issue with reading the file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return [Book.from_dict(book) for book in data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as e:
        print(f"Warning: Failed to decode JSON. Reason: {e}")
        return []
    except Exception as e:
        raise IOError(f"Unexpected error while loading books: {e}")


def save_books(file_path: str, books: List[Book]) -> None:
    """
    Save all books to a JSON file.
    :param file_path: Path to the JSON file.
    :param books: List of Book instances to save.
    :raises IOError: If there is an issue with writing to the file.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(
                [book.to_dict() for book in books], file, indent=4, ensure_ascii=False
            )
    except Exception as e:
        raise IOError(f"Unexpected error while saving books: {e}")
