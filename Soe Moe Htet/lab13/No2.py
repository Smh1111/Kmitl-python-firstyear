from tkinter import filedialog 
import pickle
import tkinter as tk
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename

def main():
    try:
        window = tk.Tk()
        window.withdraw()
        filename = input("Enter a file name: ")
        file = open(filename, "r")

        contents = file.read()

        try:
            string = input("Enter the old string to be replaced: ")
            string1 = input("Enter the new string to be replace the old string: ")

            if (string == string1):

                raise ValueError

        except ValueError:
            print("Error! Same input string")
            
        #list = contents.split()
        #for i in range(len(li
        # st)):
        #    print(list[i])
        #    if (list[i] == string):
        #        list[i] = string1
        #        print(string1)

        #contents = " ".join(list)

        contents = contents.replace(string, string1)
        file = open(filename, "w")
        file.write(str(contents))
        print("Done")
        file.close()

    except FileNotFoundError:
        print("File doesn't exist.")

main()