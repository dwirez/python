# Buat program Login 
def buatakun():
    nama = input("Masukan Nama : " )
    paswd = input("Masukan Password : ")
    akun_karyawan = {nama:paswd}
    print("Akun Berhasil di buat")
    return akun_karyawan

def Login(owner,karyawan):
    print("Silahkan Login")
    pastikan = False
    while not pastikan :
        input_nama = input("masukan nama = ")
        input_passwd = input("masukan password = ")
        
        if input_nama in owner or karyawan and owner[input_nama] or karyawan[input_nama] == input_passwd:
            print("login Berhasil")
            pastikan = True
        else:
            print("Nama Pengguna atau sandi salah")

def masuk_as_owner():
    print("="*4,"Login Sebagai Owner", "="*4)
    print("pilih yang ingin dilakukan\n1.buat akun karyawan\n2.lihat barang\n3.tambah barang\n4.histori transaksi")
    milih = int(input("Masukan pilihan (1/2/3/4) : "))
    if milih == 1 :
        buatakun

putusan = input("login? (y/n) : ")
if putusan == "y" :
    Login(owner)
