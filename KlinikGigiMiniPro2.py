import os
import time
import pwinput
from prettytable import PrettyTable

akun = {
    "admin": {
        "kata_sandi": "septi04",
        "akses": "admin"
    },
    "user": {
        "kata_sandi": "septi12",
        "akses": "user"
    }
}

data_pasien = {
    "Andi": ("Andi", "08123456789", "Sakit gigi", "06-10-2026", "10:00")
}


def login(akses):
    while True:
        print("\n----LOGIN----")
        nama_pengguna = input("Username: ")
        kata_sandi = pwinput.pwinput("Password: ")

        if nama_pengguna in akun:
            if akun[nama_pengguna]["kata_sandi"] == kata_sandi:
                if akun[nama_pengguna]["akses"] == akses:
                    print("\nLogin berhasil!")
                    time.sleep(3)
                    os.system("cls" if os.name == "nt" else "clear")
                    return True

        print("\nUsername atau password salah. Silakan coba lagi.")


def tambah_data():
    print("\n----Tambah Data Reservasi Pasien----")
    nama = input("Nama Pasien: ")
    No_HP = input("Nomor HP Pasien: ")
    keluhan = input("Keluhan Pasien: ")
    hari_tanggal = input("Hari/Tanggal: ")
    jam = input("Jam: ")

    if nama and No_HP and keluhan and hari_tanggal and jam:
        data_pasien[nama] = (nama, No_HP, keluhan, hari_tanggal, jam)
        print("\nPasien", nama, "berhasil didaftarkan!")
    else:
        print("\nData tidak Tersimpan! Semua kolom input harus diisi.")


def lihat_data():
    print("\n----Lihat Data Reservasi Pasien----")

    data_pasien_sorted = sorted(data_pasien.values(), key=lambda x: (x[3], x[4]))

    if data_pasien_sorted:
        print("\nDaftar Reservasi Pasien:")

        tabel = PrettyTable()
        tabel.field_names = ["No.Antrean", "Nama Pasien", "Nomor HP", "Keluhan", "Hari/Tanggal", "Jam"]

        for i, pasien in enumerate(data_pasien_sorted, start=1):
            tabel.add_row([
                i,
                pasien[0],
                pasien[1],
                pasien[2],
                pasien[3],
                pasien[4]
            ])

        print(tabel)

    else:
        print("\nTidak ada data reservasi pasien.")

def ubah_data():
    print("\n----Ubah Jadwal Reservasi Pasien----")
    print("1. Nomor Antrean")
    print("2. Nama Pasien")
    print("3. Nomor HP")
    print("4. Kembali")
    cari = input("Masukkan pilihan (1-4): ")

    if cari == "1":
        try:
            nomor = int(input("Nomor Antrean yang ingin diubah: "))

            data_pasien_sorted = sorted(data_pasien.values(), key=lambda x: (x[3], x[4]))

            if nomor >= 1 and nomor <= len(data_pasien_sorted):
                pasien = data_pasien_sorted[nomor - 1]
                nama = pasien[0]

                print("Data Pasien Ditemukan!")
                hari_tanggal = input("Hari/Tanggal Baru: ")
                jam = input("Jam Baru: ")

                if hari_tanggal and jam:
                    data_pasien[nama] = (pasien[0], pasien[1], pasien[2], hari_tanggal, jam)
                    print("\nJadwal pasien", nama, "berhasil diubah!")
                else:
                    print("\nData tidak Tersimpan! Kolom input jadwal harus diisi.")
            else:
                print("\nData pasien tidak ditemukan.")

        except ValueError:
            print("\nData pasien tidak ditemukan.")

    elif cari == "2":
        nama = input("Nama Pasien yang ingin diubah: ")

        if nama in data_pasien:
            pasien = data_pasien[nama]

            print("Data Pasien Ditemukan!")
            hari_tanggal = input("Hari/Tanggal Baru: ")
            jam = input("Jam Baru: ")

            if hari_tanggal and jam:
                data_pasien[nama] = (pasien[0], pasien[1], pasien[2], hari_tanggal, jam)
                print("\nJadwal pasien", nama, "berhasil diubah!")
            else:
                print("\nData tidak Tersimpan! Kolom input jadwal harus diisi.")
        else:
            print("\nData pasien", nama, "tidak ditemukan.")

    elif cari == "3":
        No_HP = input("Nomor HP Pasien yang ingin dicari: ")

        ditemukan = False

        for nama, pasien in data_pasien.items():
            if pasien[1] == No_HP:
                print("Data Pasien Ditemukan!")
                hari_tanggal = input("Hari/Tanggal Baru: ")
                jam = input("Jam Baru: ")

                if hari_tanggal and jam:
                    data_pasien[nama] = (pasien[0], No_HP, pasien[2], hari_tanggal, jam)
                    print("\nJadwal pasien", pasien[0], "berhasil diubah!")
                else:
                    print("\nData tidak Tersimpan! Kolom input jadwal harus diisi.")

                ditemukan = True
                break

        if ditemukan == False:
            print("\nData pasien tidak ditemukan.")

    elif cari == "4":
        print("\nKembali ke menu utama.")

    else:
        print("\nPilihan tidak valid. Silakan pilih antara 1-4.")


