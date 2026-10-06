# Minipro-2-DDP-SistemManajemenReservasidanAntreanPasienKlinikGigi

**NAMA  : SEPTIYA MAHARANI**<br>
**NIM   : 101**


# Deskripsi Singkat Program

Program ini merupakan program reservasi pasien pada klinik gigi dengan nama DRG.SEPTIYA. Program dibuat untuk membantu mengelola data reservasi pasien yang terdiri dari nama pasien, nomor HP, keluhan, hari/tanggal reservasi, dan jam reservasi.

Program memiliki dua jenis pengguna, yaitu admin dan user. Sebelum masuk ke dalam program, pengguna harus melakukan login menggunakan username dan password sesuai dengan aksesnya. Admin memiliki akses penuh untuk menambah, melihat, mengubah, dan menghapus data reservasi pasien. Sedangkan user hanya memiliki akses untuk melihat data reservasi pasien.

Pada bagian ubah dan hapus data, admin dapat mencari data pasien menggunakan nomor antrean, nama pasien, atau nomor HP. Data reservasi ditampilkan berdasarkan urutan hari/tanggal dan jam. Program juga menggunakan validasi input agar pilihan yang dimasukkan sesuai dengan menu yang tersedia serta menggunakan error handling agar kesalahan input tertentu tidak langsung menghentikan program.

Program ini menggunakan Dictionary untuk menyimpan data akun dan data pasien, Function untuk membagi program menjadi beberapa bagian, serta beberapa library Python yaitu os, time, pwinput, dan PrettyTable.

# GAMBAR FLOWCHART SERTA PENJELASAN ALURNYA

# PENJELASAN KODE PROGRAM

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

# **4.FUNCTION LOGIN**
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

# **5.FUNCTION tambah_data()**

- def tambah_data():
  Digunakan untuk membuat function tambah_data() yang berfungsi untuk menambahkan data reservasi pasien baru ke dalam Dictionary data_pasien.<br>
- print("\n----Tambah Data Reservasi Pasien----")<br>
  Digunakan untuk menampilkan judul bagian tambah data reservasi pasien. \n digunakan untuk memberikan jarak satu baris agar tampilan lebih rapi.<br>
- nama = input("Nama Pasien: ")<br>
  Digunakan untuk meminta pengguna memasukkan nama pasien. Data tersebut disimpan ke dalam variabel nama.
- No_HP = input("Nomor HP Pasien: ")<br>
  Digunakan untuk meminta pengguna memasukkan nomor HP pasien. Data disimpan ke dalam variabel No_HP.
- keluhan = input("Keluhan Pasien: ")
  Digunakan untuk meminta pengguna memasukkan keluhan pasien. Data disimpan ke dalam variabel keluhan.
- hari_tanggal = input("Hari/Tanggal: ")<br>
  Digunakan untuk memasukkan hari atau tanggal reservasi pasien dan menyimpannya ke dalam variabel hari_tanggal.
- jam = input("Jam: ")<br>
  Digunakan untuk memasukkan jam reservasi pasien dan menyimpannya ke dalam variabel jam.
- if nama and No_HP and keluhan and hari_tanggal and jam:<br>
  Digunakan untuk mengecek apakah semua kolom input sudah diisi.<br>
Jika nama, nomor HP, keluhan, hari/tanggal, dan jam semuanya memiliki isi, program akan melanjutkan untuk menyimpan data.
- data_pasien[nama] = (nama, No_HP, keluhan, hari_tanggal, jam)<br>
  Digunakan untuk menyimpan data pasien ke dalam Dictionary data_pasien.
nama digunakan sebagai key, sedangkan data nama, nomor HP, keluhan, hari/tanggal, dan jam disimpan sebagai tuple.
Jadi bentuk datanya menjadi seperti:<br>
-"Nama Pasien": ("Nama Pasien", "Nomor HP", "Keluhan", "Hari/Tanggal", "Jam")<br>
- print("\nPasien", nama, "berhasil didaftarkan!")<br>
  Digunakan untuk menampilkan pesan bahwa data pasien berhasil ditambahkan. Nama pasien yang dimasukkan juga ditampilkan dalam pesan.
- else:<br>
  Digunakan ketika kondisi pada if tidak terpenuhi, yaitu ketika ada salah satu atau beberapa kolom yang belum diisi.
- print("\nData tidak Tersimpan! Semua kolom input harus diisi.")<br>
  Digunakan untuk memberi tahu pengguna bahwa data tidak disimpan karena masih ada kolom yang kosong.

# **6.FUNCTION lihat_data()**

> <img width="647" height="381" alt="def lihat data" src="https://github.com/user-attachments/assets/f42308dc-4286-45e1-8659-b137ef861cf6" />

- def lihat_data():<br>
  Digunakan untuk membuat function lihat_data() yang berfungsi menampilkan seluruh data reservasi pasien yang tersimpan.<br>
- print("\n----Lihat Data Reservasi Pasien----")<br>
  Digunakan untuk menampilkan judul bagian ketika pengguna memilih untuk melihat data reservasi pasien.<br>
