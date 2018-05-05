def salam():
    print ("assalamu'alaikum")

def sapa(nama):
    print ('apa kabar '+nama+'?')

def selamat(waktu="pagi",nama='eef'):
    print ('selamat '+waktu+', '+nama)

def kabar(nama):
    print ('hallo '+nama+' bagaimana hari ini?')

nama = raw_input('masukan nama anda : ')
#menjalan fungsi

salam()
sapa(nama)
selamat()
kabar(nama)