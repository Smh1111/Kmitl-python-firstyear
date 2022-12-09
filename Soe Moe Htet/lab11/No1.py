def main():
    Phone_book = {"soe":"1234332", "Peter":"170812712"}

    print("Phonebook Manager")
    print('Press "+" to add a new contact.')
    print('Press "-" to delete a contact.')
    print('Press "f" to find a contact.')
    print('Press "p" to print out all contacts in the phonebook.')
    print('Press "q" to quit the program.')
    print()

    char = input("")

    while(char != "q"):
        if char == "+":
            name = input("Enter name: ")
            ph_no = input("Enter ph no: ")
            Phone_book[name] = ph_no

        if char == "-":
            name = input("Enter a contact name to delete a contact: ")
            Phone_book.pop(name)


        if char == "f":
            contact_name = input("Enter a contact name to find whether it exists or not.\n")
            for key in Phone_book:
                if (key == contact_name):
                    print(key + " : " + str(Phone_book[key]))



        if char == "p":
            for key in Phone_book:
                print(key + " : " + str(Phone_book[key]), end = ", ")


        print()
        char = input("")





main()