- data_pasien_sorted = sorted(data_pasien.values(), key=lambda x: (x[3], x[4]))<br>
  Digunakan untuk mengurutkan data pasien berdasarkan hari/tanggal dan jam reservasi.<br>
_data_pasien.values()_ digunakan untuk mengambil seluruh nilai yang ada di Dictionary data_pasien._sorted()_ digunakan untuk mengurutkan data.<br>
Bagian:<br>
-key=lambda x: (x[3], x[4])<br>
digunakan sebagai dasar pengurutan. x[3] merupakan hari/tanggal, sedangkan x[4] merupakan jam.
Hasil pengurutan disimpan ke dalam variabel data_pasien_sorted.<br>
- if data_pasien_sorted:<br>
  Digunakan untuk mengecek apakah terdapat data pasien yang bisa ditampilkan.Jika terdapat data, program akan menjalankan bagian di dalam if.
- print("\nDaftar Reservasi Pasien:")<br>
  Digunakan untuk menampilkan tulisan bahwa data yang muncul merupakan daftar reservasi pasien.
- tabel = PrettyTable()
  Digunakan untuk membuat tabel menggunakan library PrettyTable.Library ini digunakan supaya data pasien yang ditampilkan terlihat lebih rapi dalam bentuk tabel.
- tabel.field_names = ["No.Antrean", "Nama Pasien", "Nomor HP", "Keluhan", "Hari/Tanggal", "Jam"]<br>
  Digunakan untuk menentukan nama kolom pada tabel.Kolom yang ditampilkan terdiri dari nomor antrean, nama pasien, nomor HP, keluhan, hari/tanggal, dan jam.
- for i, pasien in enumerate(data_pasien_sorted, start=1):<br>
  Digunakan untuk melakukan perulangan pada setiap data pasien yang sudah diurutkan,enumerate() digunakan untuk memberikan nomor pada setiap data pasien,start=1 membuat nomor antrean dimulai dari angka 1, bukan 0.
i digunakan sebagai nomor antrean, sedangkan pasien berisi data pasien.
- tabel.add_row([<br>
    i,<br>
    pasien[0],<br>
    pasien[1],<br>
    pasien[2],<br>
    pasien[3],<br>
    pasien[4]<br>
])<br><br>
Digunakan untuk memasukkan setiap data pasien ke dalam tabel.<br>
Isi pasien berupa tuple, sehingga:<br>
pasien[0] = Nama Pasien<br>
pasien[1] = Nomor HP<br>
pasien[2] = Keluhan<br>
pasien[3] = Hari/Tanggal<br>
pasien[4] = Jam<br>
Sedangkan i digunakan sebagai nomor antrean.<br>
- print(tabel)<br>
  Digunakan untuk menampilkan tabel yang sudah dibuat menggunakan PrettyTable ke layar.<br>
- else:<br>
  Dijalankan jika tidak terdapat data pasien yang tersimpan.<br>
- print("\nTidak ada data reservasi pasien.")<br>
  Digunakan untuk memberikan informasi kepada pengguna bahwa belum ada data reservasi pasien yang dapat ditampilkan.
  

# **7.FUNCTION ubah_data()**

> <img width="665" height="406" alt="def ubah data" src="https://github.com/user-attachments/assets/48149804-5d4e-4bb9-8d40-dcf4d61b96a2" /><br>
> <img width="551" height="394" alt="def ubah data2" src="https://github.com/user-attachments/assets/1c646672-f5dd-4d71-9eb8-1aaea510b1e8" /><br>
><img width="558" height="398" alt="def ubah data3" src="https://github.com/user-attachments/assets/83a80040-7334-47ff-82d5-23491ad2a1ad" /><br>


- def hapus_data():<br>
  Digunakan untuk membuat function hapus_data(). Function ini digunakan untuk menghapus data reservasi pasien yang sudah tersimpan.<br>

- print("\n----Hapus Data Reservasi Pasien----")<br>
  Digunakan untuk menampilkan judul bagian hapus data reservasi pasien.<br>

- Kemudian:<br>
  print("1. Nomor Antrean")<br>
  print("2. Nama Pasien")<br>
  print("3. Nomor HP")<br>
  print("4. Kembali")<br>
  Menampilkan pilihan cara mencari data pasien yang ingin dihapus. Jadi pengguna bisa mencari berdasarkan nomor antrean, nama pasien, atau nomor HP.<br>

- cari = input("Masukkan pilihan (1-4): ")<br>
  Digunakan untuk menerima pilihan pengguna dan menyimpannya ke variabel cari.<br>

### Jika memilih nomor antrean

- if cari == "1":<br>
  Kalau pengguna memilih 1, data pasien akan dicari menggunakan nomor antrean.<br>

- try:<br>
  nomor = int(input("Nomor Antrean yang ingin dihapus: "))<br>
  Pengguna diminta memasukkan nomor antrean.<br>
  int() digunakan agar input menjadi angka, sedangkan try digunakan supaya kalau pengguna salah memasukkan input, program tidak langsung berhenti karena error.<br>

