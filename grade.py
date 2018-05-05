print ("program nilai petik\n")
grade = "E"
kelulusan = "tidak lulus"
nilai = int(input("input nilai petik : "))
if nilai >= 85:
 grade = "A"
elif nilai >= 75:
 grade = "B"
elif nilai >= 60:
 grade = "C"
elif nilai >= 50:
 grade = "D"

if grade == "A" or grade == "B" or grade == "C":
 kelulusan = "hore lulus"
print ("""
grade : %s
kelulusan : %s
""" % (grade, kelulusan))
