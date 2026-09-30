def dashboard():
    print("=" * 40)
    print("📚  YOUR LIBRARY")
    print("=" * 40)
    

def estimate_reading_time(pages):
    return round(pages / 40, 1)

def add_book(library):
    title = input("Book title: ").title()
    author = input("Author: ")
    pages = int(input("Page count: ")) 
    hours = estimate_reading_time(pages)

    book = {
        "title": title,
        "author": author,
        "pages": pages,
        "hours": hours,
    }
    library.append(book)

    print(f"Book added: '{title}' by {author} -- approx. {hours} hours to read")

def view_books(library):
    if not library:
        print("Your library is empty. Add a book first!")
        return
    for i in range(len(library)):
        book = library[i]
        print (f"{i + 1}. '{book['title']}' - {book['author']} ({book['pages']} pages - approx. {book['hours']:.1f} hours to read)")

def show_menu():
    print("""
    What would you like to do?
    
    1) View books
    2) Add a book
    
    q) Quit
    
    """)
    choice = input("> ")
    return choice.strip().lower()

def main():
    dashboard()
    library = []
    show_menu_first = True

    while True:
        choice = show_menu()

        if choice == "1":
            view_books(library)
        elif choice == "2":
            add_book(library)
        elif choice in ("q", "quit", "exit"):
            print("Goodbye!")
            break
        else:
            print("Sorry, that option isn't available.")

if __name__ == "__main__":
    main()