- data_pasien_sorted = sorted(data_pasien.values(), key=lambda x: (x[3], x[4]))<br>
  Data pasien diurutkan berdasarkan hari/tanggal dan jam, sama seperti pada lihat_data() dan ubah_data().<br>
  Ini supaya nomor antrean yang digunakan sesuai dengan urutan yang ditampilkan kepada pengguna.<br>

- if nomor >= 1 and nomor <= len(data_pasien_sorted):<br>
  Digunakan untuk mengecek apakah nomor antrean yang dimasukkan memang tersedia.<br>

- pasien = data_pasien_sorted[nomor - 1]<br>
  Digunakan untuk mengambil data pasien berdasarkan nomor antrean.<br>
  nomor - 1 digunakan karena posisi data dalam Python dimulai dari angka 0.<br>

- nama = pasien[0]<br>
  Digunakan untuk mengambil nama pasien dari data yang ditemukan.<br>

- del data_pasien[nama]<br>
  Digunakan untuk menghapus data pasien dari Dictionary data_pasien berdasarkan nama yang menjadi key.<br>

- print("\nData pasien", nama, "berhasil dihapus!")<br>
  Menampilkan pesan bahwa data pasien berhasil dihapus.<br>

- Kalau nomor antrean yang dimasukkan tidak tersedia:<br>
  print("\nData pasien tidak ditemukan.")<br>
  akan ditampilkan.<br>

- except ValueError:<br>
  print("\nData pasien tidak ditemukan.")<br>
  Bagian ini digunakan untuk menangani kesalahan ketika pengguna memasukkan sesuatu yang bukan angka pada nomor antrean.<br>
  Jadi program tidak langsung berhenti karena error.<br>

### Jika memilih berdasarkan nama

- elif cari == "2":<br>
  nama = input("Nama Pasien yang ingin dihapus: ")<br>
  Kalau pengguna memilih 2, program meminta nama pasien yang ingin dihapus.<br>

- if nama in data_pasien:<br>
  Digunakan untuk mengecek apakah nama pasien tersebut ada di Dictionary.<br>

- Kalau ada:<br>
  del data_pasien[nama]<br>
  Data pasien akan dihapus.<br>

- Kemudian:<br>
  print("\nData pasien", nama, "berhasil dihapus!")<br>
  Menampilkan pesan bahwa data berhasil dihapus.<br>

- Kalau nama tidak ditemukan, program menampilkan:<br>
  print("\nData pasien", nama, "tidak ditemukan.")<br>

### Jika memilih berdasarkan nomor HP

- elif cari == "3":<br>
  No_HP = input("Pasien yang ingin dihapus menggunakan Nomor HP: ")<br>
  Kalau memilih 3, pengguna memasukkan nomor HP pasien yang ingin dihapus.<br>

- ditemukan = False<br>
  Digunakan sebagai penanda bahwa pada awal pencarian, data pasien belum ditemukan.<br>

- for nama, pasien in list(data_pasien.items()):<br>
  Digunakan untuk mengecek data pasien satu per satu dari Dictionary.<br>
  items() digunakan untuk mengambil key dan value dari Dictionary.<br>
  list() digunakan supaya data Dictionary bisa diubah atau dihapus saat proses perulangan berlangsung.<br>

- if pasien[1] == No_HP:<br>
  Digunakan untuk membandingkan nomor HP yang tersimpan dengan nomor HP yang dimasukkan pengguna.<br>
  Kalau sama, berarti pasien yang dicari ditemukan.<br>

- del data_pasien[nama]<br>
  Digunakan untuk menghapus data pasien yang ditemukan dari Dictionary.<br>

- print("\nData pasien", nama, "berhasil dihapus!")<br>
  Menampilkan pesan bahwa data pasien berhasil dihapus.<br>

- ditemukan = True<br>
  break<br>
  ditemukan = True digunakan untuk menandakan bahwa data pasien sudah ditemukan.<br>
  break digunakan untuk menghentikan perulangan karena data yang dicari sudah ditemukan dan sudah dihapus.<br>

- if ditemukan == False:<br>
  print("\nData pasien tidak ditemukan.")<br>
  Kalau sampai pencarian selesai nilai ditemukan masih False, berarti pasien dengan nomor HP tersebut tidak ada.<br>

### Jika memilih kembali

- elif cari == "4":<br>
  print("\nKembali ke menu utama.")<br>
  Digunakan untuk kembali ke menu sebelumnya tanpa menghapus data.<br>

### Jika pilihan tidak valid

- else:<br>
  print("\nPilihan tidak valid. Silakan pilih antara 1-4.")<br>
  Digunakan jika pengguna memasukkan pilihan selain 1, 2, 3, atau 4.<br>

# **8.FUNCTION hapus_data()**

