def kali(n1,n2):
    return n1 * n2

def bagi(n1,n2):
    return n1 / n2

def tambah(n1,n2):
    return n1 + n2

def kurang(n1,n2):
    return n1 - n2

def kalkulasi(pilihan,n1,n2):
    if pilihan is 'kali' :
        return kali(n1,n2)
    elif pilihan is 'bagi':
        return bagi(n1,n2)
    elif pilihan is 'tambah':
        return tambah(n1,n2)
    elif pilihan is 'kurang':
        return kurang(n1,n2)
    else:
        return "pilihan anda salah !!"

def introprog():
    print('1.perkalian \n 2.pembagian \n 3.penjumlahan \n 4.pengurangan \n 5.keluar program')

print ('program kakulator sederhana')
introprog()
pilih = input('masukan nomor operasi yang diingginkan : ')
while True:
    if pilih == 1:
        txtpilih = 'kali'
    elif pilih == 2:
        txtpilih = 'bagi'
    elif pilih == 3:
        txtpilih = 'tambah'
    elif pilih == 4:
        txtpilih = 'kurang'
    elif pilih == 5:
            break
    n1 = input('masukan angka pertama : ')
    n2 = input('masukan angka kedua : ')
    hasil = kalkulasi(txtpilih,n1,n2)
    print ('hasil operasi dari '+txtpilih+' = '+str(hasil))
    introprog()
    pilih = input('masukan nomor operasi yang diinginkan : ')