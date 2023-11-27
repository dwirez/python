# 1.Buat kode untuk menghitung volume dan keliling tabung menggunakan fungsi
# 2.Buat Kode untuk melakukan operasi matematika berupa penjumlahan,perkalian, dan pembagian terhadap
#    2 bilangan menggunakan fungsi
# 3.Buat kode mencetak bilangan genap dan ganjil menggunakan fungsi
# 4.sebuah fungsi/method yang menerima sebuah list dengan elemen bertipe double kemudian mengembalikan
#     list baru dengan elemen yang sama namun nilai yang sudah terurut dari besar ke kecil atau 
#     dari kecil ke besar
# 5.Buatlah sebuah program fungsi perulangan dengan menginput nilai sebanyak jumlah yang kita inginkan.
#     Lalu nilai tersebut dibagi dengan jumlah perulangan.(Nilai Harian, Nilai UTS dan Nilai UAS)
# 6.Buatlah sebuah Program Fibbonanci menggunakan rekrusif!
# 7. Buatlah sebuah Program Hitung Nilai MAKSIMAL dan MINIMAL menggunakan rekursif


# FUNGSI VOLUME TABUNG
def volume_tabung(jari,tinggi):
   
    volume = 3.14 *jari**2 *tinggi
    return volume

#FUNGSI KELILING TABUNG 
def keliling_tabung(jari,tinggi):
    keliling = 2*3.14*jari
    return keliling

# FUNGSI OPERASI MATEMATIKA
def Operasi_MTK(numb1,numb2):
    tambah = numb1 + numb2
    kurang = numb1 - numb2
    kali = numb1 * numb2
    bagi = numb1 / numb2
    return tambah,kurang,kali,bagi

# FUNGSI Mengetahui Bilangan Genap atau Ganjil
def ganjilgenap(numb):
    if numb % 2 == 0 :
        numb = "Genap" 
        return numb
    else :
        numb = "Ganjil"
        return numb

# FUNGSI Mengurutkan type data double dari atas ke bawah atau sebaliknya
def urutan_list(inputan_list,descending=True) :
    list_terurut = list(inputan_list)
    list_terurut.sort(reverse=descending)

    return list_terurut

# FUNGSI Rata Rata Nilai Ulangan Harian, UTS dan Nilai UAS
def total_nilai(nilai_harian,nilai_uts,nilai_uas) :
    total_nilai_mahasiswa = int(nilai_harian)+int(nilai_uts)+int(nilai_uas)
    return total_nilai_mahasiswa

def banyak_ujian(jumlah_data):
    banyak_ujian_mahasiswa = 0
    for i in range(1, jumlah_data + 1):
        print("--------Nilai Ke ", i, "--------")
        nilai_harian = int(input("Masukan Nilai Harian : "))
        nilai_uts = int(input("Masukan Nilai UTS : "))
        nilai_uas = int(input("Masukan Nilai UAS : "))

        banyak_ujian_mahasiswa += total_nilai(nilai_harian,nilai_uts,nilai_uas)

    return banyak_ujian_mahasiswa / jumlah_data

# FUNGSI Deret Fibbonanci(Rekursif)
def Fibbonanci(n):
    if n < 1:
        return[n]

    list_sebelum_N = Fibbonanci(n - 1)
    angka1 = list_sebelum_N[-2] if len(list_sebelum_N) > 2 else 0
    angka2 = list_sebelum_N[-1] if len(list_sebelum_N) > 2 else 1

    return list_sebelum_N + [angka1 + angka2]

# FUNGSI Mencari nilai MAX dan MIN dengan metode rekursif
def nilai_maksimal (list):
    nilai_terbesar = list[0]

    if len(list) > 1:
        lanjut_nilai_terbesar = nilai_maksimal(list[1:])

        if lanjut_nilai_terbesar > nilai_terbesar :
            nilai_terbesar = lanjut_nilai_terbesar

    return nilai_terbesar

def nilai_minimal (list):
    nilai_terkecil = list[0]

    if len(list) > 1:
        lanjut_nilai_terkecil = nilai_minimal(list[1:])
        
        if lanjut_nilai_terkecil < nilai_terkecil :
            nilai_terkecil = lanjut_nilai_terkecil
    
    return nilai_terkecil

