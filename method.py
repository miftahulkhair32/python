biodata1 = {'nama' : 'doni', 'asal' : 'mardid', 'umur' : 2000};
biodata2 = {'nama' : 'gani', 'asal' : 'pluto', 'umur' : '2juta tahun'};

temp = ('nama', 'asal', 'umur');
biodatabaru = {'jeniskelamin' : 'pria'}

biodata1.clear()
print ("jumlah yang di hapus : %d" % len(biodata1))

biodata1 = biodata2.copy()

print ("biodata1 : %s" % str(biodata1))

biodata1.update(biodatabaru)
print ("update biodata1 : %s" % biodata1)
