hewan = ['ayam','cacing','kampret','kucing','kangguru','ikan']

barang = ['bangkai','pintu','manusia','komputer','nikah','mati']

for i,binatang in enumerate(hewan):
    print (i+1,':',binatang)

print (70*'=')

for binatang,dagangan in zip(hewan,barang):
    print (binatang,' sama dengan ',dagangan)

santri = {'miftahul','jafar','yuda','sandi','dian'}

for maha in sorted(santri):
    print (maha)

print (70*'-')

for i in reversed(range(1,10,2)):
    print (i)