# MEMANGGIL FUNGSI
print("="*4, "TOOLS MTK", "="*4)
print("1.Hitung VOLUME dan KELILING Tabung\n2.Hitung Operasi MATEMATIKA\n3.Mengetahui bilangan Ganjil atau genap\n4.Mengurutkan list bertipe data double \n5.Hitung rata-rata nilai Mahasiswa\n6.Deret Fibbonanci dengan rekursif\n7.Mencari Nilai Maksimal dan Minimal dengan rekursif")
print()
userchoice = int(input("Masukan sesai Nomor Program : "))
if userchoice == 1 :
    print("="*4,"Program Hitung VOlume dan Keliling Tabung","="*4)
    jari_jari = int(input("Masukan Jari jari Tabung : "))
    tinggi_tabung = int(input("Masukan Tinggi Tabung : "))
    print()
    print(f"Jadi Volume tabung adalah {volume_tabung(jari_jari,tinggi_tabung)}")
    print(f"Jadi keliling tabung adalah {keliling_tabung(jari_jari,tinggi_tabung)}")
elif userchoice == 2 :
    print("="*4,"Program OPERASI MTK TAMBAH KURANG BAGI ","="*4)
    angka1 = int(input("Masukan Angka pertama Yang ingin digunakan : "))
    angka2 = int(input("Masukan Angka kedua Yang ingin digunakan : "))
    
    print("Pilih Operasi ")
    print("1.Operasi Tambah\n2.Operasi kurang\n3.Operasi Kali\n4.Operasi Bagi")
    opchoice = int(input("Masukan Angka Sesuai dengan Nomor Program Operasi"))
    if opchoice == 1 :
        print("="*4,"Operasi Tambah","="*4)
        a,b,c,d = Operasi_MTK(angka1,angka2)
        print(f"Hasil dari Operasi Penambahan dari {angka1} dan {angka2} adalah = {a}")
    elif opchoice == 2 :
        print("="*4,"Operasi kurang","="*4)
        a,b,c,d = Operasi_MTK(angka1,angka2)
        print(f"Hasil dari Operasi pengurangan dari {angka1} dan {angka2} adalah = {b}")
    elif opchoice == 3 :
        print("="*4,"Operasi Kali","="*4)
        a,b,c,d = Operasi_MTK(angka1,angka2)
        print(f"Hasil dari Operasi perkalian dari {angka1} dan {angka2} adalah = {c}")
    elif opchoice == 4 :
        print("="*4,"Operasi Bagi","="*4)
        a,b,c,d = Operasi_MTK(angka1,angka2)
        print(f"Hasil dari Operasi Pemabagian dari {angka1} dan {angka2} adalah = {d}")
    else : 
        print("Kamu Salah Memasukan Angka")
elif userchoice == 3 :
    print("="*4,"Program Mengetahui bilangan GANJIL atau GENAP ","="*4)
    bil = int(input("Masukan Bilangan : "))
    print(f"Bilangan adalah {ganjilgenap(bil)}")
elif userchoice == 4 :
    print("="*4,"Mengurutkan List data double dari terbesar ke terkecil atau sebaliknya ","="*4)

    urutan = []
    n = int(input("Masukan berapa angka yang ingin berada di dalam list"))
    for i in range(n):
        input_urutan = float(input(f"Masukan data double/float ke -{i + 1} : "))
        urutan.append(input_urutan)

    besarkekecil = urutan_list(urutan)
    kecilkebesar = urutan_list(urutan, descending=False)

    print("Urutan dari besar ke kecil:", besarkekecil)
    print("Urutan dari kecil ke besar:", kecilkebesar)

elif userchoice == 5 :
    print("="*4,"Menghitung Rata Rata Nilai Mahasiswa ","="*4)
    jumlah_data = int(input("berapa ujian yang akan di rata rata : "))
    hasil_ujian = banyak_ujian(jumlah_data)
    print("jadi rata - rata nilai yang didapat adalah : ", hasil_ujian)

elif userchoice == 6 :
    print("="*4,"Deret Fibbonanci dengan rekursif ","="*4)
    print()
    panjang = int(input("Masukan Panjang Deret : "))
    print(Fibbonanci(panjang - 1))

elif userchoice == 7 :
    print("="*4,"Mencari Nilai MAX dan MIN dengan metode Rekursif ","="*4)
    pilih = (int(input("1. Mencari Nilai Maximal\n2. Mencari Nilai Minimal\nMasukan Nomor Program : ")))
    if pilih == 1 :
        a = []
        banyakvalue = (int(input("Masukan Berapa jumlah nilai yang ingin kamu masukan ; ")))
        for i in range(0, banyakvalue):
            angka = int(input(f"Masukan angka ke {i+1} :"))
            a.append(angka)
        print("Angka didalam list adalah",a)
        print("angka Maksimalnya adalah =", nilai_maksimal(a))
    elif pilih == 2 :
        a = []
        banyakvalue = (int(input("Masukan Berapa nilai yang ingin kamu masukan ; ")))
        for i in range(0, banyakvalue):
            angka = int(input(f"Masukan angka ke {i+1} : "))
            a.append(angka)
        print("Angka didalam list adalah",a)
        print("angka Minimalnya adalah =", nilai_minimal(a))
    else :
        print("Salah input")




    





    

