# Menu Order Recording
Web aplikasi/API untuk mencatat pesanan di restoran.

## Daftar Isi
- [Requirements](##Requirements)
- [Cara Instalasi](##CaraInstalasi)
- [Struktur Aplikasi](##StrukturAplikasi)

## Requirements
- python 3.8
- pip
- postgresql (recomend version 13)
- redis (recomend version 6)

## CaraInstalasi
1. buat virtual environtment `python -m venv env`
1. aktivasi virtual environtment `source env/bin/activate`
1. Install depedency `pip install -r requirements.txt`
1. Copy dan rename app/settings.py.example menjadi app/settings.py lalu isi settings.py berdasarkan konfigurasi postgresql dan redis yang digunakan
1. jalankan aplikasi `python manage.py runserver {port}`

## StrukturAplikasi
- app/
    - common/ (untuk menyimpan fungsi yang bisa digunakan oleh beberapa django app (contoh menu, order))
- menu/
- order/
- endpoint.py (list dokumentasi api di browserable api)
- manage.py (entrypoint)
- requirements.txt (untuk menyimpan depedenci yang digunakan aplikasi)

pada setiap django app terdapat file-file berikut dan fungsinya:
- models.py (menyimpan struktur tabel)
- serializers.py (menyimpan fungsi serializer untuk melakukan validasi json, konversi json ke dictionary dan konversi dictionary ke json)
- services.py (menyimpan bisnis logic ketika menyimpan atau mengambil data ke database)
- views.py (menghubungkan model, serializer dan services, mirip seperti controller)
- urls.py (mapping routing ke fungsi pada views)
- tests.py (untuk testing aplikasi)

Kenapa struktur setiap app di buat seperti itu. Untuk file models.py, serializers.py, views.py dan urls.py saya mengikuti struktur standard pada dokumentasi Django dan djangorestframework. Tujuanya memudahkan ketika harus instalasi package third party. Karena kebanyakan package third party berasumsi pengguna menggunakan struktur folder standar di dokumentasi. Untuk file services.py ini berawal dari kesulitan tim saya dalam membaca dan memodifikasi program, dimana bisnis proses terbesar di beberapa file. Ada bisnis proses di tulis di models.py, serializers.py dan views.py. Lalu kami mendapat inspirasi dari video konferesi python di youtube [Radoslav Georgiev - Django structure for scale and longevity](https://www.youtube.com/watch?v=yG3ZdxBb1oo) mengenai service pattern. Kami mencoba menerapkan service pattern dan ternyata bekerja dengan baik.
