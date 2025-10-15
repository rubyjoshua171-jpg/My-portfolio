# Task 1: 
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def toggle_availability(self):
        self.is_available = not self.is_available

    def __str__(self):
        status = "Available" if self.is_available else "Checked Out"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"


# Task 2:
class Member:  
    def __init__(self, name, email):
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format. Please enter a valid email address.")
        
        self.name = name
        self.email = email
        self.borrowed_books = []

    def __str__(self):
        return f"{self.name} ({self.email})"


# Task 3:
class LibrarySystem:
    def __init__(self):
        self.books = []
        self.members = []
        self._seed_data()

    # Task 4: 
    def _seed_data(self):
        sample_books = [
            Book("The Hobbit", "J.R.R. Tolkien", "111"),
            Book("1984", "George Orwell", "222"),
            Book("To Kill a Mockingbird", "Harper Lee", "333"),
            Book("Sing to the Stars", "J.K. Rowling", "456"),
            Book("Atomic Habits", "James Clear", "789012"),
            Book("Peaches", "George Orwell", "345678"),
            Book("The Greatest Showman", "F. Scott Fitzgerald", "565"),
            Book("Harry Potter", "Lewis Carroll", "677")
        ]
        
        sample_members = [
            Member("Alice", "alice@example.com"),
            Member("Bob", "bob@example.com"),
            Member("Ruby", "ruby@example.com"),
            Member("Thandi", "thandi@example.com"),
            Member("Mandy", "mandy@example.com"),
        ]
        
        self.books.extend(sample_books)
        self.members.extend(sample_members)

    # Task 5: 
    def view_books(self):
        print("\n=== Books in Library ===")
        if not self.books:
            print("No books available in the library.")
            return
        
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")

    def search_books(self):
        try:
            query = input("Enter book title or author to search: ").strip()
            if not query:
                print("Search query cannot be empty.")
                return
            
            query_lower = query.lower()
            results = [book for book in self.books 
                      if query_lower in book.title.lower() or query_lower in book.author.lower()]
            
            if results:
                print(f"\n=== Search Results for '{query}' ===")
                for i, book in enumerate(results, 1):
                    print(f"{i}. {book}")
            else:
                print(f"No books found matching '{query}'. Please try a different search term.")
                
        except KeyboardInterrupt:
            print("\nSearch cancelled.")

    def add_member(self):
        try:
            name = input("Enter member name: ").strip()
            if not name:
                print("Name cannot be empty.")
                return
                
            email = input("Enter member email: ").strip()
            if not email:
                print("Email cannot be empty.")
                return
            
            if any(member.email.lower() == email.lower() for member in self.members):
                print("Error: A member with this email already exists.")
                return
            new_member = Member(name, email)
            self.members.append(new_member)
            print(f"Member '{name}' added successfully!")
            
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nMember registration cancelled.")

    def find_member_by_email(self, email):
        return next((member for member in self.members if member.email.lower() == email.lower()), None)

    def find_book_by_isbn(self, isbn):
        return next((book for book in self.books if book.isbn == isbn), None)

    def checkout_book(self):
        try:
            email = input("Enter member email: ").strip()
            if not email:
                print("Email cannot be empty.")
                return
            
            member = self.find_member_by_email(email)
            if not member:
                print("Error: Member not found. Please check the email address.")
                return

            isbn = input("Enter book ISBN: ").strip()
            if not isbn:
                print("ISBN cannot be empty.")
                return
                
            book = self.find_book_by_isbn(isbn)
            if not book:
                print("Error: Book not found. Please check the ISBN.")
                return
                
            if not book.is_available:
                print(f"Sorry, '{book.title}' is already checked out.")
                return

            book.toggle_availability()
            member.borrowed_books.append(book)
            
            print(f"Success! {member.name} checked out '{book.title}'.")
            
        except KeyboardInterrupt:
            print("\nCheckout cancelled.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def return_book(self):
        try:
            email = input("Enter member email: ").strip()
            if not email:
                print("Email cannot be empty.")
                return
                
            member = self.find_member_by_email(email)
            if not member:
                print("Error: Member not found. Please check the email address.")
                return

            if not member.borrowed_books:
                print(f"{member.name} has no books to return.")
                return

            isbn = input("Enter book ISBN to return: ").strip()
            if not isbn:
                print("ISBN cannot be empty.")
                return
                
            book = next((book for book in member.borrowed_books if book.isbn == isbn), None)
            if not book:
                print("Error: This member did not borrow a book with that ISBN.")
                return
            
            book.toggle_availability()
            member.borrowed_books.remove(book)

            print(f"Success! {member.name} returned '{book.title}'.")
            
        except KeyboardInterrupt:
            print("\nReturn cancelled.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def add_book(self):
        try:
            title = input("Enter book title: ").strip()
            if not title:
                print("Title cannot be empty.")
                return
                
            author = input("Enter book author: ").strip()
            if not author:
                print("Author cannot be empty.")
                return
                
            isbn = input("Enter book ISBN: ").strip()
            if not isbn:
                print("ISBN cannot be empty.")
                return
            
            if any(book.isbn == isbn for book in self.books):
                print("Error: A book with this ISBN already exists.")
                return
            
            new_book = Book(title, author, isbn)
            self.books.append(new_book)
            print(f"Book '{title}' by {author} added successfully!")
            
        except KeyboardInterrupt:
            print("\nBook addition cancelled.")

    def view_members(self):
        print("\n=== Library Members ===")
        if not self.members:
            print("No members registered.")
            return
            
        for i, member in enumerate(self.members, 1):
            borrowed_count = len(member.borrowed_books)
            print(f"{i}. {member} - Books borrowed: {borrowed_count}")
            if member.borrowed_books:
                for book in member.borrowed_books:
                    print(f"   - {book.title}")

    # Task 6: Main program loop
    def run(self):
        print("Welcome to the Library Management System!")
        
        while True:
            try:
                print("\n" + "="*40)
                print("    LIBRARY MANAGEMENT SYSTEM")
                print("="*40)
                print("1. View All Books")
                print("2. Search Books")
                print("3. Add Member")
                print("4. Add Book")
                print("5. Checkout Book")
                print("6. Return Book")
                print("7. View Members")
                print("8. Exit")
                print("-"*40)

                choice = input("Choose an option (1-8): ").strip()

                if choice == "1":
                    self.view_books()
                elif choice == "2":
                    self.search_books()
                elif choice == "3":
                    self.add_member()
                elif choice == "4":
                    self.add_book()
                elif choice == "5":
                    self.checkout_book()
                elif choice == "6":
                    self.return_book()
                elif choice == "7":
                    self.view_members()
                elif choice == "8":
                    print("\nThank you for using the Library Management System!")
                    print("Goodbye, BOOKWORM! Have a great day!")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1-8.")
                    
            except KeyboardInterrupt:
                print("\n\nProgram interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                print("Please try again.")


def main():
    library = LibrarySystem()
    library.run()


if __name__ == "__main__":
    main()

