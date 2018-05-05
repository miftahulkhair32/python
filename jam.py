# untuk jalan di versi 2 harus Tkinter
import Tkinter as tk # mengimport tampilan
from time import strftime # modul waktu

class JendelaUtama: # kelas utama
    def __init__(self):
        self.root = tk.Tk() # membuat jendela utama
        self.root.title('JAM MIFTAHUL KHAIR') # judul jendela
        self.root.resizable(0, 0) # jadikan ukuran jandela tidak berubah ukurannya
        ''' masukan lebel jam disini ,,, mengatur label jam jadi Courier 40  ,,,   menampilkan jam ke jendela '''
        self.label_jam = tk.Label(self.root, text='')
        self.label_jam.configure(font='Courier 40')
        self.label_jam.pack()
        ''' memasang tombol keluar ,,, dan menampilkannya '''
        self.tombol_keluar = tk.Button(self.root, text='Keluar itu di sini', command=lambda: self.root.destroy())
        self.tombol_keluar.pack()
        ''' panggil method jam ,,, dan loop jendela utama '''
        JendelaUtama.jam(self)
        self.root.mainloop()
        ''' memasang tampilan jam '''   
    def jam(self):
        self.waktu = strftime('%H:%M:%S') # mengisi variable jam
        self.label_jam.configure(text=self.waktu) # ubah text jam memjadi yang dinginkan
        self.root.after(1000, lambda: JendelaUtama.jam(self)) # tunggu satu detik kemudian jalankan kembali
        return self.waktu

''' blok program utama ada di bawah yang untuk menjalankan keseluruhan ,,,dan sebagai penjalan utama di file ini '''
if __name__ == '__main__':
    jam = JendelaUtama()
    print ('program keluar')