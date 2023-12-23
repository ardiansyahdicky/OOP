class India():
    def capital(self):
        print("ibukota delhi")
    def language(self):
        print("bahasa hindi")

class Indonesia():
    def capital(self):
        print("Ibukota Jakarta")
    def language(self):
        print("bahasa indonesia")

obj_india=India()
obj_indo=Indonesia()
obj_india.capital()
obj_india.language()

for negara in (obj_india, obj_indo):
    negara.capital()
    negara.language()

class negara:
    def jumlah_negara(self):
        print("jumlah negara ada banyak")
    def capital(self):
        print("setiap negara punya ibukota")
    def language(self):
        print("setiap negara beda ibukota")

class India(negara):
    def capital(self):
        print("Ibu kota india")
    def language(self):
        print("bahasa hindi")
class Indonesia(negara):
    def capital(self):
        print("Ibu kota Jakarta")
    def language(self):
        print("bahasa indonesia")