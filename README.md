Nama: A. Sherwyn Fawwaz Nitisara Suthaputra
NPM: 2306165811
Kelas : PBP F

TUGAS INDIVIDU 2

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab: 
1. Membuat sebuah proyek Django baru bernama share_store yang merupakan subdirektori dari direktori utama bernama share-store. Kemudian memastikan keduanya terhubung pada github.
2. Mengaktifkan virtual environment untuk membuat aplikasi main dalam proyek share_store. Kemudian mendaftarkan aplikasi main tersebut ke dalam proyek.
3. Setelah mendaftarkan aplikasi main tersebut ke dalam proyek,kita membuat folder templates ke dalam subdirektori main untuk menampilkan data program.
4. Membuat file main.html di dalam templates, kemudian mengisi data program sesuai dengan jenis konten yang kita inginkan.
5. Mengubah file models.py dalam aplikasi main untuk mendefinisikan model baru
6. Menghubungkan view dan template dengan menambahkan sebuah fungsi show_main dalam views.py dan memodifikasi main.html dengan template variables. Di proses ini terjadi proses render tampilan main.html.
7. Mengonfigurasi Routing URL. Terdapat dua file URL, yaitu urls.py (main) dan urls.py (share_store). URL pada main berfungsi untuk mengatur rute URL spesifik untuk fitur-fitur dalam aplikasi main tersebut. Sedangkan URL pada share_store berfungsi untuk bertanggung jawab untuk mengatur rute URL tingkat proyek. Sehingga memungkinkan  aplikasi dalam proyek Django untuk bersifat modular dan terpisah.
8. Pastikan seluruh proses terhubung dengan github dan PWS, serta tampilan HTML di peramban web.

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Jawab:
Client melakukan request di browser -> terjadi proses di webserver environment -> run django -> menerima request dan mencocokkannya dengan pola URL pada urls.py -> Jika sesuai, akan diteruskan ke views.py -> mengambil data dalam database di models.py -> data diperoleh dan diproses kembali di views.py -> menggunakan template main.html untuk merender tampilan halaman -> Django mengirimkan response berupa halaman web yang sudah berisi data kembali ke client.

Jelaskan fungsi git dalam pengembangan perangkat lunak!
Jawab:
Fungsi git dalam pengembangan perangkat lunak sangat penting karena:
1. Git dapat membantu dalam mengatur direktori dalam pengembangan proyek
2. Git dapat memungkinkan pengembang untuk melacak setiap perubahan yang dilakukan pada sumber kode, sehingga dapat mengetahui kapan dan siapa yang membuat perubahan pada kode, serta detail perubahan tersebut.
3. Git memungkinkan banyak pengembang untuk bekerja secara bersamaan pada proyek yang sama tanpa saling mengganggu dengan menggunakan branch.
4. Git dapat membantu dalam melihat riwayat perubahan dan dapat diakses kapan saja, serta pengembang dapat memulihkan kode yang telah terhapus.

Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Jawab:
Framework Django cocok dijadikan permulaan pembelajaran pengembangan perangkat lunak karena:
1. Django dikenal memiliki dokumentasi yang sangat lengkap dan mudah dipahami bagi pemula
2. Django menggunakan pola MVT(Model-view-template) yang membantu pengembang memisahkan logika aplikasi, data, dan tampilan yang terstruktur.
3. Django dikembangkan menggunakan aplikasi python yang ramah karena sintaksnya yang mudah dipahami.
4. Django menyediakan banyak fitur keamanan bawahan, seperti serangan SQL injection, Cross Site Scripting, dll.

Mengapa model pada Django disebut sebagai ORM?
Jawab: 
Model pada Django disebut ORM (Object Relational Mapping) karena Django menggunakan konsep ini untuk memetakan data objek-objek Python ke dalam tabel-tabel database relasional dan sebaliknya, sehingga memungkinkan pengembang untuk bekerja dengan data menggunakan pendekatan berorientasi objek tanpa harus berinteraksi langsung dengan SQL.

-------------------------------------------------------------------------------------------

TUGAS INDIVIDU 3

