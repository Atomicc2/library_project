#Main function

from library import Library
from book import Book
from member import Member

def main():
    
    andinho = Library('Andinho')

    aSelecao = Book('A seleção', 'Kiera Cass', 'Romance', 360)
    aEscolha = Book('A escolha', 'Kiera cass', 'Romance', 260)

    anderson = Member('Anderson')
    anelyse = Member('Anelyse')

    andinho.register_book(aSelecao)
    andinho.register_book(aEscolha)
    andinho.register_member(anderson)
    andinho.register_member(anelyse)

    andinho.list_books()
    andinho.list_members()

    x = andinho.check_availability('A escolha')
    if x == True:
        print("Available")
    else:
        print("Isn't available")
    
    anderson.borrow_book('A escolha')
    andinho.set_availability('A escolha')

    x = andinho.check_availability('A escolha')
    if x == True:
        print("Available")
    else:
        print("Isn't available")

if __name__ == "__main__":
    main()
 