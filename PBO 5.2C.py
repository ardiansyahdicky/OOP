from abc import ABC, abstractmethod
class Bentuk(ABC):
    @abstractmethod
    def luas(self): 
        return self.sisi * self.sisi

    @abstractmethod
    def keliling(self): 
        return 4 * self.sisi

    @abstractmethod
    def luas(self):
        return self.p*self.l

    @abstractmethod
    def keliling(self):
        return 2*self.p+2*self.l

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi
    def luas(self):
        return self.sisi * self.sisi
    def keliling(self):
        return 4 * self.sisi

class Persegipanjang(Bentuk):
    def __init__(self,p,l):
        self.p=p
        self.l=l
    def luas(self):
        return self.p*self.l
    def keliling(self):
        return 2*self.p+2*self.l

persegi = Persegi(6)
persegipanjang=Persegipanjang(3,5)

print('Luas perseginya adalah ',persegi.luas())
print('Keliling perseginya adalah ',persegi.keliling())
print('Luas persegi panjangnya adalah ',persegipanjang.luas())
print('Keliling persegi panjangnya adalah ',persegipanjang.keliling())