from tkinter import *
from resourcepacksha1 import resourcePackSHA1
from tkinter import messagebox
from pyperclip import copy
from os.path import isdir, isfile


def createWindow(name, geometry):
    window = Tk()
    window.title(name)
    window.geometry(geometry)
    window.iconbitmap("icone.ico")
    window.resizable(False, False)
    window.eval('tk::PlaceWindow . center')

    # ajout d'un menu en haut de l'écran
    menu_bar = Menu(window)

    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Quitter", command=window.destroy)
    menu_bar.add_cascade(label="Fichier", menu=file_menu)
    window.config(menu=menu_bar, background="#41B77F")

    return window


mainWindow = createWindow("Aide Minecraft", "400x130")
currentWindow = mainWindow


def windowMainMenu():
    global currentWindow

    currentWindow.destroy()
    window = createWindow("Aide Minecraft", "400x130")

    currentWindow = window

    buttonRP = Button(window, text="Resource Pack SHA-1", command=windowRPSHA1, bg="gray")
    buttonRP.pack(side=TOP, pady=20)

    window.mainloop()


filename = Entry()


def copySHA1():
    global filename
    if filename.get() == "":
        messagebox.showerror("Erreur", "Merci de mettre un emplacement de ficher ou de dossier valide.")
    elif isdir(filename.get()) or isfile(filename.get()):
        copy(resourcePackSHA1(filename.get()))
        messagebox.showinfo("Information", "Le SHA-1 a été mis dans votre presse-papier.")
    else:
        messagebox.showerror("Erreur", "Merci de mettre un emplacement de ficher ou de dossier valide.")


def windowRPSHA1():
    global filename, currentWindow
    currentWindow.destroy()

    windowRP = createWindow("Resource Pack SHA-1", "400x150")
    currentWindow = windowRP

    entryAccessPath = Entry(windowRP)
    filename = entryAccessPath
    entryAccessPath.pack(side=TOP, pady=20)

    buttonValidate = Button(windowRP, text="Valider", command=copySHA1, bg="gray")
    buttonValidate.pack(side=TOP, pady=5)

    buttonBack = Button(windowRP, text="Retour", command=windowMainMenu, bg="gray")
    buttonBack.pack(side=TOP)

    windowRP.mainloop()


buttonRPSHA1 = Button(mainWindow, text="Resource Pack SHA-1", command=windowRPSHA1, bg="gray")
buttonRPSHA1.pack(side=TOP, pady=20)

mainWindow.mainloop()
