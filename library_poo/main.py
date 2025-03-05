#Main function
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

    #Loop the functionalities
    while True:
        utils.list_menus()
        sleep(1)

        option = utils.input_int("Enter option: ")

        if option == 1:
            sleep(1)
            new_book = Book()
            new_book.new_book()
            my_library.register_book(new_book)
        
        if option == 2:
            sleep(1)
            new_member = Member()
            new_member.new_member()
            my_library.register_member(new_member)
        
        if option == 3:
            sleep(1)
            try:
                resp = my_library.check_availability("Which book do you want to check out? ")
                if resp[0]:
                    print("This book is available!")
                elif resp[0] == False:
                    print("This book is unavailable!")
            except TypeError:
                print(f"The book {resp[1]} not found!")

        if option == 4:
            sleep(1)
            my_library.list_books()

        if option == 5:
            sleep(1)
            my_library.list_members()
        if option == 6:
            my_library.borrow_book()

        if option == 7:
            sleep(1)
            utils.menus("Bye bye, see you later!")
            my_library.save_books()
            my_library.save_members()
            break
            
if __name__ == "__main__":
    main()
 