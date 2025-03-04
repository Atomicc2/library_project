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
    d = Book("A Escolha", "Kiera Cass", 351, "Romance")
    my_library.register_book(d)
    my_library.list_books()
    my_library.list_member()
    livro = 'A seleção'
    status = my_library.check_availability(livro)
    if status is True:
        print(f"The book {livro} is available!")
    else:
        print(f"The book {livro} isn't available!")

if __name__ == "__main__":
    main()
 