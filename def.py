# Buat program Login 
def buatakun():
    nama = input("Masukan Nama : " )
    paswd = input("Masukan Password : ")
    user = {nama:paswd}
    print("Akun Berhasil di buat")
    return user

def Login(existing_user):
    print("Silahkan Login")
    pastikan = False
    while not pastikan :
        input_nama = input("masukan nama = ")
        input_passwd = input("masukan password = ")
        
        if input_nama in existing_user and existing_user[input_nama] == input_passwd:
            print("login Berhasil")
            pastikan = True
        else:
            print("Nama Pengguna atau sandi salah")


putusan = input("login or sign up : ")
existing_user = {"dwiki" : "456"}

while putusan != "login" and putusan != "sign up":
    putusan = input(f"Salah input\nMasukan lagi Login or sign in : ")

if putusan == "sign up" :
    user_data = buatakun()
    existing_user.update(user_data)
    Login(existing_user)

if putusan == "login":
    Login(existing_user)

