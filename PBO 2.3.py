class persegi():
    def __init__ (hitung, sisi):
        hitung.sisi=sisi

    def luas(l):
        return l.sisi**2

    def keliling(k):
        return k.sisi*4

angka=persegi(8)
luas=angka.luas()
keliling=angka.keliling()
print ('Sisi persegi 8 cm, luas perseginya ', luas,'cm2', ', kelilingnya ', keliling,'cm')