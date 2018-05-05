# di jalan menggunakan python 3
nilai = 30
print (50*'=')
if nilai is 30:
    print ("nilainya adalah", nilai)
print (50 * '+')
if nilai is not 10:
    print ("nilainya adalah", nilai)
print (50*'=')

def fib(n):
    a, b = 0, 1
    while a < n:
        print (a, end=" ")  # bagian ini harus python 3
        a, b = b, a+b
    print ()

fib(100)
print (50*'=')

gorengan = ["bakwan","resoles","tahu goreng","pisang goreng"]

beli = input("masukan yang akan dibeli : ")

if beli in gorengan:
    print ('ya saya jualan', beli, "monggo di beli")
else:
    print ('saya tidak jualan', beli, 'silahkan pergi dari sini')

if not beli in gorengan:
    print ('\ndan jangan kembali lagi')
print (50*'=')
print ("""
nilainya adalah : %i
""" % nilai)
