from tkinter import filedialog 
import pickle
import tkinter as tk
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
def main():
    Phone_book = {"soe moe":"1234332", "Peter":"170812712", "John":"45553"}

    
    print("Phonebook Manager")
    print('Press "+" to add a new contact.')
    print('Press "-" to delete a contact.')
    print('Press "f" to find a contact.')
    print('Press "s" to save all contact to a file.')
    print('Press "p" to print out all contacts in the phonebook.')
    print('Press "q" to quit the program.')
    print()
        

    char = input("")

    while(char != "q"):

        try:
            if char != '+' and char != '-' and char != 'f' and char != 's' and char != 'p' and char != 'q':
                raise ValueError


            elif char == "+":
                name = input("Enter name: ")
                ph_no = input("Enter ph no: ")
                Phone_book[name] = ph_no

            elif char == "-":
                name = input("Enter a contact name to delete a contact: ")
                Phone_book.pop(name)


            elif char == "f":
                contact_name = input("Enter a contact name to find whether it exists or not.\n")
                for key in Phone_book:
                    if (key == contact_name):
                        print(key + " : " + str(Phone_book[key]))

                    file = open(filepath,'wb')
                    pickle.dump(str(Phone_book), file)
                    file.close()
            elif char == "s":

                try:
                    window = tk.Tk()
                    window.withdraw()
                    filepath = filedialog.asksaveasfilename(title="Save a Text File", filetypes=(("text files","*.txt"), ("all files","*.*")))
                    file = open(filepath, "w")
                    file.write(str(Phone_book))
                    file.close()   

                except:
                    print("wrong")


            elif char == "l":
                filepath = filedialog.askopenfilename(title="Open a Text File", filetypes=(("text files","*.txt"), ("all files","*.*")))
                with open(filepath,'rb') as file:
                    contents = pickle.load(file)
                    print(str(contents))



                file.close()     


            elif char == "p":
                for key in Phone_book:
                    print(key + " : " + str(Phone_book[key]), end = ", ")




            print()
            char = input("")

            
        except:

            print("No charater")


main()