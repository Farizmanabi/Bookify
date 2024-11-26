import csv
from tabulate import tabulate

class Book:
    def __init__(self, book_id, title, author, year, category, price):
        self.book_id = book_id
        self.title = title
        self.category = category
        self.author = author
        self.year = year
        self.price = price

    def __str__(self):
        return f"{self.book_id} - {self.title} - {self.category} - {self.author} ({self.year}) - {self.price}"

class ManageBook:
    def __init__(self, file_name="book.csv"):
        self.file_name = file_name
        self.book_list = []
        self.load_data()

    # Load data from CSV
    def load_data(self):
        try:
            with open(self.file_name, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    book = Book(
                        row["ID"], 
                        row["Title"], 
                        row["Author"], 
                        row["Year"], 
                        row["Category"], 
                        row["Price"]
                    )
                    self.book_list.append(book)
        except FileNotFoundError:
            pass  

    # Save data to CSV
    def save_data(self):
        with open(self.file_name, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["ID", "Title", "Author", "Year", "Category", "Price"])
            writer.writeheader()
            for book in self.book_list:
                writer.writerow({
                    "ID": book.book_id,
                    "Title": book.title,
                    "Author": book.author,
                    "Year": book.year,
                    "Category": book.category,
                    "Price": book.price,
                })

    # CREATE
    def add_book(self, book_id, title, author, year, category, price):
        new_book = Book(book_id, title, author, year, category, price)
        self.book_list.append(new_book)
        self.save_data()
        print(f"The book '{title}' has been added successfully")

    # READ
    def read_book(self):
        if not self.book_list:
            print("There are no books on the list.")
        else:
            print("Book List:")
            # Format harga dengan Rp dan tanda koma
            table = [
                [book.book_id, book.title, book.category, book.author, book.year, f"Rp. {int(book.price):,}"]
                for book in self.book_list
            ]
            headers = ["ID", "Title", "Category", "Author", "Year", "Price"]
            print(tabulate(table, headers, tablefmt="grid"))


    # UPDATE
    def update_book(self, book_id, new_title=None, new_category=None, new_author=None, new_year=None, new_price=None):
        for book in self.book_list:
            if book.book_id == book_id:
                if new_title:
                    book.title = new_title
                if new_category:
                    book.category = new_category
                if new_author:
                    book.author = new_author
                if new_year:
                    book.year = new_year
                if new_price:
                    book.price = new_price
                self.save_data()
                print(f"Book with ID '{book_id}' updated successfully!")
                return
        print(f"Book with ID '{book_id}' not found.")

    # DELETE
    def hapus_buku(self, book_id):
        for book in self.book_list:
            if book.book_id == book_id:
                self.book_list.remove(book)
                self.save_data()
                print(f"Book with ID '{book_id}' successfully deleted!")
                return
        print(f"Book with ID '{book_id}' not found.")

    # SEARCH
    def cari_buku(self, keyword):
        result = [book for book in self.book_list if keyword.lower() in book.title.lower() or keyword.lower() in book.category.lower() or keyword.lower() in book.author.lower() or keyword.lower() in book.year.lower() or keyword.lower() in str(book.price).lower()]
        if result:
            print("Search Results:")
            for book in result:
                print(f" - {book}")
        else:
            print(f"No books found with keywords '{keyword}'.")

if __name__ == "__main__":
    manage = ManageBook()

    while True:
        print("\n=== Book Management System ===")
        print("1. Add Book")
        print("2. View Book List")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Search Book")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            year = input("Enter Book Year: ")
            category = input("Enter Book Category: ")
            price = input("Enter Book Price: ")
            manage.add_book(book_id, title, author, year, category, price)
        elif choice == "2":
            manage.read_book()
        elif choice == "3":
            book_id = input("Enter the Book ID to update: ")
            title = input("Enter new Title (leave empty to skip): ")
            category = input("Enter new Category (leave empty to skip): ")
            author = input("Enter new Author (leave empty to skip): ")
            year = input("Enter new Year (leave empty to skip): ")
            price = input("Enter new Price (leave empty to skip): ")
            manage.update_book(book_id, title if title else None, category if category else None, author if author else None, year if year else None, price if price else None)
        elif choice == "4":
            book_id = input("Enter the Book ID to delete: ")
            manage.hapus_buku(book_id)
        elif choice == "5":
            keyword = input("Enter search keyword (title/author/category/year/price): ")
            manage.cari_buku(keyword)
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
