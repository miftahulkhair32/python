from tkinter import *
from tkinter import messagebox
root = Tk()

class tombolLogin:
    def __init__(self, master):
        frame = Frame(master, width=400, height=300)
        frame.pack()

        self.labelUser = Label(frame, text='Nama User')
        self.labelUser.grid(row=0, column=0, sticky='w')
        self.labelPass = Label(frame, text='Password')
        self.labelPass.grid(row=1, column=0, sticky='w')

        self.entryuser = Entry(frame)
        self.entryuser.grid(row=0, column=1)
        self.entrypass = Entry(frame)
        self.entrypass.grid(row=1, column=1)

        self.checkbutton = Checkbutton(frame, text='ingat saya')
        self.checkbutton.grid(row=2)

        self.buttonLogin = Button(frame, text='masuk', width=20, command=self.klikTombol)
        self.buttonLogin.grid(row=3, columnspan=2)
    def klikTombol(self):
        Username = self.entryuser.get()
        Password = self.entrypass.get()

        if Username == 'admin' and Password == '123':
            messagebox.showinfo('Login', 'login berhasil')
        else:
            messagebox.showerror('Login', 'masukkan username dan password')

ojb = tombolLogin(root)   
root.mainloop()