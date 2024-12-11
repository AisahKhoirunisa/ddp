from Animal import *
print("======================Ikan Paus======================")
class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, spesies):
        super().__init__(nama,makanan,hidup,berkembang_biak)
        self.warna = warna
        self.spesies = spesies

    def cetak_ikan(self):
        super().cetak()
        print("Warna \t\t\t\t\t: ", self.warna,"\nSpesies \t\t\t\t: ", self.spesies)

Paus = Ikan("Paus", "capelin", "Air", "Vivipar", "Abu-abu", "Famili Columbidae")
Paus.cetak_ikan()

from Animal import *
print("======================Ikan Nemo======================")
class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, spesies):
        super().__init__(nama,makanan,hidup,berkembang_biak)
        self.warna = warna
        self.spesies = spesies

    def cetak_ikan(self):
        super().cetak()
        print("Warna \t\t\t\t\t: ", self.warna,"\nSpesies \t\t\t\t: ", self.spesies)

Nemo = Ikan("Nemo", "Plankton", "Air", "Bertelur", "Garis Merah dan Putih", "Amphiprion")
Nemo.cetak_ikan()