Mengapa Data Delivery Diperlukan dalam Pengembangan Platform?
Jawab:
Data delivery penting dalam pengembangan platform karena memastikan informasi yang disimpan di server atau database pusat dapat diakses oleh pengguna dari berbagai lokasi. Dengan data delivery, platform dapat berkomunikasi dan terintegrasi dengan layanan lain seperti API eksternal, memungkinkan data untuk dikirim dan diterima dalam format yang sesuai. Hal ini mendukung kolaborasi dan interaksi efisien antar sistem, serta memastikan komunikasi data antara berbagai komponen platform berjalan dengan lancar, memfasilitasi akses dan pemrosesan informasi yang tepat.

Mana yang Lebih Baik: XML atau JSON? Mengapa JSON Lebih Populer?
Jawab:
JSON lebih populer dibandingkan XML karena memiliki format yang lebih sederhana dan mudah dibaca. JSON menggunakan {} untuk merepresentasikan objek dan array, sementara XML menggunakan tag <tag>...</tag> untuk setiap elemen, membuatnya lebih panjang dan sulit dibaca. XML cocok untuk dokumen yang membutuhkan struktur kompleks dan detil, sedangkan JSON lebih sering digunakan untuk aplikasi yang membutuhkan komunikasi data cepat dan efisien.

Jelaskan fungsi dari method is_valid() pada Form Django dan Pentingnya
Method is_valid() 
Jawab:
Pada form Django digunakan untuk memvalidasi data input yang dimasukkan ke dalam form, memastikan data tersebut sesuai dengan aturan yang telah ditentukan (misalnya tipe data, panjang maksimal, atau format yang benar). Jika data valid, method ini mengembalikan nilai True, dan jika tidak valid, mengembalikan False. Method ini penting untuk mencegah data yang tidak sesuai masuk ke dalam sistem.

Mengapa csrf_token Diperlukan di Form Django dan Apa Risikonya Tanpa CSRF?
Jawab:
csrf_token digunakan dalam form Django untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery), di mana penyerang mencoba memanipulasi pengguna agar melakukan tindakan yang tidak diinginkan. Dengan menambahkan csrf_token dalam form, aplikasi dapat memverifikasi bahwa permintaan berasal dari sumber yang sah. Jika tidak menambahkan csrf_token, penyerang bisa mengeksploitasi sesi pengguna yang sudah login untuk melakukan tindakan yang merugikan, seperti mengubah pengaturan akun atau mencuri data pribadi tanpa persetujuan pengguna. Tanpa CSRF token, aplikasi dapat memproses permintaan palsu yang tampak seperti berasal dari pengguna yang sah.

Langkah-langkah Implementasi Checklist pada Django
Jawab:
1. Buat direktori templates di direktori utama dan buat file HTML bernama base.html yang berisi kerangka halaman web.
2. Tambahkan konfigurasi di DIRS pada settings.py, lalu buat extends dan block content di main.html. Import uuid di models.py dan lakukan migrasi.
3. Buat file forms.py di direktori main untuk membuat form, simpan form sebagai objek, dan tambahkan import di views.py dengan fungsi yang menerima parameter request.
4. Modifikasi fungsi show_main untuk menggunakan Product.objects.all() untuk mengambil data dari database.
5. Import fungsi yang sudah dibuat, tambahkan path URL di urlpatterns dan urls.py di main. Buat file create_product.html di main/templates, dan tambahkan {% block content %} di main.html untuk menampilkan data.
6. Jalankan proyek dengan python manage.py runserver dan buka di http://localhost:8000/.
7. Buat fungsi show_xml di views.py, tambahkan path URL di urls.py, dan buka di http://localhost:8000/xml/.
8. Buat fungsi show_json di views.py, tambahkan path URL di urls.py, lalu jalankan proyek di http://localhost:8000/json/.
9. Buat fungsi show_xml_by_id dan show_json_by_id di views.py, tambahkan path URL di urls.py, lalu akses di http://localhost:8000/json/[id]/ atau http://localhost:8000/xml/[id]/.
10. Uji endpoint di Postman, lalu lakukan push ke GitHub dan PWS.

