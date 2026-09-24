Pertemuan 04 — Seleksi Multi-Kondisi dan Validasi Input

Nama: Fahrezi Sauqi Alghani
NIM: 2225250029
Kelas: 3E

Tujuan

Membangun program Python yang menggunakan seleksi multi-kondisi dengan "if-elif-else" serta melakukan validasi input berdasarkan tipe data dan rentang nilai.

Program pada pertemuan ini juga bertujuan untuk memastikan setiap kondisi dapat diproses dengan benar melalui tabel keputusan dan pengujian pada setiap cabang.

Struktur Folder

pertemuan-04-validasi-NIM/
│
├── README.md
├── .gitignore
│
├── latihan/
│   ├── 01_predikat_nilai.py
│   ├── 02_kategori_bilangan.py
│   ├── 03_validasi_rentang.py
│   ├── 04_validasi_tipe.py
│   └── 05_klasifikasi_segitiga_sudut.py
│
└── praktik/
    └── validasi_klasifikasi_nilai.py

Materi

Materi yang dipelajari pada pertemuan ini meliputi:

- Seleksi multi-kondisi menggunakan "if-elif-else"
- Klasifikasi berdasarkan rentang nilai
- Urutan kondisi dalam "if-elif-else"
- Validasi tipe data
- Validasi rentang nilai
- Validasi domain pilihan
- Penggunaan "try-except ValueError"
- Penyusunan tabel keputusan
- Penyusunan test case
- Pengujian program menggunakan berbagai kondisi input

Cara Menjalankan

Pastikan Python sudah terpasang pada komputer.

Untuk menjalankan program Praktik 1:

python3 praktik/validasi_klasifikasi_nilai.py

Pada Windows, perintah berikut juga dapat digunakan:

python praktik/validasi_klasifikasi_nilai.py

Tabel Keputusan

Program Praktik 1 menghitung nilai akhir menggunakan rumus:

Nilai Akhir = (0.6 × Nilai Ujian) + (0.4 × Nilai Tugas)

Predikat| Syarat Nilai Akhir
A| Nilai akhir >= 85
B| Nilai akhir >= 70
C| Nilai akhir >= 60
D| Nilai akhir >= 50
E| Nilai akhir < 50

Ketentuan kehadiran:

- Kehadiran kurang dari 80% → Tidak memenuhi syarat kehadiran
- Kehadiran minimal 80% → dapat dilanjutkan ke proses penentuan predikat.
- Predikat A, B, dan C → Lulus
- Predikat D dan E → Belum lulus

Validasi Input

Program melakukan validasi terhadap tiga data masukan:

1. Nilai ujian
   
   - Harus berupa angka.
   - Berada pada rentang 0 sampai 100.

2. Nilai tugas
   
   - Harus berupa angka.
   - Berada pada rentang 0 sampai 100.

3. Kehadiran
   
   - Harus berupa angka.
   - Berada pada rentang 0 sampai 100.

Jika input bukan angka, program menggunakan "try-except ValueError" untuk memberikan pesan penolakan.

Hasil Pengujian

Ujian| Tugas| Kehadiran| Nilai Akhir| Keluaran Diharapkan| Status
90| 80| 95| 86.00| Predikat A, Lulus| Sesuai
75| 70| 85| 73.00| Predikat B, Lulus| Sesuai
60| 60| 80| 60.00| Predikat C, Lulus| Sesuai
55| 50| 90| 53.00| Predikat D, Belum lulus| Sesuai
40| 30| 100| 36.00| Predikat E, Belum lulus| Sesuai
90| 90| 75| 90.00| Tidak memenuhi syarat kehadiran| Sesuai
105| 80| 90| -| Penolakan nilai ujian| Sesuai
80| -5| 90| -| Penolakan nilai tugas| Sesuai
80| 80| abc| -| Penolakan tipe input| Sesuai

Contoh Alur Program

Program menjalankan proses dengan urutan:

Input
  ↓
Validasi tipe data
  ↓
Validasi rentang 0–100
  ↓
Menghitung nilai akhir
  ↓
Memeriksa kehadiran
  ↓
Menentukan predikat
  ↓
Menentukan status kelulusan
  ↓
Output

Refleksi

Pada pembuatan program ini, saya mempelajari bahwa penggunaan "if-elif-else" harus memperhatikan urutan kondisi agar hasil klasifikasi tidak keliru. Kondisi untuk predikat disusun dari nilai tertinggi ke nilai terendah sehingga setiap nilai dapat masuk ke kategori yang sesuai.

Saya juga memahami pentingnya validasi input sebelum data diproses. Input yang bukan angka ditangani menggunakan "try-except ValueError", sedangkan input yang berada di luar rentang 0 sampai 100 ditolak dengan pesan yang sesuai.

Pengujian dilakukan menggunakan nilai normal, nilai batas, nilai di luar rentang, dan input bukan angka untuk memastikan setiap kondisi program dapat berjalan dengan baik.

Kesimpulan

Seleksi multi-kondisi dengan "if-elif-else" dapat digunakan untuk menentukan satu kategori dari beberapa kemungkinan berdasarkan kondisi tertentu. Validasi input diperlukan agar data yang diproses sesuai dengan aturan program.

Melalui latihan dan Praktik 1, program dapat menggabungkan validasi tipe, validasi rentang, perhitungan nilai akhir, klasifikasi predikat, serta penentuan status kelulusan dalam satu alur program.

Referensi

- RPS Algoritma dan Pemrograman OBE Untirta, Tahun Ajaran 2026/2027 Ganjil.
- Downey, A. B. (2015). Think Python: How to Think Like a Computer Scientist (2nd ed.).
- Sweigart, A. (2019). Automate the Boring Stuff with Python.
- Python Software Foundation. Python Tutorial: More Control Flow Tools.
- Python Software Foundation. Python Tutorial: Errors and Exceptions.
- Visual Studio Code. Python Tutorial dan Python Debugging.

Integritas Akademik

Kode, tabel keputusan, hasil pengujian, dan refleksi dalam repositori ini dibuat dan dipahami oleh pemilik repositori. Dokumentasi resmi dan sumber pembelajaran digunakan sebagai referensi dalam memahami materi.