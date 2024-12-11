from Animal import *
print("======================Burung Merpati======================")
class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, spesies):
        super().__init__(nama,makanan,hidup,berkembang_biak)
        self.warna = warna
        self.spesies = spesies

    def cetak_burung(self):
        super().cetak()
        print("Warna \t\t\t\t\t: ", self.warna,"\nSpesies \t\t\t\t: ", self.spesies)

Merpati = Burung("Merpati", "Biji-bijian", "Udara", "Bertelur", "Abu-abu", "Famili Columbidae")
Merpati.cetak_burung()

from Animal import *
print("======================Burung Gereja======================")
class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, spesies):
        super().__init__(nama,makanan,hidup,berkembang_biak)
        self.warna = warna
        self.spesies = spesies

    def cetak_burung(self):
        super().cetak()
        print("Warna \t\t\t\t\t: ", self.warna,"\nSpesies \t\t\t\t: ", self.spesies)

Gereja = Burung("Gereja", "Biji-bijian", "Udara", "Bertelur", "Cokelat", "Passer montanus")
Gereja.cetak_burung()