Bukti screenshot Postman:
1. http://localhost:8000/xml/
![alt text](<Tangkapan Layar 2024-09-18 pukul 11.24.11.png>)
2. http://localhost:8000/xml/[id]/ 
![alt text](<Tangkapan Layar 2024-09-18 pukul 11.27.33.png>)
3. http://localhost:8000/json/
![alt text](<Tangkapan Layar 2024-09-18 pukul 11.32.17.png>)
4. http://localhost:8000/json/[id]/
![alt text](<Tangkapan Layar 2024-09-18 pukul 11.28.48.png>)


-------------------------------------------------------------------------------------------

TUGAS INDIVIDU 4

Apa perbedaan antara HttpResponseRedirect() dan redirect()
Jawab:
HttpResnponseRedirect() adalah salah satu fungsi dari django yang digunakan untuk mengarahkan user pada URL yang kita tentukan dan hanya menerima URL sebagai string. Sedangkan redirect() berfungsi adalah metode yang lebih fleksibel, mempermudah pengalihan dengan menerima nama view, objek, atau URL.

Jelaskan cara kerja penghubungan model Product dengan User!
Jawab:
Hubungan antara model Product dengan User dilakukan dengan menggunakan ForeignKey. Dalam metode ini, satu pengguna (user) bisa memiliki banyak produk, tetapi setiap produk hanya dimiliki oleh satu pengguna. Ini dikenal sebagai hubungan One-to-many (satu pengguna ke banyak produk).
Cara kerjanya:
1. Mengimpor User pada models.py 
2. Menambahkan "user = models.ForeignKey(User, on_delete=models.CASCADE)" untuk menunjukkan setiap produk dimiliki oleh user dan jika User dihapus, maka semya produk yang dimiliki oleh pengguna tersebut juga akan dihapus.
3. Memodifikasi fungsi pada create_product dalam views.py dan menambahkan commit=False untuk mencegah Django agar tidak langsung menyimpan objek yang telah dibuat dari form langsung ke database. Kemudian mengisi field user dengan objek User dari return value request.user yang sedang terotorisasi untuk menandakan bahwa objek tersebut dimiliki oleh pengguna yang sedang login.
4. Menambahkan request.user.username untuk menampilkan username pengguna yang login pada halaman main.

Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Jawab: 
Authentication atau otentikasi digunakan untuk memverifikasi identitas seorang user. Saat user mencoba login, sistem memastikan user tersebut cocok dengan data yang tersimpan di database, misalnya dengan memverifikasi nama user dan kata sandi.Jika nama user dan kata sandi sesuai, pengguna dianggap terotentikasi. Sedangkan authorization atau otorisasi digunakan untuk menentukan apa yang diizinkan dilakukan oleh user setalah mereka diotentikasi. Setelah user berhasil diotentikasi, sistem menentukan hak akses atau izin pengguna terhadap halaman web, fitur, atau data.

Secara umum, Django menggunakan authenticate() dan login() untuk memverifikasi pengguna. Pertama authenticate() berfungsi untuk memverifikasi apakah kredensial pengguna (misalnya, username dan password) benar. Jika benar, Django mengembalikan objek pengguna. Jika salah, akan mengembalikan None. Kemudian login() berfungsi untuk membuat session untuk pengguna setelah mereka berhasil diautentikasi. Sementara otorisasi diatur melalui permissions dan groups, yang diperiksa dengan has_perm() atau @permission_required decorator.

Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Jawab:
Django mengingat pengguna yang telah login dengan menggunakan session yang disimpan di cookies. Ketika pengguna berhasil login, Django membuat session untuk pengguna tersebut. Session ini bertindak seperti "penyimpanan sementara" yang menyimpan data penting tentang pengguna, termasuk apakah mereka sudah login atau belum. 

Selain untuk menyimpan session, cookies memiliki kegunaan lain seperti untuk menyimpan pengaturan/preferensi user, seperti bahasa pilihan, tema tampilan, ukuran teks, dll. Kemudian cookies sering digunakan untuk melacak aktivitas user di situs web. Dalam e-commerce cookies digunakan untuk menyimpan informasi keranjang belanja pengguna tanpa takut kehilangan item yang telah dipilih. 

