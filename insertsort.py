def Insertsort(val):
    for index in range(1,len(val)):
        valuesaktif = val[index]
        posisi = index


        while posisi > 0 and val[posisi - 1] > valuesaktif:
            val[posisi] = val[posisi - 1]
            posisi = posisi - 1
        val[posisi] = valuesaktif

DaftarAngka = [6,4,5,2,1,3,9,7,8,10]
frt = [1,354,5,7,6,78,89,3,47,656,467,459,45,34,9,32,324]
Insertsort(DaftarAngka)
Insertsort(frt)
print(DaftarAngka)
print(frt)