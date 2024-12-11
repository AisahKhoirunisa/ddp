from Animal import *
print("======================Ular Anaconda======================")
class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, corak, racun):
        super().__init__(nama,makanan,hidup,berkembang_biak)
        self.corak = corak
        self.racun = racun

    def cetak_ular(self):
        super().cetak()
        print("Corak \t\t\t\t\t: ", self.corak,"\nRacun \t\t\t\t\t: ", self.racun)

anaconda = Ular("Anaconda", "Daging", "Air", "Bertelur", "Bergaris", "Tidak Berbisa")
anaconda.cetak_ular()

from Animal import *
print("======================Ular Kobra======================")
class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, corak, racun):
        super().__init__(nama,makanan,hidup,berkembang_biak)
        self.corak = corak
        self.racun = racun

    def cetak_ular(self):
        super().cetak()
        print("Corak\t\t\t\t\t: ", self.corak,"\nRacun \t\t\t\t\t: ", self.racun)

Kobra = Ular("Kobra", "Daging", "Darat", "Bertelur", "Zigzag", "Berbisa")
Kobra.cetak_ular()