from tkinter import *

def jendelaBaru():
    window = Toplevel(root)

root = Tk()
tombol = Button(root, text='klik untuk menampilkan jendela', command=jendelaBaru)
tombol.pack()

root.mainloop()