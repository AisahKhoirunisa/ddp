import math


# Fungsi penjumlahan
def tambah(bil1, bil2):
    hasil = bil1 + bil2
    print("Hasil tambah dari", bil1, "+", bil2, "=", hasil)

# Fungsi pengurangan
def kurang(bil1, bil2):
    hasil = bil1 - bil2
    print("Hasil pengurangan dari", bil1, "-", bil2, "=", hasil)

# Fungsi perkalian
def kali(bil1, bil2):
    hasil = bil1 * bil2
    print("Hasil perkalian dari", bil1, "*", bil2, "=", hasil)

# Fungsi pembagian
def bagi(bil1, bil2):
        hasil = bil1 / bil2
        print("Hasil pembagian dari", bil1, "/", bil2, "=", hasil)

# Fungsi pemangkatan
def pangkat(bil1, bil2):
    hasil = math.pow(bil1, bil2)
    print("Hasil pemangkatan dari", bil1, "^", bil2, "=", hasil)

# Fungsi menghitung luas bangun datar

# Luas segitiga
def luas_segitiga(alas, tinggi):
    hasil = (alas * tinggi) / 2
    print("Luas segitiga dengan alas", alas, "dan tinggi", tinggi, "=", hasil)

# Luas lingkaran
def luas_lingkaran(jari_jari):
    hasil = math.pi * (jari_jari ** 2)
    print("Luas lingkaran dengan jari-jari", jari_jari, "=", hasil)

# Luas persegi
def luas_persegi(sisi):
    hasil = sisi * sisi
    print("Luas persegi dengan sisi", sisi, "=", hasil)

# Luas trapesium
def luas_trapesium(s1, s2, tinggi):
    hasil = 0.5 * (s1 + s2) * tinggi
    print("Luas trapesium dengan sisi 1", s1, ", sisi 2", s2, "dan tinggi", tinggi, "=", hasil)

# Luas jajar genjang
def luas_jajar_genjang(alas, tinggi):
    hasil = alas * tinggi
    print("Luas jajar genjang dengan alas", alas, "dan tinggi", tinggi, "=", hasil)

# Luas layang-layang
def luas_layang_layang(diagonal1, diagonal2):
    hasil = 0.5 * diagonal1 * diagonal2
    print("Luas layang-layang dengan diagonal 1", diagonal1, "dan diagonal 2", diagonal2, "=", hasil)

# Luas persegi panjang
def luas_persegi_panjang(panjang, lebar):
    hasil = panjang * lebar
    print("Luas persegi panjang dengan panjang", panjang, "dan lebar", lebar, "=", hasil)

# Luas belah ketupat
def luas_belah_ketupat(diagonal1, diagonal2):
    hasil = 0.5 * diagonal1 * diagonal2
    print("Luas belah ketupat dengan diagonal 1", diagonal1, "dan diagonal 2", diagonal2, "=", hasil)

# Fungsi menghitung luas permukaan bangun ruang

# Luas permukaan kubus
def luas_kubus(sisi):
    hasil = 6 * (sisi ** 2)
    print("Luas permukaan kubus dengan sisi", sisi, "=", hasil)

# Luas permukaan tabung
def luas_tabung(jari_jari, tinggi):
    hasil = 2 * math.pi * jari_jari * (jari_jari + tinggi)
    print("Luas permukaan tabung dengan jari-jari", jari_jari, "dan tinggi", tinggi, "=", hasil)

# Luas permukaan balok
def luas_balok(panjang, lebar, tinggi):
    hasil = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    print("Luas permukaan balok dengan panjang", panjang, ", lebar", lebar, "dan tinggi", tinggi, "=", hasil)

# Luas permukaan bola
def luas_bola(jari_jari):
    hasil = 4 * math.pi * (jari_jari ** 2)
    print("Luas permukaan bola dengan jari-jari", jari_jari, "=", hasil)

# Luas permukaan limas
def luas_limas(luas_alas, jumlah_sisi_miring):
    hasil = luas_alas + jumlah_sisi_miring
    print("Luas permukaan limas dengan luas alas", luas_alas, "dan jumlah sisi miring", jumlah_sisi_miring, "=", hasil)

# Luas permukaan prisma
def luas_prisma(luas_alas, keliling_alas, tinggi):
    hasil = 2 * luas_alas + keliling_alas * tinggi
    print("Luas permukaan prisma dengan luas alas", luas_alas, ", keliling alas", keliling_alas, "dan tinggi", tinggi, "=", hasil)

# Luas permukaan kerucut
def luas_kerucut(jari_jari, sisi_miring):
    hasil = math.pi * jari_jari * (jari_jari + sisi_miring)
    print("Luas permukaan kerucut dengan jari-jari", jari_jari, "dan sisi miring", sisi_miring, "=", hasil)
