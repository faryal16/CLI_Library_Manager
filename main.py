import json
import os

# File to store book data
BOOKS_FILE = "books.json"

# Initialize books list
def load_books():
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "r") as file:
            return json.load(file)
    return [
        {"title": "Atomic Habits", "author": "James Clear", "category": "Self-Help", "status": "Read"},
        {"title": "The Pragmatic Programmer", "author": "Andrew Hunt", "category": "Programming", "status": "Unread"},
        {"title": "Deep Work", "author": "Cal Newport", "category": "Productivity", "status": "Read"},
         {"title": "The Psychology of Money", "author": "Morgan Housel", "category": "Finance", "status": "Unread", },
        {"title": "Thinking, Fast and Slow", "author": "Daniel Kahneman", "category": "Psychology", "status": "Read", },
        
    ]

def save_books(books):
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)

# Display all books
def display_books():
    books = load_books()
    if not books:
        print("📚 No books available.")
        return
    print("\n📖 Your Book Collection:\n")
    for i, book in enumerate(books, start=1):
        print(f"{i}. {book['title']} by {book['author']} - {book['category']} [{book['status']}]")

# Search books by title or author
def search_books():
    books = load_books()
    query = input("🔍 Enter book title or author: ").strip().lower()
    results = [book for book in books if query in book['title'].lower() or query in book['author'].lower()]
    
    if results:
        print("\n🔎 Search Results:\n")
        for book in results:
            print(f"- {book['title']} by {book['author']} [{book['status']}]")
    else:
        print("⚠️ No matching books found.")

# Add a new book
def add_book():
    books = load_books()
    title = input("📖 Enter book title: ").strip()
    author = input("✍️ Enter author name: ").strip()
    category = input("📂 Enter book category: ").strip()
    status = input("📌 Reading status (Read/Unread): ").strip()

    if title and author and category and status in ["Read", "Unread"]:
        books.append({"title": title, "author": author, "category": category, "status": status})
        save_books(books)
        print(f"✅ '{title}' added successfully!")
    else:
        print("⚠️ Please enter valid details.")

# Remove a book
def remove_book():
    books = load_books()
    display_books()
    
    if not books:
        return
    
    try:
        choice = int(input("🗑️ Enter book number to remove: ")) - 1
        if 0 <= choice < len(books):
            removed_book = books.pop(choice)
            save_books(books)
            print(f"✅ '{removed_book['title']}' removed successfully!")
        else:
            print("⚠️ Invalid selection.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# Dashboard: Count Read vs. Unread books
def dashboard():
    books = load_books()
    read_books = sum(1 for book in books if book["status"] == "Read")
    unread_books = sum(1 for book in books if book["status"] == "Unread")

    print("\n📊 Library Dashboard")
    print(f"✅ Read Books: {read_books}")
    print(f"📌 Unread Books: {unread_books}")
    print(f"📚 Total Books: {len(books)}")

# Main Menu
def main():
    while True:
        print("\t\n📚 Library Manager CLI\n")
        print(" 1️⃣   - View Books")
        print(" 2️⃣   - Search Books")
        print(" 3️⃣   - Add a Book")
        print(" 4️⃣   - Remove a Book")
        print(" 5️⃣   - Dashboard")
        print(" 0️⃣   - Exit")

        choice = input("\nEnter your choice: \n").strip()

        if choice == "1":
            display_books()
        elif choice == "2":
            search_books()
        elif choice == "3":
            add_book()
        elif choice == "4":
            remove_book()
        elif choice == "5":
            dashboard()
        elif choice == "0":
            print("👋 Exiting Library Manager. Happy Reading!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
