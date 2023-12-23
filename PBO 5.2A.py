class Indonesia():
    def ibukota(self):
        print('Ibukota Negara Indonesia adalah Jakarta')
    def matauang(self):
        print('Mata uangnya Rupiah')
    def bahasa(self):
        print('Bahasanya adalah Bahasa Indonesia')

class Malaysia():
    def ibukota(self):
        print('Ibukota Negara malaysia adalah Kuala Lumpur')
    def matauang(self):
        print('mata uangnya Ringgit')
    def bahasa(self):
        print('Bahasanya adalah Bahasa Melayu')

indo=Indonesia()
malay=Malaysia()
for negara in (indo, malay):
    negara.ibukota()
    negara.matauang()
    negara.bahasa()