def hapus_data():
    print("\n----Hapus Data Reservasi Pasien----")
    print("1. Nomor Antrean")
    print("2. Nama Pasien")
    print("3. Nomor HP")
    print("4. Kembali")
    cari = input("Masukkan pilihan (1-4): ")

    if cari == "1":
        try:
            nomor = int(input("Nomor Antrean yang ingin dihapus: "))

            data_pasien_sorted = sorted(data_pasien.values(), key=lambda x: (x[3], x[4]))

            if nomor >= 1 and nomor <= len(data_pasien_sorted):
                pasien = data_pasien_sorted[nomor - 1]
                nama = pasien[0]

                del data_pasien[nama]

                print("\nData pasien", nama, "berhasil dihapus!")
            else:
                print("\nData pasien tidak ditemukan.")

        except ValueError:
            print("\nData pasien tidak ditemukan.")

    elif cari == "2":
        nama = input("Nama Pasien yang ingin dihapus: ")

        if nama in data_pasien:
            del data_pasien[nama]
            print("\nData pasien", nama, "berhasil dihapus!")
        else:
            print("\nData pasien", nama, "tidak ditemukan.")

    elif cari == "3":
        No_HP = input("Pasien yang ingin dihapus menggunakan Nomor HP: ")

        ditemukan = False

        for nama, pasien in list(data_pasien.items()):
            if pasien[1] == No_HP:
                del data_pasien[nama]
                print("\nData pasien", nama, "berhasil dihapus!")
                ditemukan = True
                break

        if ditemukan == False:
            print("\nData pasien tidak ditemukan.")

    elif cari == "4":
        print("\nKembali ke menu utama.")

    else:
        print("\nPilihan tidak valid. Silakan pilih antara 1-4.")

def menu_admin():
    while True:
        print("\n" + "✦== JADWAL PASIEN KLINIK ==✦")
        print("✦==    DRG.SEPTIYA      ==✦")

        print("\n-----MENU-----")
        print("1. Tambah Data Reservasi Pasien")
        print("2. Lihat Data Reservasi Pasien")
        print("3. Ubah Jadwal Reservasi Pasien")
        print("4. Hapus Data Reservasi Pasien")
        print("5. Keluar")
        pilihan = input("Masukkan pilihan (1-5): ")

        if pilihan == "1":
            tambah_data()

        elif pilihan == "2":
            lihat_data()

        elif pilihan == "3":
            ubah_data()

        elif pilihan == "4":
            hapus_data()

        elif pilihan == "5":
            print("\nKembali ke menu utama.")
            break

        else:
            print("\nPilihan tidak valid. Silakan pilih antara 1-5.")

def menu_user():
    while True:
        print("\n" + "✦== JADWAL PASIEN KLINIK ==✦")
        print("✦==    DRG.SEPTIYA      ==✦")

        print("\n-----MENU-----")
        print("1. Lihat Data Reservasi Pasien")
        print("2. Keluar")
        pilihan = input("Masukkan pilihan (1-2): ")

        if pilihan == "1":
            lihat_data()

        elif pilihan == "2":
            print("\nKembali ke menu utama.")
            break

        else:
            print("\nPilihan tidak valid. Silakan pilih antara 1-2.")

while True:
    print("\n" + "✦== JADWAL PASIEN KLINIK ==✦")
    print("✦==    DRG.SEPTIYA      ==✦")

    print("\n-----MENU-----")
    print("1. Admin")
    print("2. User")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan (1-3): ")

    if pilihan == "1":
        if login("admin"):
            menu_admin()

    elif pilihan == "2":
        if login("user"):
            menu_user()

    elif pilihan == "3":
        print("\n----Keluar----")
        print("\nTerima kasih telah menggunakan layanan reservasi pasien klinik gigi.")
        break

    else:
        print("\nPilihan tidak valid. Silakan pilih antara 1-3.")