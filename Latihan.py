print("=====Class Person=====")
class Person:
    def __init__(self,nama,umur,jekel):
        self.nama = nama
        self.umur = umur
        self.jekel = jekel

    def jalan (self):
        print(f"{self.nama} bisa berjalan")

    def ngomong (self):
        print(f"Dia berbicara karena dia {self.jekel}")

bayu = Person("bayu", 20, "Laki-laki")
bayu.jalan()
bayu.ngomong()

print("=====Class Supir=====")
from Person import*
Class Supir(Person):
    pass

andi = Supir("Andi", 30, "Laki-laki")
andi.jalan()

print("=====Class Supir=====")
Class Supir(Person):
    def __init__(self, nama, umur, jekel, sim):
        super().__init__(nama,umur,jekel)
        self.sim = sim

    def nyupir(self):
        print(f'{self.nama}bisa nyupir karena memiliki sim {self.sim}')

Andi.nyupir()

print("=====class mahasiswa=====")
class Mahasiwa(Person):
    def __init__(self, nama, umur, jekel, nim)
        super().__init__(nama, umur, jekel, nim)
        self.nim = nim
    def belajar(self):
        print(f'{self.nama} sedang belajar dengan nim {self.nim}')

bunga = Mahasiswa ("bunga", 18, "Perempuan",11121314)
bunga.belajar()

print("=====Object Inheritance=====")
from Mahasiswa import *
from Dosen import *#ciptakan object
m1 = Mahasiswa('Siti Aminah','Wanita',20,'SI',3)
m2 = Mahasiswa('Budi Santoso','Pria',23,'TI',5)
d1 = Dosen('Sirojul Munir','Pria',43,'S.Si, M.Kom', 'LPPM')
d2 = Dosen('Henry Saptono','Pria',44,'S.Si, M.Kom', 'LTSI')#gunakan fungsi2 yg ada di class 
d1.setGaji(12000000)
d2.setGaji(10000000)
m1.cetak()
m2.cetak()
d1.cetak()
d2.cetak()