x = float(input("masukan suhu celcius : "))
y = input("masukan tujuan konversi : ")
# di ubah dari raw_input ke input karena sekarang banyak menggunakan python v3.5

if(y=='f'):
	z = (x * 9/5) + 32
elif(y=='k'):
	z = 273 + x
elif(y=='r'):
	z = (x * 4/5)
else:
	print ("inputan yang anda masukan salah")

print("konversi suhu dari "+str(x)+"celcius ke "+y+" = "+str(z))
