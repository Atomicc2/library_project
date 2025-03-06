from time import sleep

from library import Library
from book import Book
from member import Member
import utils

def main():
    #creation the library
    utils.menus("WELCOME TO YOUR LIBRARY")
    sleep(1)

    name_library = input("What is the name of your library? ").lower()
    my_library = Library(name_library)
    my_library.load_books()
    my_library.load_members()
    sleep(1)

    utils.menus(f"Congratulations, the library '{my_library.name}' created! ")
    sleep(1)

    #Options and functions
    options = {
        1: lambda: (sleep(1), new_book := Book(), new_book.new_book(), my_library.register_book(new_book)),
        2: lambda: (sleep(1), new_member := Member(), new_member.new_member(), my_library.register_member(new_member)),
        3: lambda: (sleep(1), my_library.show_status()),
        4: lambda: (sleep(1), my_library.list_books()),
        5: lambda: (sleep(1), my_library.list_members()),
        6: lambda: (sleep(1), my_library.borrow_book()),
        7: lambda: (sleep(1), my_library.return_book()),
        8: lambda: (sleep(1), my_library.exit_library()),
    }
    #main program
    while True:
        utils.list_menus()
        sleep(1)
        resp = utils.input_int("Enter option: ")
        utils.simple_lines()
        
        action = options.get(resp)

        if action:
            action()
        else:
            print("Invalid option, tru again!")
            
if __name__ == "__main__":
    main()
 