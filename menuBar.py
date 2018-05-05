from tkinter import *
root = Tk()

menuBar = Menu(root)
fileMenu = Menu(menuBar)
fileMenu.add_command(label='New')
fileMenu.add_command(label='Open')
fileMenu.add_command(label='Save')
fileMenu.add_command(label='Exit')

menuBar.add_cascade(label='File', menu=fileMenu)

root.config(menu=menuBar)
root.mainloop()