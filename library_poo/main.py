#Main function

from library import Library
from book import Book
from member import Member

def main():
    
    my_library = Library()
    a = Book("A seleção", "Kiera Cass", 361, "Romance")
    b = Member("Anderson")
    my_library.register_book(a)
    my_library.register_member(b)
    c = Member("Anelyse")
    my_library.register_member(c)
    d = Book("A escolha", "Kiera Cass", 351, "Romance")
    my_library.register_book(d)
    my_library.list_books()
    my_library.list_member()

if __name__ == "__main__":
    main()
 