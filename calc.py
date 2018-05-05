def kali(n1,n2):
    return n1 * n2

def bagi(n1,n2):
    return n1 / n2

def tambah(n1,n2):
    return n1 + n2

def kurang(n1,n2):
    return n1 - n2

print ('program kakulator sederhana')
print ('1.perkalian \n 2.pembagian \n 3.penjumlahan \n 4.pengurangan')

pilih = input('masukan nomor operasi yang diinginkan : ')
n1 = input('masukan angka pertama : ')
n2 = input('masukan angka kedua : ')

if pilih == 1:
    hasil = kali(n1,n2)
    print ('hasil perkalian '+str(n1)+' dan '+str(n2)+' adalah '+str(hasil))
elif pilih == 2:
    hasil = bagi(n1,n2)
    print ('hasil pembagian '+str(n1)+' dan '+str(n2)+' adalah '+str(hasil))
elif pilih == 3:
    hasil = tambah(n1,n2)
    print ('hasil pemjumlahan '+str(n1)+' dan '+str(n2)+' adalah '+str(hasil))
elif pilih == 4:
    hasil = kurang(n1,n2)
    print ('hasil pengurangan '+str(n1)+' dan '+str(n2)+' adalah '+str(hasil))
else:
    print ('pilihan anda salah')