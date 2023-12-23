class buah():
    a='mangga'
    b='nanas'
    c='jambu'

nama=buah()
print("buah 1: ",nama.a)
print('buah 2: ',nama.b)
print('buah 3: ',nama.c)
delattr(buah,'c') #MENGHAPUS ATRIBUT
print('Setelah menghapus atribut')
print("buah 1: ",nama.a)
print('buah 2: ',nama.b)
print('Akan muncul error karena atribut c sudah dihapus')
print('buah 3: ',nama.c)