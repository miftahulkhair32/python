def Bubblesort(val):
    for passnum in range(len(val)):
        for i in range(passnum):
            if val[i]>val[i+1]:
                temp = val[i]
                val[i] = val[i+1]
                val[i+1] = temp
DaftarAngka = [6,1,2,4,3,5,10,7,9,8]
frt = [1,354,5,7,6,78,89,3,47,656,467,459,45,34,9,32,324]
Bubblesort(DaftarAngka)
Bubblesort(frt)
print(DaftarAngka)
print(frt)