> <img width="566" height="395" alt="def hapus data1" src="https://github.com/user-attachments/assets/da259762-98ae-43aa-9a6d-317a4ed12c26" /><br>
> <img width="488" height="388" alt="def hapus data2" src="https://github.com/user-attachments/assets/0aa7db08-4ea8-4b29-b559-ed61109b0f18" /><br>
> <img width="415" height="61" alt="def hapus data3" src="https://github.com/user-attachments/assets/b0797995-116a-4899-9a1c-012173573cc6" /><br>

- def hapus_data():<br>
  Digunakan untuk membuat function hapus_data() yang digunakan untuk menghapus data pasien.<br>

- print("\n----Hapus Data Reservasi Pasien----")<br>
  Digunakan untuk menampilkan judul pada bagian hapus data reservasi pasien.<br>

- print("1. Nomor Antrean")<br>
  Menampilkan pilihan untuk mencari pasien berdasarkan nomor antrean.<br>

- print("2. Nama Pasien")<br>
  Menampilkan pilihan untuk mencari pasien berdasarkan nama.<br>

- print("3. Nomor HP")<br>
  Menampilkan pilihan untuk mencari pasien berdasarkan nomor HP.<br>

- print("4. Kembali")<br>
  Menampilkan pilihan untuk kembali ke menu sebelumnya.<br>

- cari = input("Masukkan pilihan (1-4): ")<br>
  Digunakan untuk menerima pilihan yang dimasukkan pengguna dan disimpan ke dalam variabel cari.<br>

### Jika memilih nomor antrean

- if cari == "1":<br>
  Digunakan untuk menjalankan proses jika pengguna memilih nomor 1, yaitu mencari pasien menggunakan nomor antrean.<br>

- try:<br>
  Digunakan untuk mencoba proses input nomor antrean supaya jika terjadi kesalahan input program tidak langsung berhenti.<br>

- nomor = int(input("Nomor Antrean yang ingin dihapus: "))<br>
  Digunakan untuk meminta nomor antrean yang ingin dihapus. int() digunakan supaya input yang dimasukkan berupa angka.<br>

- data_pasien_sorted = sorted(data_pasien.values(), key=lambda x: (x[3], x[4]))<br>
  Digunakan untuk mengurutkan data pasien berdasarkan hari/tanggal dan jam. Pengurutan ini sama seperti pada bagian lihat data dan ubah data.<br>

- if nomor >= 1 and nomor <= len(data_pasien_sorted):<br>
  Digunakan untuk mengecek apakah nomor antrean yang dimasukkan ada di dalam data pasien.<br>

- pasien = data_pasien_sorted[nomor - 1]<br>
  Digunakan untuk mengambil data pasien sesuai nomor antrean yang dipilih.<br>
  nomor - 1 digunakan karena urutan data pada Python dimulai dari 0.<br>

- nama = pasien[0]<br>
  Digunakan untuk mengambil nama pasien dari data yang sudah ditemukan.<br>

- del data_pasien[nama]<br>
  Digunakan untuk menghapus data pasien dari Dictionary berdasarkan nama pasien.<br>

- print("\nData pasien", nama, "berhasil dihapus!")<br>
  Digunakan untuk menampilkan pesan bahwa data pasien berhasil dihapus.<br>

- else:<br>
  Dijalankan jika nomor antrean yang dimasukkan tidak ada.<br>

- print("\nData pasien tidak ditemukan.")<br>
  Menampilkan pesan bahwa data pasien tidak ditemukan.<br>

- except ValueError:<br>
  Digunakan untuk menangani kesalahan jika pengguna memasukkan sesuatu yang bukan angka pada nomor antrean.<br>

### Jika memilih nama pasien

- elif cari == "2":<br>
  Digunakan jika pengguna memilih nomor 2, yaitu mencari pasien berdasarkan nama.<br>

- nama = input("Nama Pasien yang ingin dihapus: ")<br>
  Digunakan untuk meminta nama pasien yang ingin dihapus.<br>

- if nama in data_pasien:<br>
  Digunakan untuk mengecek apakah nama pasien yang dimasukkan ada di dalam Dictionary data_pasien.<br>

- del data_pasien[nama]<br>
  Jika nama pasien ditemukan, data pasien tersebut akan dihapus.<br>

- print("\nData pasien", nama, "berhasil dihapus!")<br>
  Menampilkan pesan bahwa data pasien berhasil dihapus.<br>

- else:<br>
  Dijalankan jika nama pasien tidak ditemukan.<br>

- print("\nData pasien", nama, "tidak ditemukan.")<br>
  Menampilkan pesan bahwa data pasien yang dicari tidak ditemukan.<br>

### Jika memilih nomor HP

- elif cari == "3":<br>
  Digunakan jika pengguna memilih nomor 3, yaitu mencari pasien berdasarkan nomor HP.<br>

- No_HP = input("Pasien yang ingin dihapus menggunakan Nomor HP: ")<br>
  Digunakan untuk meminta nomor HP pasien yang ingin dihapus.<br>

