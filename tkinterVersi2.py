# membuat GUI dalam bentuk python versi 2
from Tkinter import *
# objek pertama pada python2
root = Tk()
# jandela utama
root.wm_title("test")
''' rowspan untuk jumlah baris '''
frame1 = Frame(root, width=200, height=100, bg='red')
frame1.grid(row=0, column=0, rowspan=3, padx=10, pady=10)

frame2 = Frame(root, width=100, height=50, bg='blue')
frame2.grid(row=0, column=1, padx=5, pady=5, sticky='n')
# untukan membuat input di GUI
entry1 = Entry(root)
entry1.grid(row=1, column=1)
entry2 = Entry(root)
entry2.grid(row=2, column=1)
# perintah menjalankan jendela
root.mainloop()