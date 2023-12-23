class Kalkulator:
    def __init__(self,x,y):
        self.A = x
        self.B = y
        print ("A = "+str(x)+", B = "+str(y))
    def tambah(self):
        self.hasil = self.A + self.B
        print("A + B = " +str(self.hasil))
    def kurang(self):
        self.hasil = self.A - self.B
        print("A - B = " +str(self.hasil))
    def kali(self):
        self.hasil = self.A * self.B
        print("A x B = " +str(self.hasil))
    def bagi(self):
        if self.B==0:
            print ("Pembagian dengan nol")
        else:
            self.hasil = self.A / self.B
            print("A / B = " +str(self.hasil))

Object1 = Kalkulator(7,8)
Object1.tambah()
Object1.kurang()
Object1.kali()
Object1.bagi()
Object2 = Kalkulator(5,0)
Object2.bagi()