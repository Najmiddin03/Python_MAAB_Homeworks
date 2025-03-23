import json


# Load books data from the JSON file
def load_books():
    try:
        with open('books.json', 'r') as file:
            return json.load(file)['books']
    except FileNotFoundError:
        return []


# Save books data to the JSON file
def save_books(books):
    with open('books.json', 'w') as file:
        json.dump({"books": books}, file, indent=4)


# Add a new book
def add_book(books):
    title = input("Enter book title: ")
    author = input("Enter author: ")
    written_date = input("Enter written date (YYYY-MM-DD): ")
    genre = input("Enter genre: ")

    new_book = {
        "title": title,
        "author": author,
        "written_date": written_date,
        "genre": genre
    }

    books.append(new_book)
    save_books(books)
    print(f"Book '{title}' added successfully.")


# Update existing book information
def update_book(books):
    title = input("Enter the title of the book to update: ")
    for book in books:
        if book['title'].lower() == title.lower():
            print(f"Found book: {book['title']}")
            book['author'] = input(f"Enter new author (current: {book['author']}): ")
            book['written_date'] = input(f"Enter new written date (current: {book['written_date']}): ")
            book['genre'] = input(f"Enter new genre (current: {book['genre']}): ")

            save_books(books)
            print(f"Book '{title}' updated successfully.")
            return

    print(f"Book with title '{title}' not found.")


# Delete a book
def delete_book(books):
    title = input("Enter the title of the book to delete: ")
    for book in books:
        if book['title'].lower() == title.lower():
            books.remove(book)
            save_books(books)
            print(f"Book '{title}' deleted successfully.")
            return

    print(f"Book with title '{title}' not found.")


# Display all books
def display_books(books):
    if not books:
        print("No books available.")
        return

    print("\nBooks in the collection:")
    for index, book in enumerate(books, start=1):
        print(
            f"{index}. Title: {book['title']}, Author: {book['author']}, Written Date: {book['written_date']}, Genre: {book['genre']}")


def main():
    books = load_books()

    while True:
        print("\nMenu:")
        print("1. Add a new book")
        print("2. Update an existing book")
        print("3. Delete a book")
        print("4. Display all books")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_book(books)
        elif choice == '2':
            update_book(books)
        elif choice == '3':
            delete_book(books)
        elif choice == '4':
            display_books(books)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
