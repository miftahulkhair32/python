from tkinter import *
from tkinter import messagebox
root = Tk()

def klikTombol():
    Username = entryuser.get()
    Password = entrypass.get()

    if Username == 'admin' and Password == '123':
        messagebox.showinfo('Login', 'login berhasil')
    else:
        messagebox.showerror('Login', 'masukkan username dan password')
        
frame = Frame(root, width=400, height=300)
frame.pack()

labelUser = Label(frame, text='Nama User')
labelUser.grid(row=0, column=0, sticky='w')
labelPass = Label(frame, text='Password')
labelPass.grid(row=1, column=0, sticky='w')

entryuser = Entry(frame)
entryuser.grid(row=0, column=1)
entrypass = Entry(frame)
entrypass.grid(row=1, column=1)

checkbutton = Checkbutton(frame, text='ingat saya')
checkbutton.grid(row=2)

buttonLogin = Button(frame, text='masuk', width=20, command=klikTombol)
buttonLogin.grid(row=3, columnspan=2)

root.mainloop()