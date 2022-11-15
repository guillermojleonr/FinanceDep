from tkinter import *
import sqlite3
from tkinter.messagebox import showinfo, askyesno, showwarning
from hamcrest import none

raiz=Tk()
raiz.title("costs entry form")

miFrame=Frame(raiz)
miFrame.pack()

""" ------------------ Functionality ------------ 
Conectar
Salir
"""

myConnection = None
myCursor = None

def connect():
    global myConnection, myCursor
    myConnection = sqlite3.connect("finance")
    myCursor = myConnection.cursor()
    showinfo("Connection", "You have succesfully connected to the database")

def exit():
    confirmation = askyesno("Exit", "Do you want to exit?")
    if confirmation == True:
        raiz.quit()

def create():
    global myCursor, myConnection

    Producto_value = ProductoEntry.get()
    Item_value = ItemEntry.get()
    Cantidad_value = CantidadEntry.get()

    values_list = (Producto_value,Item_value,Cantidad_value)
    
    myCursor.execute("""INSERT INTO usuarios VALUES(NULL,?,?,?);""",values_list) 
    myConnection.commit()

    showinfo("Record created", "You have succesfully created a record")

def clear():
    IdEntry.delete(0,END)
    ProductoEntry.delete(0,END)
    ItemEntry.delete(0,END)

""" ---------------- Menu Bar  -------------"""

menubar = Menu(raiz)
raiz.config(menu=menubar)


BBDDmenu = Menu(menubar,tearoff=0)
BBDDmenu.add_command(label="Connect", command=connect)
BBDDmenu.add_command(label="Exit", command=exit)

Borrarmenu = Menu(menubar,tearoff=0)
Borrarmenu.add_command(label="Clear fields", command=clear)

CRUDmenu = Menu(menubar,tearoff=0)
CRUDmenu.add_command(label="Create", command=create)

menubar.add_cascade(label="BBDD", menu=BBDDmenu)
menubar.add_cascade(label="Borrar", menu=Borrarmenu)
menubar.add_cascade(label="CRUD", menu=CRUDmenu)

#Alternatively to this disposition is to create two frames: one for the labels and fields and another for the buttons 

""" ---------------- Labels  -------------"""
IdLabel= Label(miFrame, text="Id")
IdLabel.grid(row = 1, column = 1, padx= 10, pady=10, columnspan=2)

ProductoLabel= Label(miFrame, text="Producto")
ProductoLabel.grid(row = 2, column = 1, padx= 10, pady=10, columnspan=2)

ItemLabel= Label(miFrame, text="Item")
ItemLabel.grid(row = 3, column = 1, padx= 10, pady=10, columnspan=2)

CantidadLabel= Label(miFrame, text="Cantidad")
CantidadLabel.grid(row = 4, column = 1, padx= 10, pady=10, columnspan=2)


""" ---------------- Fields  -------------"""

IdEntry = Entry(miFrame)
IdEntry.grid(row = 1, column = 3, padx= 10, pady=10, columnspan=4)

ProductoEntry = Entry(miFrame)
ProductoEntry.grid(row = 2, column = 3, padx= 10, pady=10, columnspan=4)

ItemEntry = Entry(miFrame)
ItemEntry.grid(row = 3, column = 3, padx= 10, pady=10, columnspan=4)

CantidadEntry = Entry(miFrame)
CantidadEntry.grid(row = 4, column = 3, padx= 10, pady=10, columnspan=4)
CantidadEntry.config(show="*")

""" ---------------- Buttons line  -------------"""

ButtonCreate = Button(miFrame, text= "Create", width= 6, command=create)
ButtonCreate.grid(row = 7, column = 1, padx= 10, pady=10, columnspan= 1)

raiz.mainloop()