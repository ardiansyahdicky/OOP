a=int(input('Masukkan angka 3: '))
b=int(input('Masukkan angka 7: '))
pilihan=int(input('Pilih 1 untuk selisih, 2 untuk jumlah, 0 untuk stop : '))
while pilihan >0:
    if pilihan==1:
        print('Selisihnya',abs(a-b))
    elif pilihan==2:
        print('Jumlahnya',a+b)
    else:
        print('Salah angka!')
    pilihan=int(input('Pilih 1 untuk selisih, 2 untuk jumlah, 0 untuk stop : '))
print('Terima kasih')