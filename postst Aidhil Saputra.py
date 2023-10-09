# daftar menu seafood dan harganya
menu_seafood = {
    "1": {"nama": "Lobster", "harga": 250000},
    "2": {"nama": "Udang", "harga": 10000},
    "3": {"nama": "Ikan Salmon", "harga": 165000}
}

# Fungsi untuk menampilkan menu seafood
def tampilkan_menu_seafood():
    print("Daftar Seafood:")
    for kode, data in menu_seafood.items():
        print(f"{kode}. {data['nama']} - Rp {data['harga']}")

# Fungsi untuk menghitung total harga pembelian seafood
def hitung_total_seafood(pembelian_seafood):
    total = 0
    for item in pembelian_seafood:
        total += menu_seafood[item]["harga"]
    return total

# Fungsi untuk admin mengubah menu seafood
def admin_ubah_menu_seafood():
    print("Mode Admin - Mengubah Menu Seafood")
    tampilkan_menu_seafood()
    
    while True:
        print("Pilih tindakan:")
        print("1. Tambah produk baru di menu")
        print("2. Ubah harga makanan di menu")
        print("3. Kembali ")
        
        tindakan_admin = input("Masukkan tindakan: ")
        
        if tindakan_admin == "1":
            kode_produk_baru = str(len(menu_seafood) + 1)
            nama_menu_baru = input("Masukkan nama menu baru: ")
            harga_makanan_baru = int(input("Masukkan harga makanan baru: "))
            menu_seafood[kode_produk_baru] = {"nama": nama_menu_baru, "harga": harga_makanan_baru}
            print(f"Produk seafood {nama_menu_baru} telah ditambahkan ke menu.")
        elif tindakan_admin == "2":
            tampilkan_menu_seafood()
            kode_produk_ubah = input("Masukkan kode produk yang ingin diubah harganya: ")
            if kode_produk_ubah in menu_seafood:
                harga_baru = int(input(f"Masukkan harga baru untuk {menu_seafood[kode_produk_ubah]['nama']}: "))
                menu_seafood[kode_produk_ubah]["harga"] = harga_baru
                print(f"Harga {menu_seafood[kode_produk_ubah]['nama']} telah diubah menjadi Rp {harga_baru}.")
            else:
                print("Kode produk tidak valid.")
        elif tindakan_admin == "3":
            break
        else:
            print("Tindakan tidak valid. Silakan pilih tindakan yang benar.")

# Program utama
print("Selamat datang, silahkan registrasi terlebih dulu")
nama = input("Masukkan Nama Anda : ")
umur = input("Masukkan Umur Anda : ")
KataSandi = input("Buat Kata Sandi anda : ")
konfirKataSandi = input("Konfirmasikan Kata Sandi Anda : ")
if konfirKataSandi == KataSandi :
    print("Akun anda telah berhasil dibuat, Silahkan melakukan Login kembali : ")
    print("-"*100)
    nama = input("masukan nama :")
umur = input("masukan umur :")
password = input ("masukan password :")

while True:
    if  nama == (nama):
        if umur == (umur): 
            if password == (KataSandi):
                print ("password yang anda masukan benar !!")
                break
            else :
                print ("password yang anda masukan salah !!")
                break
        else :
            print ("password yang anda masukan salah !!")
            break
    else:
        print("password anda salah, silahkan regis lagi")
        

while True:
    print("Selamat datang di Toko Aidhil!")
    print("Pilih mode:")
    print("1. Admin")
    print("2. Pembeli")
    print("3. Keluar")

    mode = input("Masukkan pilihan: ")

    if mode == "1":
        admin_ubah_menu_seafood()
    elif mode == "2":
        tampilkan_menu_seafood()
        konsumen_pembelian_seafood = []
        while True:
            pilihan = input("Masukkan kode seafood (selesai untuk mengakhiri belanja): ")
            if pilihan.lower() == "selesai":
                break
            elif pilihan in menu_seafood:
                konsumen_pembelian_seafood.append(pilihan)
            else:
                print("Seafood tidak valid. Silakan pilih seafood yang benar.")

        total_harga_seafood = hitung_total_seafood(konsumen_pembelian_seafood)
        print(f"Total harga pembelian seafood: Rp {total_harga_seafood}")
    elif mode == "3":
        print("Terima kasih telah berbelanja ditoko kami")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")