- ditemukan = False<br>
  Digunakan sebagai tanda bahwa data pasien belum ditemukan.<br>

- for nama, pasien in list(data_pasien.items()):<br>
  Digunakan untuk mengecek data pasien satu per satu dari Dictionary.<br>
  items() digunakan untuk mengambil nama dan data pasien yang ada di dalam Dictionary.<br>

- if pasien[1] == No_HP:<br>
  Digunakan untuk mengecek apakah nomor HP yang dimasukkan sama dengan nomor HP yang tersimpan.<br>

- del data_pasien[nama]<br>
  Digunakan untuk menghapus data pasien yang nomor HP-nya sudah ditemukan.<br>

- print("\nData pasien", nama, "berhasil dihapus!")<br>
  Menampilkan pesan bahwa data pasien berhasil dihapus.<br>

- ditemukan = True<br>
  Digunakan untuk menandakan bahwa data pasien sudah ditemukan.<br>

- break<br>
  Digunakan untuk menghentikan perulangan setelah data pasien ditemukan dan dihapus.<br>

- if ditemukan == False:<br>
  Digunakan untuk mengecek apakah data pasien tidak ditemukan setelah semua data diperiksa.<br>

- print("\nData pasien tidak ditemukan.")<br>
  Menampilkan pesan bahwa data pasien tidak ditemukan.<br>

### Jika memilih kembali

- elif cari == "4":<br>
  Digunakan jika pengguna memilih nomor 4 untuk kembali.<br>

- print("\nKembali ke menu utama.")<br>
  Menampilkan pesan bahwa pengguna kembali ke menu utama.<br>

### Jika pilihan tidak sesuai

- else:<br>
  Dijalankan jika pengguna memasukkan pilihan selain 1 sampai 4.<br>

- print("\nPilihan tidak valid. Silakan pilih antara 1-4.")<br>
  Menampilkan pesan bahwa pilihan yang dimasukkan tidak sesuai dengan pilihan yang tersedia.<br>

# **9.FUNCTION menu_admin()**

> <img width="515" height="416" alt="def menu admin1" src="https://github.com/user-attachments/assets/de0f81c0-2436-4ff7-b85d-625f753c3dc4" /><br>
> <img width="424" height="53" alt="def menu admin2" src="https://github.com/user-attachments/assets/6b077a32-ee91-4a01-9f66-5e530101cae7" /><br>

- def menu_admin():<br>
  Digunakan untuk membuat function menu_admin() yang berisi menu khusus untuk admin.<br>

- while True:<br>
  Digunakan supaya menu admin bisa terus digunakan dan kembali muncul setelah admin selesai melakukan suatu pilihan.<br>

- print("\n" + "✦== JADWAL PASIEN KLINIK ==✦")<br>
  Digunakan untuk menampilkan judul program pada menu admin.<br>

- print("✦==    DRG.SEPTIYA      ==✦")<br>
  Digunakan untuk menampilkan nama klinik pada program.<br>

- print("\n-----MENU-----")<br>
  Digunakan untuk menampilkan bagian menu.<br>

- print("1. Tambah Data Reservasi Pasien")<br>
  Menampilkan pilihan untuk menambahkan data reservasi pasien.<br>

- print("2. Lihat Data Reservasi Pasien")<br>
  Menampilkan pilihan untuk melihat data reservasi pasien.<br>

- print("3. Ubah Jadwal Reservasi Pasien")<br>
  Menampilkan pilihan untuk mengubah jadwal reservasi pasien.<br>

- print("4. Hapus Data Reservasi Pasien")<br>
  Menampilkan pilihan untuk menghapus data reservasi pasien.<br>

- print("5. Keluar")<br>
  Menampilkan pilihan untuk keluar dari menu admin dan kembali ke menu utama.<br>

- pilihan = input("Masukkan pilihan (1-5): ")<br>
  Digunakan untuk menerima pilihan yang dimasukkan admin dan menyimpannya ke dalam variabel pilihan.<br>

- if pilihan == "1":<br>
  Digunakan untuk mengecek apakah admin memilih pilihan nomor 1.<br>

- tambah_data()<br>
  Jika admin memilih nomor 1, function tambah_data() akan dijalankan untuk menambahkan data pasien.<br>

- elif pilihan == "2":<br>
  Digunakan untuk mengecek apakah admin memilih pilihan nomor 2.<br>

- lihat_data()<br>
  Jika admin memilih nomor 2, function lihat_data() akan dijalankan untuk menampilkan data pasien.<br>

- elif pilihan == "3":<br>
  Digunakan untuk mengecek apakah admin memilih pilihan nomor 3.<br>

- ubah_data()<br>
  Jika admin memilih nomor 3, function ubah_data() akan dijalankan untuk mengubah jadwal pasien.<br>

- elif pilihan == "4":<br>
  Digunakan untuk mengecek apakah admin memilih pilihan nomor 4.<br>

- hapus_data()<br>
  Jika admin memilih nomor 4, function hapus_data() akan dijalankan untuk menghapus data pasien.<br>

