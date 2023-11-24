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
    keliling = 2*3.14*jari*tinggi
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

# FUNGSI 

# MEMANGGIL FUNGSI
print("="*4, "TOOLS MTK", "="*4)
print("1.Hitung VOLUME dan KELILING Tabung\n2.Hitung Operasi MATEMATIKA\n3.Mengetahui bilangan Ganjil atau genap\n4.Mengurutkan list bertipe data double ")
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
    elif opchoice == 3 :
        print("="*4,"Operasi Bagi","="*4)
        a,b,c,d = Operasi_MTK(angka1,angka2)
        print(f"Hasil dari Operasi Pemabagian dari {angka1} dan {angka2} adalah = {d}")
    else : 
        print("Kamu Salah Memasukan Angka")
        opchoice = int(input("Masukan Lagi : "))
elif userchoice == 3 :
    print("="*4,"Program Mengetahui bilangan GANJIL atau GENAP ","="*4)
    bil = int(input("Masukan Bilangan : "))
    print(f"Bilangan adalah {ganjilgenap(bil)}")
elif userchoice == 4 :
    urutan = []
    n = int(input("Masukan berapa angka yang ingin berada di dalam list"))
    for i in range(n):
        input_urutan = float(input(f"Masukan data double/float ke -{i + 1} : "))
        urutan.append(input_urutan)

    besarkekecil = urutan_list(urutan)
    kecilkebesar = urutan_list(urutan, descending=False)

    print("Urutan dari besar ke kecil:", besarkekecil)
    print("Urutan dari kecil ke besar:", kecilkebesar)



    

