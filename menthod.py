barang = ['sepeda','meja','motor']
# menambah list pada terakhirnya
barang.append('mobil')
print ('menggunakan append\n',barang)
# untuk menambah dimana saja
barang.insert(1,'komputer')
print ('menggunakan insert\n',barang)
#  untuk menghitung jumlah data sama
barang.insert(3,'meja')
print ('jumlah meja ada: ',barang.count('meja'),"\n",barang) 
# menghapus data
barang.remove('meja')
print ('hapus meja menggunakan remove\n',barang)
# membalikan data
barang.reverse()
print ('di balikkan\n',barang)

print (70*'=')

stuff = barang.copy()
stuff.append('laptop')
print (stuff)
print (barang)