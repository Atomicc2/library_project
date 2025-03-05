def check_information(obj):
    #Display information about a book or a member      
    for k, v in obj.__dict__.items():
        print(f"{k}: {v}")

def colors(text):
    list_colors = {
        'colorless': '\033[m',
        'blue': '\033[1;36m'
    }
    return f"{list_colors['blue']}{text}{list_colors['colorless']}"

def simple_lines(int=30):
    print("-" * int)

def menus(text):
    simple_lines(len(text) + 10)
    print(f"     {colors(text)}")
    simple_lines(len(text) + 10)

def list_menus():
    list_menus = {
        1: 'Register a new book',
        2: 'Register a new member',
        3: 'Check the availability', 
        4: 'List all the books',
        5: 'List all the members',
        6: 'Exit program',
    }
    simple_lines(30)
    for k, v in list_menus.items():
        print(f"[ {k} ] - {v}")
    simple_lines(30)

def erro_invalid_input():
    print(f"\033[0;31;40mERROR! Invalid input!\033[m")

def input_str(msg):
    while True:
        try:
            n = str(input(msg)).strip()   
        except (ValueError, TypeError, InterruptedError):
            erro_invalid_input()
        else:
            return n 

def input_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError, InterruptedError):
            erro_invalid_input()
        else:
            return n