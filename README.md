# 📚 Library Manager CLI

Library Manager CLI is a simple command-line application to manage your book collection. It allows users to **view, search, add, and remove books**, as well as track their reading status.

## 🚀 Features
- 📖 View all books in your collection
- 🔍 Search books by title or author
- ➕ Add new books with category and status
- 🗑️ Remove books from the collection
- 📊 View reading statistics (Read vs. Unread books)
- 💾 Data persistence using a JSON file

## 🛠 Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/faryal16/ST_Library_Manager.git
   ```
2. Navigate to the project directory:
   ```sh
   cd ST_Library_Manager
   ```
3. Ensure you have Python installed (>= 3.x).

## ▶️ Usage
Run the script:
```sh
python main.py
```
You'll see a menu like this:
```
📚 Library Manager CLI

 1️⃣   - View Books
 2️⃣   - Search Books
 3️⃣   - Add a Book
 4️⃣   - Remove a Book
 5️⃣   - Dashboard
 0️⃣   - Exit
```

### 📝 Example Commands
#### ➕ Add a Book
1. Choose **3** from the menu.
2. Enter book details when prompted:
   ```
   📖 Enter book title: Deep Work
   ✍️ Enter author name: Cal Newport
   📂 Enter book category: Productivity
   📌 Reading status (Read/Unread): Read
   ✅ 'Deep Work' added successfully!
   ```

#### 🔍 Search for a Book
1. Choose **2** from the menu.
2. Enter the book title or author name.
   ```
   🔍 Enter book title or author: Atomic Habits
   🔎 Search Results:
   - Atomic Habits by James Clear [Read]
   ```

#### 📊 View Dashboard
1. Choose **5** from the menu.
   ```
   📊 Library Dashboard
   ✅ Read Books: 3
   📌 Unread Books: 2
   📚 Total Books: 5
   ```

## 🛠 Troubleshooting
**Issue: JSON Decode Error**
- If you get an error like `json.decoder.JSONDecodeError`, delete `books.json` and restart the program.

## 📜 License
This project is open-source and available under the **MIT License**.

---
🚀 Happy Reading! 😊

