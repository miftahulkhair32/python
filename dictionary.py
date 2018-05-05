mahasantri1 = {
    "NIP":1,
    "Nama":"Fajri",
    "Alamat":"Tinggal di jalan",
    "Jurusan":"PKJ"
}

mahasantri2 = {
    "NIP":2,
    "Nama":"yuda",
    "Alamat":"Di bumi",
    "Jurusan":"Programmer"
}
member = {1:mahasantri1,2:mahasantri2}
print (member[2])

print (70*'+')
print (mahasantri1)
print (mahasantri1.keys())
print (mahasantri1.items())
print (mahasantri1['Nama'])
print (mahasantri1['Jurusan'])
print (70*'+')

for i,c in mahasantri1.items():
    print (i,":",c)

