from tkinter import *
root = Tk()
root.wm_title('jendela')

Label(root, text="ini merah", width=15, bg='red').place(x=10, y=20)
Label(root, text='biru', width=15, bg='blue').place(x=10, y=40)

root.mainloop()