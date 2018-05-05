gorengan = ["tempe goreng","tahu goreng","resoles","korket"]

for w in range(len(gorengan)):
    print (w+1, "ini",gorengan[w])
else:
    print ("looping berakhir")

for i in range(10,50,5):
    if i is 20:
        print ("ini angka %s" % i)
        continue
    print ("angka", i)
    if i is 30:
        print ("ini angka %s" % i)
        break
else:
    print ("angka hilang")
angka = 0
u = True
while u:
    print ("angka", angka)
    if angka is 5:
        u = False
        print ("while berhenti")
    angka += 1