Namun tidak semua cookies aman digunakan. Kita harus bijak untuk menyetujui cookies pada sebuah web, seperti penggunaan HTTPS/HttpOnly pada laman web, membatasi akses domain/path, menggunakan token CSRF untuk melindungi dari serangan CSRF, dan menggunakan cookie expire time.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab:
1. Membuat fungsi dan forum registrasi. Kita menggunakan UserCreationForm dari django.contrib.auth. Form ini mempermudah pembuatan akun pengguna dalam aplikasi web. Kita kemudian membuat fungsi registrasi untuk memproses formulir dan membuat akun baru saat formulir dikirim. Sebuah template HTML disediakan untuk menampilkan halaman pendaftaran, dan sistem pesan memberikan umpan balik kepada pengguna. Fungsi ini diimpor ke dalam views.py, dan rute URL untuk pendaftaran ditambahkan ke urlpatterns.
2. Membuat fungsi login. Kita membuat fungsi login menggunakan authenticate, login, dan AuthenticationForm untuk autentikasi pengguna. Fungsi login_user di views.py memverifikasi kredensial pengguna dan membuat session jika login berhasil. Template login.html dibuat untuk memungkinkan pengguna masuk ke aplikasi, dengan opsi pendaftaran bagi mereka yang belum memiliki akun.
3. Restriksi Akses. Kita menambahkan dekorator login_required untuk membatasi akses ke halaman utama (main). Ini memastikan hanya pengguna yang sudah login yang bisa mengakses halaman tersebut. Jika pengguna belum login, mereka akan diarahkan ke halaman login.
4. Menggunakan data dari Cookies. Kita menambahkan fungsionalitas last_login untuk menyimpan waktu login terakhir pengguna menggunakan cookie. Data ini ditampilkan di halaman utama, dan cookie tersebut dihapus saat pengguna logout. Fungsi ini diatur di views.py, dan informasi login terakhir pengguna ditampilkan sebagai pesan di halaman utama.
5. Melihat Cookies. Untuk melihat cookie di proyek, kita membuka halaman di localhost menggunakan Chrome, dan melalui Inspect di bagian Application, kami bisa melihat cookie yang disimpan.
6. Menghubungkan Product dengan User. Kita menambahkan relasi antara ProductEntry dan User di models.py dengan menggunakan ForeignKey. Setelah melakukan perubahan pada kode di views.py, termasuk menampilkan entri produk yang terkait dengan pengguna yang login, kami menyimpan semua perubahan dan melakukan migrasi database. Jika terjadi error, default value untuk field user akan diatur, dan proyek dijalankan dengan pengaturan DEBUG yang sudah dimodifikasi.

Bukti screenshot dua akun dengan tiga dummy data, beserta tampilan cookies:
1. sherwyn.fz
![alt text](<Tangkapan Layar 2024-09-24 pukul 23.09.43.png>)
2. sherwyn.fns
![alt text](<Tangkapan Layar 2024-09-24 pukul 23.09.04.png>)

-------------------------------------------------------------------------------------------

