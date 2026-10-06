# Minipro-2-DDP-SistemManajemenReservasidanAntreanPasienKlinikGigi

**NAMA  : SEPTIYA MAHARANI**<br>
**NIM   : 101**




# PENJELASAN PROGRAM

# **1.IMPORT LIBRARY**
> <img width="251" height="71" alt="IMPORT" src="https://github.com/user-attachments/assets/0dc2f9c8-e551-4774-b2fb-307a840678d6" />

Program menggunakan beberapa library Python, yaitu:<br>
- _import os_ digunakan untuk membersihkan tampilan layar setelah proses login.<br>
- _import time_ digunakan untuk memberikan jeda waktu setelah proses tertentu, seperti ketika login berhasil.<br>
- _import pwinput_ digunakan untuk memasukkan password agar password tidak terlihat langsung saat diketik.<br>
- _from prettytable import PrettyTable_ digunakan untuk menampilkan data reservasi pasien dalam bentuk tabel agar lebih rapi.<br>

# **1.DATA AKUN**
> <img width="259" height="154" alt="DATA AKUN" src="https://github.com/user-attachments/assets/41d75bdd-36cc-4c7f-90a7-789018736303" />

Bagian ini merupakan Dictionary yang digunakan untuk menyimpan data akun yang dapat digunakan untuk masuk ke dalam program. Dictionary dipilih karena data dapat disimpan berdasarkan username sebagai key, kemudian setiap username memiliki data berupa password dan hak akses.
Program memiliki dua akun, yaitu Admin dan User. 
- Pada akun Admin terdapat username "admin", password "septi04", dan akses "admin".
- Sedangkan untuk akun User memiliki username "user", password "septi12", dan akses "user".
- Bagian "kata_sandi" digunakan untuk menyimpan password masing-masing akun. Ketika pengguna melakukan login, password yang dimasukkan akan dibandingkan dengan password yang tersimpan di Dictionary ini.
- Bagian "akses" digunakan untuk menentukan hak akses pengguna. Nilai "admin" menunjukkan bahwa akun tersebut memiliki hak sebagai Admin, sedangkan nilai "user" menunjukkan bahwa akun tersebut memiliki hak sebagai User.

Data akses ini kemudian digunakan pada proses login(akses) untuk memastikan pengguna masuk ke menu yang sesuai dengan hak aksesnya. Jika memilih menu Admin, program akan memeriksa apakah akun yang digunakan memang memiliki akses "admin". Begitu juga ketika memilih menu User.Perbedaan hak akses tersebut membuat Admin memiliki akses CRUD lengkap, yaitu dapat menambah, melihat, mengubah, dan menghapus data reservasi pasien. Sementara itu, User hanya memiliki akses untuk melihat data reservasi pasien dan tidak dapat melakukan perubahan terhadap data.Dengan adanya Dictionary akun dan pengecekan hak akses pada proses login, program dapat menerapkan sistem Login dan dua role pengguna dengan hak akses yang berbeda.

# **3.DATA PASIEN**
> <img width="454" height="74" alt="data pasien" src="https://github.com/user-attachments/assets/7c2821b7-b596-495d-96f8-3637e02154b1" />

Bagian ini digunakan untuk menyimpan data reservasi pasien. Data utama disimpan menggunakan Dictionary, dengan nama pasien sebagai _key_, sedangkan informasi lengkap pasien disimpan dalam bentuk Tuple sebagai value.Tuple tersebut berisi beberapa informasi, yaitu nama pasien, nomor HP, keluhan, hari/tanggal reservasi, dan jam reservasi. Penggunaan Dictionary memudahkan program dalam mencari dan mengelola data pasien, sedangkan Tuple digunakan untuk mengelompokkan informasi yang dimiliki oleh satu pasien. Data ini nantinya juga bisa digunakan dalam proses tambah, lihat, ubah, dan hapus data reservasi.

# **3.FUNCTION LOGIN**
<img width="451" height="253" alt="def login akses" src="https://github.com/user-attachments/assets/68c06fc3-b64e-4bc1-8061-0178eab23bdb" />

- def login(akses):<br>
  Digunakan untuk membuat function login() yang bertugas melakukan proses login sekaligus mengecek hak akses pengguna.
def digunakan untuk membuat function, sedangkan login merupakan nama function. Bagian (akses) merupakan parameter yang digunakan untuk menerima jenis hak akses yang ingin digunakan, yaitu "admin" atau "user".<br>
- while True:<br>
  Digunakan untuk membuat proses login terus berjalan selama kondisi bernilai benar. Dengan adanya perulangan ini, jika pengguna memasukkan username atau password yang salah, pengguna dapat mencoba login kembali tanpa program berhenti.<br>
- print("\n----LOGIN----")<br>
  Digunakan untuk menampilkan judul atau penanda bahwa pengguna sedang berada pada bagian login. \n digunakan untuk memberikan satu baris kosong sebelum tulisan agar tampilan lebih rapi.<br>
- nama_pengguna = input("Username: ")<br>
  Digunakan untuk meminta pengguna memasukkan username. Data yang dimasukkan kemudian disimpan ke dalam variabel nama_pengguna.<br>
- kata_sandi = pwinput.pwinput("Password: ")<br>
  Digunakan untuk meminta pengguna memasukkan password. Library pwinput digunakan agar password tidak terlihat secara langsung ketika diketik.Data password yang dimasukkan disimpan ke dalam variabel _kata_sandi_.<br>
- if nama_pengguna in akun:<br>
  Digunakan untuk mengecek apakah username yang dimasukkan terdapat di dalam Dictionary akun.
