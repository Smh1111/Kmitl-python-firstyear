
from tkinter import *
from tkinter import messagebox
class circle:
    def __init__(self, window):
        self.window = window
        
        self.canvas = Canvas(
            window, 
            width = 700, 
            height = 700, 
            bg = "light blue"
            )

        self.title = Label(window, width = 8, height= 1, text = "Translator application", font = "Bold 30", bg = "blue", fg='#ffffff')
        self.title.place(x = 580, y = 0, width = 400, height = 60)
        
        


        # menubar = Menu(window)
        # filemenu = Menu(menubar, tearoff=0)
        # filemenu.add_command(label="New",           command = self.donothing)
        # filemenu.add_command(label="Open",          command = self.donothing)
        # filemenu.add_command(label="Save",          command = self.donothing)
        # filemenu.add_command(label="Save as...",    command = self.donothing)
        # filemenu.add_command(label="Close",         command = self.donothing)

      # filemenu.add_separator()

      # filemenu.add_command(label="Exit", command=window.quit)
      # menubar.add_cascade(label="File", menu=filemenu)

        # menubar.place(x = 300, y = 0)
        varList = StringVar(window)
        varList.set("Thai")
        om = OptionMenu(window, varList, "Japanese", "English", "Burmese")
        om.config(width=10)
        om.config(height=2)
        om.config(font= "2")
        om.config(bg='orange')
        om.pack()
        om.place( x = 500, y = 300)

        self.number = StringVar()
        

        self.text = Entry(window, font = "Bold 20", textvariable = self.number, justify="right")
        self.text.place(x = 500, y = 400, width = 200, height = 40)

        self.result = "<Translated text>"
        self.output = Label(window, font = "Bold 15", text = self.result, justify="right")
        self.output.place(x = 850, y = 400, width = 200, height = 40)

        varList = StringVar(window)
        varList.set("English")
        om = OptionMenu(window, varList, "Japanese", "Thai", "Burmese")
        om.config(width=10)
        om.config(height=2)
        om.config(font= "2")
        om.config(bg='orange')
        om.pack()
        om.place( x = 850, y = 300)


        self.menu = Button(window, text = "Translate", width = 10, height= 1, font = "bold 20", fg = "white", bg = "brown", command = self.donothing)
        self.menu.pack(pady=20)
        self.menu.place(x = 700, y = 600)

        self.canvas.pack()
        window.mainloop()
    

    def donothing(self):
     
        messagebox.showinfo("Do nothing", "You pressed 'Translate' button but there is no function about it yet.")
        
        
        
def main():
    window = Tk()
    c = circle(window)

main()