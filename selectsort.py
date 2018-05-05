def Selectsort(val):
    for isi in range(len(val)-1,0,-1):
        max=0
        for lokasi in range(1,isi+1):
            if val[lokasi]>val[max]:
                max = lokasi
            temp = val[isi]
            val[isi] = val[max]
            val[max] = temp

DaftarAngka = [6,4,5,2,1,3,9,7,8,10]
frt = [1,354,5,7,6,78,89,3,47,656,467,459,45,34,9,32,324]
Selectsort(DaftarAngka)
Selectsort(frt)
print(DaftarAngka)
print(frt)