Jika username ditemukan, program akan melanjutkan ke pengecekan password. Jika tidak ditemukan, proses pengecekan di dalam if tidak dilanjutkan.<br>
- if akun[nama_pengguna]["kata_sandi"] == kata_sandi:<br>
  Digunakan untuk membandingkan password yang dimasukkan pengguna dengan password yang tersimpan di Dictionary akun.
akun[nama_pengguna] digunakan untuk mengambil data akun berdasarkan username yang dimasukkan, sedangkan ["kata_sandi"] digunakan untuk mengambil password dari akun tersebut.<br>
- if akun[nama_pengguna]["akses"] == akses:<br>
  Digunakan untuk mengecek apakah hak akses akun sesuai dengan hak akses yang diminta.
Contohnya, ketika pengguna memilih menu Admin, program akan menjalankan:<br>
-login("admin")<br>
Maka nilai akses adalah "admin". Program akan memastikan akun yang digunakan juga mempunyai:
"akses": "admin" Dengan pengecekan ini, akun User tidak dapat masuk ke menu Admin hanya dengan menggunakan username dan password yang benar.
- print("\nLogin berhasil!")<br>
  Jika username, password, dan hak akses semuanya sesuai, program menampilkan pesan bahwa proses login berhasil.<br>
- time.sleep(3)<br>
  Digunakan untuk memberikan jeda selama 3 detik setelah pesan login berhasil ditampilkan. Fungsi ini berasal dari library time.<br>
- os.system("cls" if os.name == "nt" else "clear")<br>
  Digunakan untuk membersihkan layar setelah proses login berhasil.os.name == "nt" digunakan untuk mengecek sistem operasi. Jika menggunakan Windows, program menjalankan perintah "cls", sedangkan sistem lainnya menggunakan "clear".<br>
- return True<br>
  Digunakan untuk mengembalikan nilai True ketika login berhasil.Nilai ini nantinya digunakan oleh program utama untuk menentukan apakah pengguna boleh masuk ke menu Admin atau User.<br>
- print("\nUsername atau password salah. Silakan coba lagi.")<br>
Bagian ini dijalankan apabila username, password, atau hak akses tidak sesuai.
Karena function masih berada di dalam:<br>
-while True:<br>
pengguna akan kembali diminta memasukkan username dan password sampai berhasil login.




# HASIL OUTPUT


# **1.TAMPILAN AWAL PROGRAM KETIKA AWAL DI JALANKAN**

ADA MENU:
  - ADMIN
  - USER
  - KELUAR
     
> <img width="219" height="187" alt="tampilan awal program" src="https://github.com/user-attachments/assets/91eaba34-538e-477b-9279-c4d8b742aa3f" />

# **2.JIKA MEMILIH ADMIN AKAN MENAMPILKAN USER UNTUK ADMIN**

**- TAMPILAN JIKA LOGIN ADMIN GAGAL**

> <img width="302" height="257" alt="pilih menu admin dan password salah" src="https://github.com/user-attachments/assets/2a1dc161-d446-4c0f-ae35-7c9bd32aa912" />

**- TAMPILAN JIKA LOGIN ADMIN BERHASIL**

> <img width="190" height="227" alt="pilih menu admin dan login berhasil" src="https://github.com/user-attachments/assets/d2e1f2f2-38ab-420e-bbb4-71d9242506e1" />

(Jika berhasil login program akan menunggu 3 detik kemudian layar bersih dan akan menampilkan menu-menu yang ada di user)

**- TAMPILAN MENU-MENU YANG ADA DI DALAM MENU ADMIN**

> <img width="221" height="194" alt="tampilan menu admin,dan ke clear karena pake os" src="https://github.com/user-attachments/assets/0628f643-3a77-4f3a-907c-e033dd78b203" />

**- JIKA MEMILIH MENU 1 (TAMBAH DATA RESERVASI PASIEN) DAN MENAMBAHKAN DATA PASIEN 1**

<img width="257" height="273" alt="pilih menu 1 dan nambah pasien1" src="https://github.com/user-attachments/assets/068df3f1-9fb4-4c57-a4da-77d29e536c31" />

**-MENAMBAHKAN DATA PASIEN KE 2-4**

> <img width="254" height="259" alt="tambah data pasien 2" src="https://github.com/user-attachments/assets/ebccd0b1-d179-4a65-af9f-7c0d42e79d12" />

> <img width="251" height="273" alt="tambah pasien3" src="https://github.com/user-attachments/assets/54d36942-894a-4fe9-b570-17c9a78616bf" />

> <img width="241" height="272" alt="tambah pasien 4" src="https://github.com/user-attachments/assets/c2515ead-b04a-4633-b4fb-d883440c22ab" />

**- JIKA MEMILIH MENU 1 (TAMBAH DATA RESERVASI PASIEN) DAN MENAMBAHKAN DATA PASIEN GAGAL/TIDAK LENGKAP**
> 

**- JIKA MEMILIH MENU 2 (LIHAT DATA RESERVASI PASIEN)DAN HASIL DARI LIHAT DATA PASIEN**

> <img width="526" height="326" alt="hasil lihat pasien" src="https://github.com/user-attachments/assets/71a3b1d4-6c7c-4011-8832-70bd1c19773d" />

**- JIKA MEMILIH MENU 3 (UBAH DATA RESERVASI PASIEN)DAN HASIL DARI PILIHAN UBAH DATA PASIEN**
  ADA 4 MENU DI DALAM UBAH DATA RESERVASI PASIEN:
  - 1.UBAH 