- elif pilihan == "5":<br>
  Digunakan untuk mengecek apakah admin memilih pilihan nomor 5.<br>

- print("\nKembali ke menu utama.")<br>
  Menampilkan pesan bahwa admin akan kembali ke menu utama.<br>

- break<br>
  Digunakan untuk menghentikan perulangan pada menu admin sehingga program kembali ke menu utama.<br>

- else:<br>
  Dijalankan jika admin memasukkan pilihan selain 1 sampai 5.<br>

- print("\nPilihan tidak valid. Silakan pilih antara 1-5.")<br>
  Menampilkan pesan bahwa pilihan yang dimasukkan tidak sesuai dengan pilihan menu yang tersedia.<br>


# **10.FUNCTION menu_user()**

> <img width="530" height="346" alt="def menu user1" src="https://github.com/user-attachments/assets/76972110-9266-4d05-89e7-a234998d3702" /><br>
> <img width="573" height="353" alt="def menu user2" src="https://github.com/user-attachments/assets/5f0d5bcb-2f85-42af-911a-4c48ba97519a" /><br>

- def menu_user():<br>
  Digunakan untuk membuat function menu_user() yang berisi menu khusus untuk user.<br>

- while True:<br>
  Digunakan supaya menu user bisa terus digunakan sampai user memilih untuk keluar.<br>

- print("\n" + "✦== JADWAL PASIEN KLINIK ==✦")<br>
  Digunakan untuk menampilkan judul program pada menu user.<br>

- print("✦==    DRG.SEPTIYA      ==✦")<br>
  Digunakan untuk menampilkan nama klinik pada program.<br>

- print("\n-----MENU-----")<br>
  Digunakan untuk menampilkan bagian menu user.<br>

- print("1. Lihat Data Reservasi Pasien")<br>
  Menampilkan pilihan untuk melihat data reservasi pasien yang sudah tersimpan.<br>

- print("2. Keluar")<br>
  Menampilkan pilihan untuk keluar dari menu user dan kembali ke menu utama.<br>

- pilihan = input("Masukkan pilihan (1-2): ")<br>
  Digunakan untuk menerima pilihan yang dimasukkan user dan menyimpannya ke dalam variabel pilihan.<br>

- if pilihan == "1":<br>
  Digunakan untuk mengecek apakah user memilih pilihan nomor 1.<br>

- lihat_data()<br>
  Jika user memilih nomor 1, function lihat_data() akan dijalankan untuk menampilkan data reservasi pasien.<br>

- elif pilihan == "2":<br>
  Digunakan untuk mengecek apakah user memilih pilihan nomor 2.<br>

- print("\nKembali ke menu utama.")<br>
  Menampilkan pesan bahwa user akan kembali ke menu utama.<br>

- break<br>
  Digunakan untuk menghentikan perulangan pada menu user sehingga user kembali ke menu utama.<br>

- else:<br>
  Dijalankan jika user memasukkan pilihan selain 1 atau 2.<br>

- print("\nPilihan tidak valid. Silakan pilih antara 1-2.")<br>
  Menampilkan pesan bahwa pilihan yang dimasukkan tidak sesuai dengan pilihan menu yang tersedia.<br>







# HASIL OUTPUT


# **1.TAMPILAN AWAL PROGRAM KETIKA AWAL DI JALANKAN**

ADA MENU:
  - ADMIN
  - USER
  - KELUAR
     
> <img width="219" height="187" alt="tampilan awal program" src="https://github.com/user-attachments/assets/91eaba34-538e-477b-9279-c4d8b742aa3f" />

# **2.MENU ADMIN**

Jika memilih ADMIN pada menu utama, program akan meminta username dan password untuk login sebagai admin.

**- TAMPILAN JIKA LOGIN ADMIN GAGAL**

Jika username atau password yang dimasukkan salah, program akan menampilkan pesan bahwa username atau password salah dan pengguna diminta untuk mencoba lagi.

> <img width="302" height="257" alt="pilih menu admin dan password salah" src="https://github.com/user-attachments/assets/2a1dc161-d446-4c0f-ae35-7c9bd32aa912" />

**- TAMPILAN JIKA LOGIN ADMIN BERHASIL**

Jika username dan password yang dimasukkan benar, program akan menampilkan pesan login berhasil.

> <img width="190" height="227" alt="pilih menu admin dan login berhasil" src="https://github.com/user-attachments/assets/d2e1f2f2-38ab-420e-bbb4-71d9242506e1" />

(Setelah berhasil login, program akan menunggu selama 3 detik kemudian layar dibersihkan dan menampilkan menu admin)

**- TAMPILAN MENU-MENU YANG ADA DI DALAM MENU ADMIN**

Menu admin memiliki beberapa pilihan yaitu:
- Tambah Data Reservasi Pasien
- Lihat Data Reservasi Pasien
- Ubah Jadwal Reservasi Pasien
- Hapus Data Reservasi Pasien
- Keluar

