from tkinter import *
root = Tk()

label1 = Label(root, text='merah', bg='red')
label1.pack(side=RIGHT, expand=1)
label2 = Label(root, text='green', bg='green')
labre = Label(root, text='terd', bg='black')
labre.pack(fill=X)# untuk memperluas objek
label2.pack(side=LEFT)

root.mainloop()