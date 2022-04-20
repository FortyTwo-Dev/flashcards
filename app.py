from imp import reload
import random
from tkinter import*
import tkinter as tk
from tkinter import messagebox
import tkinter
import webbrowser

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.entrythingy = tk.Entry(width=45, bg='#a2a2a6')
        self.entrythingy.pack(fill="both",padx=10, pady=8, side="left" and "top")

        self.entrythingy2 = tk.Entry(width=45, bg='#a2a2a6')
        self.entrythingy2.pack(fill="both",padx=10, pady=8,side="right" and "top")

        self.contents1 = tk.StringVar()
        self.text_1 = tk.StringVar()

        self.contents2 = tk.StringVar()
        self.text_2 = tk.StringVar()

        self.contents1.set("new")
        self.contents2.set("new")

        # Creation d'un menu
        self.mainMenu = tk.Menu()

        # première partie du menu
        self.firstMenu = tk.Menu(self.mainMenu, tearoff=0)
        
        self.firstMenu.add_command(label="My Github", command=lambda: webbrowser.open("https://github.com/Titi0603"))
        self.firstMenu.add_command(label="My Modpack Minecraft", command=lambda: webbrowser.open("https://www.curseforge.com/minecraft/modpacks/cyber-craft"))
        self.firstMenu.add_command(label="Diavo", command=lambda: webbrowser.open("https://www.youtube.com/channel/UCgVFOK24H2TZOv2AqGZgJIw/featured"))
        self.firstMenu.add_command(label="Quitter", command=self.master.quit)

        # deuxième partie du menu
        self.secondMenu = tk.Menu(self.mainMenu, tearoff=0)

        self.secondMenu.add_command(label="Go to choice flashcarg aléa")

        # ajout des menus
        self.mainMenu.add_cascade(label="Menu", menu=self.firstMenu)
        self.mainMenu.add_cascade(label="play", menu=self.secondMenu)
        # fonction syncrho text inserte_Text
        def update_Text(*args):
          self.text_1.set(self.contents1.get())
          self.text_2.set(self.contents2.get())

        # fonction verifictaion
        def butAction():
          reponse = messagebox.askquestion(title="attention", message="what")
          if reponse == 'yes':
            ficverify = open("variable/flashcardsnomber.txt", "r", encoding="utf-8")
            i = ficverify.read()
            i = int(i)
            i = i + 1
            i = str(i)
            ficverify.close()
            ficadd = open("variable/flashcardsnomber.txt", "w", encoding="utf-8")
            ficadd.write(i)
            print(i)
            FlashCA = open("flashcards/"+ i+ "a.txt", "x", encoding="utf-8")
            FlashCB = open("flashcards/"+ i+ "b.txt", "x", encoding="utf-8")
            self.contents1 = str(self.contents1.get())
            self.contents2 = str(self.contents2.get())
            a = FlashCA.write(self.contents1)
            b = FlashCB.write(self.contents2)
            ficadd.close()
            self.contents1 = tk.StringVar()
            self.contents2 = tk.StringVar()
            

        self.entrythingy["textvariable"] = self.contents1
        self.entrythingy2["textvariable"] = self.contents2

        # add botton
        self.bottom = tk.Button(fg='black', font=("A"), command=butAction, width=4, height=1, text="save")
        self.bottom.pack(padx=10, pady=8)
        
        # va avec butAction
        self.text_1.trace("w", update_Text)
        self.text_2.trace("w", update_Text)
        separ = "-"*200
        # affichage du text
        self.master.text_1 = Message(fg='black', textvariable=self.contents1, font=("Arial", 15), bg='#a2a2a6')
        self.master.text_0 = Label(fg='black', text=separ, font=("Arial", 15), bg='#a2a2a6')
        self.master.text_2 = Message(fg='black', textvariable=self.contents2, font=("Arial", 15), bg='#a2a2a6')
        
       
# réglage
myapp = App()

myapp.master.title("FlashCardsCreator")
myapp.master.minsize(600, 600)
myapp.master.maxsize(1200, 600)
myapp.master.config(bg='#a2a2a6')
myapp.master.text_1.pack(expand=1)
myapp.master.text_0.pack()
myapp.master.text_2.pack(expand=1)

myapp.master.config(menu = myapp.mainMenu)
myapp.mainloop()

# myFile = open(".txt", "w")

# myFile.write("")

# myFile.close()

"""
génération aléatoire
nombre aléatoire
Lettre aléatoire

aléa + aléaLettre + ".txt"

lecture avec r

du premier fichier puis lecture du deuxième 
condition
  if a ou b:
    a 
    OR
    b


random
"""
