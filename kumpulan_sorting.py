def ss():
    n=int(input('masukan banyaknya bilangan: '))
    bilangan=[]
    for i in range(n):
        print 'bilangan ke-',i+1,
        bil=int(raw_input(': '))
        bilangan.append(bil)
        print "daftar bilangan sebelum diurutkan: ",bilangan

    i=0
    while i<n-1:
        kecil=i
        j=i+1
    while j<=n-1:
        if bilangan[j]<bilangan[kecil]:
            kecil=j
            j=i+1
    if kecil!=i:
        temp<bilangan[i]
        bilangan[i]=bilangan[kecil]
        bilangan[kecil]=temp
        print 'proses mengurutkan ',i+1,': ',bilangan
    i=i+1
    print 'daftar bilangan setelah diurutkan : ',bilangan
def es():
    n=int(raw_input('masukan banyaknya bilangan :'))
    bilangan=[]
    for i in range(n):
        print 'bilangan ke-',i+1,
        bil=int(raw_input(': '))
        bilangan.append(bil)
    print 'daftar bilangan sebelum di urutkan:',bilangan    
    i=0
    while i<n:
        j=i+i
    while j<n:
        if bilangan[i]>bilangan[j]:
            temp=bilangan[i]
            bilangan[i]=bilangan[j]
            bilangan[j]=temp
            print 'proses mengurutkan ',i+1,': ',bilangan
        elif bilangan[j]==bilangan[i]:
            print 'bilangan yang ingin di tukar bernilai sama'
        else:
            bilangan[i]
        j=j+1
    i=i+1
    print 'daftar bilangan setelah di urutkan :',bilangan

def ins():
    n=int(raw_input('masukan banyaknya bilangan:'))
    bilangan=[]
    for i in range(n):
        print'bilangan ke-',i+1,
        bil=int(raw_input(': '))
        bilangan.append(bil)
        print 'daftar bilangan sebelum diurutkan : ',bilangan
    i=1
    while i<n:
        kcl=i
        j=i-1
        while j>=0:
            if bilangan[kcl]<bilangan[j]:
                temp=bilangan[j]
                bilangan[j]=bilangan[kcl]
                bilangan[kcl]=temp
                tukar=i+1
                print 'proses mengurutkan ',i+1,': ',bilangan
                kcl=j
            j=j-1
            i=i+1
            print 'daftar bilangan setelah diurutkan: ',bilangan

def coba():
    option1 = raw_input('mau coba lagi[Y/T]?').upper()
    if option1 not in ('Y','T'):
        coba()
    if (option1== 'Y'):
        menu()
    if (option1== 'T'):
        exit

def menu():
    print'''
    ======Menu program sorting========
    ||  1.selection sort            ||
    ||  2.bubble sort               ||
    ||  3.insert sort               ||
    ||  4.exit                      ||
    =======dipilih salah satu=========
    '''
    option2 = raw_input('masukan pilihan (1/2/3/4): ')
    if (option2 == '1'):
        ss()
        coba()
    elif (option2 == '2'):
        es()
        coba()
    elif (option2 == '3'):
        ins()
        coba()
    elif (option2 == '4'):
        exit
    else:
        menu()

menu()
