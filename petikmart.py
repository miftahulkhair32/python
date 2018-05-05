detergen = 15000
minyak_goreng = 25000
laptop = 4500000
disc1 = float(0.1)
disc2 = float(0.25)
detergendisc  = float(detergen*disc1)
minyakdisc = float(minyak_goreng*disc2)
laptopdisc = float(laptop*disc2)
detnet = detergen - detergendisc
minyaknet = minyak_goreng - minyakdisc
laptopnet = laptop - laptopdisc
print ('selamat datang di petik mart')
print ('beli detergen dengan diskon 10% seharga '+str(detnet))
print ('beli minyak goreng dengan diskon 10% seharga '+str(minyaknet))
print ('promo laptop diskon 25% seharga '+str(laptopnet))