> <img width="221" height="194" alt="tampilan menu admin,dan ke clear karena pake os" src="https://github.com/user-attachments/assets/0628f643-3a77-4f3a-907c-e033dd78b203" />

**- JIKA MEMILIH MENU 1 (TAMBAH DATA RESERVASI PASIEN) DAN MENAMBAHKAN DATA PASIEN 1/BERHASIL MENAMBAHKAN DATA PASIEN**

<img width="257" height="273" alt="pilih menu 1 dan nambah pasien1" src="https://github.com/user-attachments/assets/068df3f1-9fb4-4c57-a4da-77d29e536c31" />

**-MENAMBAHKAN DATA PASIEN KE 2-4**

> <img width="254" height="259" alt="tambah data pasien 2" src="https://github.com/user-attachments/assets/ebccd0b1-d179-4a65-af9f-7c0d42e79d12" />

> <img width="251" height="273" alt="tambah pasien3" src="https://github.com/user-attachments/assets/54d36942-894a-4fe9-b570-17c9a78616bf" />

> <img width="241" height="272" alt="tambah pasien 4" src="https://github.com/user-attachments/assets/c2515ead-b04a-4633-b4fb-d883440c22ab" />

**- JIKA MEMILIH MENU 1 (TAMBAH DATA RESERVASI PASIEN) DAN MENAMBAHKAN DATA PASIEN GAGAL/TIDAK LENGKAP**

<img width="249" height="250" alt="jika tidak memasukkan data pasien dengan lengkap" src="https://github.com/user-attachments/assets/7c648cd6-3a12-41f9-b525-8c99112124d2" />


**- JIKA MEMILIH MENU 2 (LIHAT DATA RESERVASI PASIEN)DAN HASIL DARI LIHAT DATA PASIEN BERHASIL**

> <img width="526" height="326" alt="hasil lihat pasien" src="https://github.com/user-attachments/assets/71a3b1d4-6c7c-4011-8832-70bd1c19773d" />

**- JIKA MEMILIH MENU 3 (UBAH DATA RESERVASI PASIEN)DAN HASIL DARI PILIHAN UBAH DATA PASIEN**
  Jika memilih menu 3, admin dapat memilih cara mencari data pasien yang ingin diubah, yaitu berdasarkan:
- Nomor Antrean
- Nama Pasien
- Nomor HP
- Kembali
  
> <img width="244" height="250" alt="menu di dalam ubah jadwal" src="https://github.com/user-attachments/assets/cf90cf9c-010b-478b-bbb5-854b20e44281" />

- TAMPILAN GAGAL UBAH DATA PASIEN MENGGUNAKAN NOMOR ANTRIAN

> <img width="275" height="287" alt="gagal ubah basien pakai no antrian" src="https://github.com/user-attachments/assets/d5bd6f62-ed90-421e-ab93-8332744b155c" />

- TAMPILAN BERHASIL UBAH DATA PASIEN MENGGUNAKAN NOMOR ANTRIAN

> <img width="256" height="178" alt="ubah pakai no antrian berhasil" src="https://github.com/user-attachments/assets/76a8c369-b785-4149-9401-813fc6b34aed" />

- TAMPILAN GAGAL UBAH DATA PASIEN MENGGUNAKAN NAMA PASIEN

  > <img width="239" height="143" alt="ubah pasien pakai nama gagal" src="https://github.com/user-attachments/assets/a1629c5e-e751-44ab-aa20-1f03e3b18122" />

- TAMPILAN BERHASIL UBAH DATA PASIEN MENGGUNAKAN NAMA PASIEN

><img width="269" height="172" alt="ubah pakai nama berhasil" src="https://github.com/user-attachments/assets/c647a6c4-8c21-4740-aa55-497804d14f2b" />

- TAMPILAN GAGAL UBAH DATA PASIEN MENGGUNAKANNO HP

- TAMPILAN BERHASIL UBAH DATA PASIEN MENGGUNAKAN NOMOR HP

- TAMPILAN PILIH MENU UBAH DATA 1-4 GAGAL<br>
  > <img width="345" height="272" alt="hasil menu di dalam ubah dan salah input nomor" src="https://github.com/user-attachments/assets/6655f3ec-6cec-4801-b27b-3bcb2d078984" />

- TAMPILAN BERHASIL KELUAR DARI MENU UBAH DAN KEMBALI KE MENU UTAMA ADMIN<br>
  > <img width="257" height="272" alt="kembali ke menu utama saat di dalam ubah" src="https://github.com/user-attachments/assets/ed5c2fcd-05e7-4892-86ec-22d1669a28ee" />

- TAMPILAN DARI HASIL MELIHAT DATA RESERVASI SETELAH DIUBAH<br>
  > <img width="491" height="320" alt="lihat data setelah di ubah datanya" src="https://github.com/user-attachments/assets/6d79987e-65ce-4bd2-95e4-4718df211d9c" />


