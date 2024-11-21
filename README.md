# Library Management System

A simple console-based application for managing a library of books. The application allows users to add, delete, search,
update, and list books stored in a JSON file.

---

## Features

- **Add Book**: Add a new book to the library with a title, author, and year of publication.
- **Delete Book**: Remove a book from the library by its ID.
- **Search Books**: Search for books by title, author, or year of publication.
- **List All Books**: Display all books in the library along with their details.
- **Update Book Status**: Change the status of a book (`available` or `checked_out`).
- **Persistent Storage**: Books are stored in a JSON file, ensuring data persistence between sessions.
- **Error Handling**: Handles invalid inputs and operations gracefully with user-friendly messages.

---

## Requirements

- **Python**: Version 3.8 or higher.

---

## Installation

### 1. Clone the repository
Run the following command to clone the repository:
```bash
git clone https://github.com/YuryHaurylenka/test_task_library
```

### 2. Set up a virtual environment
The steps for creating a virtual environment differ slightly between Windows and Linux/macOS.

#### **On Windows**:
1. Run the following command to create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   ```bash
   .\venv\Scripts\activate
   ```

#### **On Linux/macOS**:
1. Run the following command to create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
2. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

### 3. Run the application
Once the virtual environment is activated, you can run the application using the following command:
```bash
python main.py
```

---


## Usage

1. **Run the application**:
   ```bash
   python main.py
   ```

2. **Navigate the menu**:
   Use the console-based menu to manage the library. Options include adding, deleting, searching, updating, and listing
   books.

---

## File Structure

```
library-management-system/
├── book_models.py          # Defines the Book model with validations and serialization
├── book_repository.py      # Implements data storage and retrieval logic
├── book_service.py         # Handles business logic for library operations
├── file_utils.py           # Provides functions for reading and writing JSON data
├── interface.py            # Implements the user interface and menu logic
├── main.py                 # Entry point of the application
├── exceptions.py           # Custom exceptions for better error handling
└── README.md               # Project documentation
```

---

## Example Menu Flow

1. **Start the application**:
   ```
   Library Management System
   1. Add Book
   2. Delete Book
   3. Search Book
   4. List All Books
   5. Update Book Status
   6. Exit
   ```

2. **Add a Book**:
   ```
   Enter title: The Great Gatsby
   Enter author: F. Scott Fitzgerald
   Enter year: 1925
   Book added: {'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925, 'status': 'available'}
   ```

3. **List Books**:
   ```
   All books:
   {'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925, 'status': 'available'}
   ```

4. **Update Book Status**:
   ```
   Enter book ID: 1
   Enter new status ('available' or 'checked_out'): checked_out
   Book status updated successfully.
   ```

---

## Error Handling

- **Invalid Inputs**: The program checks for valid inputs (e.g., year must be a positive integer).
- **Non-existent Books**: Attempts to delete or update a book that doesn't exist will display an appropriate error
  message.
- **Empty Library**: Operations on an empty library (e.g., listing books) are gracefully handled.
