print "jumlah siswa masuk\n"
grade = "kelas sampai E"
kelas = "siswa sangat banyak"
siswa = input("masukan jumlah siswa masuk : ")
if siswa <=30:
 grade = "kelas A"
elif siswa <=60:
 grade = "kelas A,B"
elif siswa <=90:
 grade = "kelas A,B,C"
elif siswa <=120:
 grade = "kelas A,B,C,D"

if grade == "kelas A" or grade == "kelas A,B" or grade == "kelas A,B,C":
 kelas = "siswa sedikit"
print"""
grade : %s
kelas : %s
"""%(grade, kelas)

