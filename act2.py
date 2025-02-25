#act2
def address_book(): 
    address_book = {}
    
    for x in range(1, 4):
        name = input("Enter your name: ")
        number = int(input("Enter your number: "))
        address_book[name] = number

    print(f"Adress Book: {address_book}")

    search = input("Lookup Name: ")

    if search in address_book:
            print(address_book[search])
    else:
        print("Name not found")

address_book()
    