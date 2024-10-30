#soal nomor 1
# list utama : kendaraan
kendaraan = ["mio", "motor","200cc","hitam", "roda 2" ]

#mencetak isi list kendaraan
print(kendaraan)

#menambahkan value atau nilai di ujung list (pakai append())

#proses append 1 (harga kendaraan)
kendaraan.append("20.000.000")

#proses append 2 (tipe kendaraan)
kendaraan.append("matic")

#cetak nilai kendaraan setelah perubahan
print(kendaraan)

#sisispan nilai untuk tipe kendaraan
kendaraan.insert (2,"yamaha")

#cetak hasil list akhirnya
print(kendaraan)

#soal nomor 3
pilihan = int(input("""Masukkan Pilihan Nomor:
1. Menghitung Luas Persegi
2. Menghitung Luas Lingkaran
3. Menghitung Luas Segitiga
"""))

match pilihan:
    case 1:
        print("Menghitung Luas Persegi")
        s = int(input("Masukan nilai sisi: "))
        luasPersegi = s * s
        print(f"Luas persegi dengan sisi {s} adalah {luasPersegi}")
    case 2:
        print("Menghitung Luas Lingkaran")
        pi = 3.14
        r = int(input("Masukkan nilai jari-jari"))
        luasLingkaran = pi * r**2
        print(f"Luas Lingkaran dengan jari-jari {r} adalah {luasLingkaran}")
    case 3:
        print("Menghitung Luas segitiga")
        alas = int(input("Masukkan nilai alas: "))
        tinggi = int(input("Masukkan nilai tinggi: "))
        luasSegitiga = 1/2 * alas * tinggi
        print(f"Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luasSegitiga}")
    case _:
        print("Input tidak valid")