**- JIKA MEMILIH MENU 4 (HAPUS DATA RESERVASI PASIEN) DAN HASIL DARI PILIHAN HAPUS DATA PASIEN**

Jika memilih menu 4, admin dapat memilih cara mencari data pasien yang ingin dihapus, yaitu berdasarkan:<br>
- Nomor Antrean
- Nama Pasien
- Nomor HP
- Kembali


- TAMPILAN GAGAL HAPUS DATA PASIEN MENGGUNAKAN NOMOR ANTRIAN
  > <img width="287" height="239" alt="hapus pake no antrian gagal" src="https://github.com/user-attachments/assets/02370a55-4ec9-40d5-8b64-c344bddcf802" />

- TAMPILAN BERHASIL HAPUS DATA PASIEN MENGGUNAKAN NOMOR ANTRIAN
  > <img width="248" height="173" alt="hapus pakai no antrian berhasil" src="https://github.com/user-attachments/assets/ea8a3943-48a1-4b05-9a5e-e42e9757ec79" />

- TAMPILAN GAGAL HAPUS DATA PASIEN MENGGUNAKAN NAMA PASIEN
  > <img width="256" height="139" alt="gagal hapus pake nama pasien" src="https://github.com/user-attachments/assets/8795d6ac-b821-4ecd-9409-70bd541b663e" />

- TAMPILAN BERHASIL HAPUS DATA PASIEN MENGGUNAKAN NAMA PASIEN
  > <img width="263" height="138" alt="hapus pakai nama pasien berhasil" src="https://github.com/user-attachments/assets/8aa43f9d-dc8d-4f80-a944-073cbeca1b24" />


- TAMPILAN GAGAL HAPUS DATA PASIEN MENGGUNAKAN NOMOR HP
  
- TAMPILAN BERHASIL HAPUS DATA PASIEN MENGGUNAKAN NOMOR HP

- TAMPILAN PILIH MENU HAPUS DATA 1-4 GAGAL<br>
> <img width="286" height="280" alt="salah pilih no di menu hapus" src="https://github.com/user-attachments/assets/308b4757-f7c2-4967-8011-881808878560" />

- TAMPILAN BERHASIL KELUAR DARI MENU HAPUS DAN KEMBALI KE MENU UTAMA ADMIN<br>
> <img width="254" height="128" alt="kembali ke menu dalam hapus" src="https://github.com/user-attachments/assets/99340f34-aef7-4a94-8f8f-1f909fd31f39" />


- TAMPILAN DARI HASIL MELIHAT DATA RESERVASI SETELAH DIUBAH<br>

# **GAGAL MEMILIH MENU UTAMA ADMIN 1-5**<br>
> <img width="337" height="330" alt="gagal pilih menu 1-5" src="https://github.com/user-attachments/assets/d3750a6d-0b76-45e9-8314-805eb6644c25" />

# **BERHASIL KELUAR DARI PROGRAM (MEMILIH MENU 5.KEMBALI) DAN KEMBALI KE MENU UTAMA**

# **3.MENU USER**

Jika memilih USER pada menu utama, program akan meminta username dan password untuk login sebagai USER.

**- TAMPILAN JIKA LOGIN USER GAGAL**

> <img width="371" height="272" alt="user salah" src="https://github.com/user-attachments/assets/e1b611d6-9e1b-4706-bfee-ce70a78a8cbc" />

Jika username atau password yang dimasukkan salah, program akan menampilkan pesan bahwa username atau password salah dan pengguna diminta untuk mencoba lagi.

**- TAMPILAN JIKA LOGIN USER BERHASIL**

Jika username dan password yang dimasukkan benar, program akan menampilkan pesan login berhasil.

**- TAMPILAN MENU-MENU YANG ADA DI DALAM MENU ADMIN**

Menu USER memiliki pilihan yaitu:<br>
- Lihat Data Reservasi Pasien
- Keluar

> <img width="230" height="128" alt="tampilan di dalam user" src="https://github.com/user-attachments/assets/c8bcd257-ee8e-45c7-a81e-f12e29667588" />

(Setelah berhasil login, program akan menunggu selama 3 detik kemudian layar dibersihkan dan menampilkan menu USER)

**- TAMPILAN JIKA MEMILIH MENU 1 LIHAT DATA PASIEN**
> <img width="530" height="248" alt="lihat data di user" src="https://github.com/user-attachments/assets/04cf3de3-b11e-4f6c-b34d-022fa90a8ad7" />

**- TAMPILAN JIKA SALAH MEMILIH MENU 1-2 DI USER**

> <img width="352" height="260" alt="salah pilih menu 1-2 di user" src="https://github.com/user-attachments/assets/f12a6940-e4f8-4350-a6c7-7b6aedfd768c" />

**- TAMPILAN JIKA KELUAR DARI MENU USER DAN KEMBALI KE MENU AWAL**

> <img width="230" height="224" alt="kembali di menu utama dari dalam user" src="https://github.com/user-attachments/assets/af1904d6-8202-489b-9a6f-c0548233c8d1" />


















