class karyawan(object):
    jml_karyawan = 0

    # konsuktor
    def __init__(self,kid,nama,jabatan):
        self.kid = kid
        self.nama = nama
        self.jabatan = jabatan
        karyawan.jml_karyawan += 1

    # menthod
    def infoKaryawan(self):
        print ('karyawan masuk')
        print (20*'=')
        print ("ID : {}".format(self.kid))
        print ("Nama : %s" % self.nama)
        print ("Jabatan : %s" % self.jabatan)


# cara akses class
ojb = karyawan("K001","Pretty","akutansi")
ojb.infoKaryawan()

# tambah karyawan baru
ojb1 = karyawan("B003","Budi","Teknisi")
ojb1.infoKaryawan()


print (20*"-")
print ("total karyawan : %d" % karyawan.jml_karyawan)