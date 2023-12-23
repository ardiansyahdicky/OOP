class menu():
    def __init__ (jenis, nama, makanan, minuman):
        jenis.nama=nama
        jenis.makanan=makanan
        jenis.minuman=minuman

    def pemesanan(pesan):
        print(f'Permisi, saya {pesan.nama} ingin memesan makanan {pesan.makanan} dan minuman {pesan.minuman}')

pesan1=menu(nama='Ilham',makanan='nasi ayam bakar', minuman='es teh')
pesan2=menu(nama='Kurniawan',makanan='nasi ayam goreng',minuman='es jeruk')
pesan1.pemesanan()
pesan2.pemesanan()