TUGAS INDIVIDU 5

Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Jawab:
CSS tentunya memiliki urutan prioritas yang menentukan gaya mana yang diterapkan pada elemen HTML ketika beberapa selector digunakan. Urutan prioritas CSS mengikuti aturan berikut:
1. Inline CSS: 
Gaya yang diterapkan langsung pada elemen HTML memiliki prioritas tertinggi (misalnya, <div style="color: red;">).
2. ID Selector: 
Selector berbasis ID (misalnya, #header) memiliki prioritas yang lebih tinggi dibandingkan dengan selector lainnya seperti class dan elemen.
3. Class Selector, Attribute Selector, dan Pseudo-Class: 
Class (.className), attribute selector ([type="text"]), dan pseudo-class (:hover, :active) memiliki prioritas yang lebih rendah dibandingkan ID selector, namun lebih tinggi dari elemen.
4. Tag Selector: Selector elemen atau tag HTML (div, p, h1, dll.) memiliki prioritas paling rendah.
5. Universal Selector (*) dan Inherited Style: Gaya yang diwarisi dari elemen parent atau universal selector memiliki prioritas terendah.

Ketika dua selector memiliki tingkat spesifisitas yang sama, urutan definisi dalam stylesheet akan menentukan mana yang diterapkan. Gaya yang didefinisikan terakhir akan menimpa gaya sebelumnya. Selain itu, gaya dengan !important akan selalu diutamakan, terlepas dari urutan atau spesifisitas.

Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Jawab:
Responsive design memastikan bahwa tampilan dan fungsi situs tetap optimal, terlepas dari ukuran layar yang berbeda dari masing-masing pengguna.Dengan adanya responsive design, pengguna mendapatkan pengalaman yang lebih baik tanpa harus memperbesar atau menggulir secara berlebihan. Hal ini dapat meningkatkan kepuasan dan keterlibatan pengguna. Dengan responsive design, situs web lebih mungkin mendapatkan peringkat yang lebih baik di hasil pencarian.

Contoh:
1. Sudah Menerapkan Responsive Design: YouTube dengan Layout video dan kontrol yang menyesuaikan dengan layar ponsel atau tablet.
2. Belum Menerapkan Responsive Design: Aplikasi mobile versi lama, seperti Tetris Classic yang didesain hanya untuk layar berukuran tetap dengan rasio yang spesifik (misalnya 4:3 atau 16:9).

Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Jawab:
1. Margin: Ruang antara elemen dengan elemen lain di luar elemen tersebut. Margin tidak memiliki warna atau isi dan hanya berupa ruang kosong di luar batas elemen.
2. Border: Garis yang mengelilingi elemen, terletak di antara margin dan padding. Border dapat diberi warna, lebar, dan gaya (misalnya solid, dotted).
3. Padding: Ruang di dalam elemen antara konten elemen dan border. Padding menambah ruang di dalam elemen tanpa mempengaruhi ukuran elemen itu sendiri secara eksternal.
4. Implementasi: 
.div-style {
  margin: 20px; /* Jarak dari elemen lain */
  border: 2px solid black; /* Garis tepi di sekitar elemen */
  padding: 15px; /* Ruang antara border dan konten di dalam elemen */
}

Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Jawab:
1. Flexbox: Flexbox (Flexible Box Layout) adalah modul CSS yang dirancang untuk menyusun elemen dalam satu dimensi (baik horizontal atau vertikal). Flexbox sangat berguna untuk mengatur layout dinamis, merespon ukuran kontainer, dan memusatkan elemen. Flexbox sering digunakan untuk tata letak yang memerlukan aliran konten seperti navbar atau tombol yang harus disusun di sepanjang satu baris atau kolom.
2. Grid Layout: Grid layout memungkinkan pengaturan elemen dalam dua dimensi, yaitu baris dan kolom. Grid sangat berguna untuk tata letak yang kompleks. Grid digunakan untuk layout yang lebih kompleks dan terstruktur seperti halaman majalah, dashboard, atau galeri gambar.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Jawab:
1. Implementasikan fungsi untuk menghapus dan mengedit product.
Pertama, kita menambahkan fungsi edit_product dan delate_product di views.py untuk memuat/menghapus data product berdasarkan id, menampilkan form, dan menyimpan perubahan. Kemudian menambahkan import reverse dan HttpsResponseRedirect. Selanjutnya membuat file edit_product.html dan delate_product.html, menambahkan route URL, dan memodifikasi main.html untuk menampilkan tombol edit dan delate .
2. Kustomisasi halaman login, register, dan tambah product semenarik mungkin.
Saya menggunakan framework TailwindCSS untuk membuat tampilan yang responsif dengan layout yang rapi. Form input diberi kelas CSS untuk mengontrol ukuran penuh di layar, dan menambahkan padding serta margin agar elemen terlihat lebih rapi dan profesional. Saya Menggunakan palet warna yang minimalis dan monokrom, seperti kombinasi abu-abu, putih yang akan memberikan kesan modern. Kemudian saya menggunakan shadow dan border-radius pada kotak input dan tombol untuk memberikan efek depth (kedalaman) yang membuat elemen UI lebih menarik. Tombol diberi efek hover untuk memberikan feedback visual kepada pengguna. Kemudian, menambahkan font bold untuk judul, ukuran teks yang lebih besar untuk elemen penting, serta penggunaan font sans-serif agar terlihat lebih modern dan jelas.
3. Kustomisasi halaman daftar product menjadi lebih menarik dan responsive.
Saya menggunakan CSS Grid atau Flexbox untuk membuat layout produk dalam bentuk grid yang fleksibel. Ini memungkinkan produk untuk diatur dalam kolom-kolom, dan akan menyesuaikan secara otomatis berdasarkan ukuran layar. Untuk setiap produk ditampilkan dalam card, dengan border radius, bayangan, dan warna latar belakang yang menarik. Elemen seperti gambar produk, nama produk, deskripsi, dan harga diletakkan di dalam card_product. Kemudian menyesuaikan jumlah kolom berdasarkan ukuran layar. Misalnya, 1 kolom untuk layar mobile, 2 kolom untuk tablet, dan 3 kolom atau lebih untuk layar yang lebih besar. Kemudian, menambahkan hover effect pada card produk, di mana ukuran atau bayangan card akan berubah saat pengguna mengarahkan kursor, memberikan pengalaman yang lebih interaktif.
4. Membuat dua buah button untuk mengedit dan menghapus product pada card product!
Tombol ditempatkan di dalam card di bagian bawah atau sudut kanan bawah, untuk mempermudah pengguna dalam mengakses fitur edit dan hapus. Tombol dibuat menggunakan warna yang sesuai dengan fungsinya. Misalnya, tombol Edit diberi warna netral atau warna aksen seperti abu-abu, sedangkan tombol Delete diberi warna merah untuk memperjelas bahwa itu adalah tombol untuk menghapus product.
5. Membuat navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop!
Navbar diletakkan di bagian atas halaman dengan tautan ke halaman-halaman utama yang berisi fitur Home, Produk, Categories, Cart, Welcome (user), serta Logout. Navbar dilengkapi dengan hamburger menu (ikon tiga garis) yang muncul di perangkat mobile. Saat ikon ini diklik, menu dropdown akan menampilkan tautan yang sama dengan versi desktop, tapi dalam bentuk yang lebih kompak.Saya menggunakan warna latar belakang yang gelap (misalnya indigo atau abu-abu gelap) dengan teks dan tautan berwarna terang (putih atau abu-abu cerah) seperti konsep monokrom yang saya inginkan. Shadow dan fixed position juga ditambahkan agar navbar selalu terlihat di bagian atas halaman saat pengguna menggulir. Kemudian menggunakan media queries agar desain navbar akan berubah pada berbagai ukuran layar. Pada layar kecil, elemen navbar ditumpuk secara vertikal di bawah tombol hamburger, sementara pada layar besar elemen-elemen tersebut ditampilkan secara horizontal.

Bukti screenshot tampilan login, register, main dengan product dan tanpa product, create product, dan edit product
1. Login
![alt text](<Tangkapan Layar 2024-10-02 pukul 04.41.46.png>)
2. Register
![alt text](<Tangkapan Layar 2024-10-02 pukul 04.41.46.png>)
3. Main dengan product
![alt text](<Tangkapan Layar 2024-10-02 pukul 04.42.10.png>)
4. Main tanpa product
![alt text](<Tangkapan Layar 2024-10-02 pukul 04.42.33.png>)
5. Create Product
![alt text](<Tangkapan Layar 2024-10-02 pukul 04.42.56.png>)
6. Edit Product
![alt text](<Tangkapan Layar 2024-10-02 pukul 04.43.07.png>)

-------------------------------------------------------------------------------------------

TUGAS INDIVIDU 6

Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
Jawab:
JavaScript biasanya dijalankan pada sisi klien (client-side JavaScript) dalam aplikasi web. Bahasa ini memungkinkan pembuatan halaman web yang interaktif dan responsif, di mana perubahan dapat dilakukan tanpa perlu memuat ulang halaman secara keseluruhan. Dengan JavaScript, elemen halaman bisa diperbarui secara dinamis. Selain itu, JavaScript mendukung fitur-fitur seperti lazy loading, animasi, serta elemen dinamis lainnya. JavaScript juga mengelola cookie dan penyimpanan lokal, yang memungkinkan aplikasi menyimpan informasi pengguna seperti preferensi atau status login. Pengguna juga bisa menyimpan data di penyimpanan lokal melalui LocalStorage atau SessionStorage, sehingga aplikasi bisa berjalan tanpa harus terus-menerus berkomunikasi dengan server.

Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Jawab:
Penggunaan await dalam fetch() membuat JavaScript menunggu hingga respons HTTP diterima dan diproses sebelum melanjutkan eksekusi kode. Jika await tidak digunakan, fungsi fetch() akan langsung mengembalikan objek promise, bukan hasil yang telah diproses. Tanpa await, kode akan terus berjalan dan mungkin mencoba memproses data yang belum tersedia, menyebabkan kesalahan atau hasil yang tidak diinginkan. Untuk menangani promise tanpa await, perlu menggunakan metode .then(), yang dapat membuat kode lebih rumit dan tidak sebersih pendekatan async/await.

Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
Jawab:
Decorator csrf_exempt digunakan untuk menonaktifkan pengecekan CSRF pada permintaan POST, seperti dalam AJAX POST. Hal ini diperlukan untuk menghindari kegagalan permintaan yang tidak menyertakan token CSRF, seperti pada fungsi add_product_entry_ajax.

Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Jawab:
Meskipun validasi di frontend penting untuk memberikan umpan balik cepat kepada pengguna, pembersihan dan validasi di backend juga diperlukan untuk alasan keamanan.Frontend bisa dimodifikasi oleh pengguna melalui alat seperti dev tools, yang memungkinkan mereka untuk melewati validasi atau memanipulasi input. Validasi di backend memastikan bahwa input yang tidak valid tidak diterima oleh server meskipun validasi frontend telah diubah atau dilewati. Backend dapat memberikan tingkat validasi dan sanitasi yang lebih mendalam, misalnya memeriksa integritas data, format yang benar, dan keamanan dari serangan seperti SQL Injection atau Cross-Site Scripting (XSS). Dengan melakukan pembersihan di backend, kita memastikan bahwa aplikasi akan bekerja sesuai yang diharapkan terlepas dari bagaimana input dimasukkan di frontend, menjaga keandalan dan prediktabilitas sistem. Oleh karena itu, validasi di frontend dan backend sama-sama penting. Frontend memberikan feedback langsung kepada pengguna, sedangkan backend memastikan keamanan dan integritas data.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Jawab:
1. Menambahkan eror message pada login, dimana akan menempelkan pesan eror kepada request yang mengirimkan permintaan login, yang nantinya akan ditempelkan di template login html.
2. Membuat function untuk menambahkan product dengan AJAX, yaitu dengan menambahkan import dan membuat fungsi baru di views.py dengan nama add_product_entry_ajax.
3. Menambahkan routing untuk fungsi add_product_entry_ajax, dengan membuka urls.py pada direktori main dan mengimpor fungsi yang sudah kita buat serta menambahkan path url ke urlpatterns untuk mengakses fungsi impor yang sudah diimpor tadi.
4. Menampilkan data Product Entry dengan fetch() API, yaitu dengan meghapus 2 baris pada file views.py dan mengubah baris pertama pada fungsi show_xml dan show_json. Kemudian membuka file main.html dan menghapus bagian block conditional product_entries untuk menampilkan card_product ketika kosong atau tidak. Kemudian membuat block script di bagian bawah file, yaitu sebelum {% endblock content %}. Kemudian memebuat fungsi baru pada block script dengan nama refreshProdEntries yang digunakan untuk me-refresh data moods secara asinkronus.
5. Membuat modal sebagai form untuk menambahkan mood. agar modal dapat berfungsi, kita perlu menambahkan fungsi-fungsi JavaScript.
6. Menambahkan data Product dengan AJAX. dimana modal dengan form yang telah kita buat tadi digunakan untuk menambhakan data product. sehingga kita perlu membuat fungsi JavaScript, kemudian tambahin sebuah event listener pada form di modal untuk menjalankan fungsi addProduct().
7. Melindungi aplikasi dari cross site scripting(XSS), yaitu dengan menambahkan data product baru dengan nilai field. Field lain dapat diisi sesuai dengan keinginan kita lalu tekan tombol simpan dan jika penyimpanan berhasil maka kita akan mendapatkan pesan alert dengan nilai xss. Kemudian kita menambahkan strips_tags untuk memebersihkan data baru  dengan membuka berkas views.py dan menambahkan import strip_tags dan pada fungsi add_product_ajax kita gunakan fungsi strip_tags pada data product. Kemudian kita menambahkan strips_tags dan hapus data product yang tadi kita tambahin, membersihkan data dengan DOMPurify dengan membuka main.html
8. Me-refresh halaman utama kita dan alert box tidak akan muncul lagi di browser kita.