Nama: A. Sherwyn Fawwaz Nitisara Suthaputra
NPM: 2306165811
Kelas : PBP F


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
Data delivery penting dalam pengembangan platform karena memastikan informasi yang disimpan di server atau database pusat dapat diakses oleh pengguna dari berbagai lokasi. Dengan data delivery, platform dapat berkomunikasi dan terintegrasi dengan layanan lain seperti API eksternal, memungkinkan data untuk dikirim dan diterima dalam format yang sesuai. Hal ini mendukung kolaborasi dan interaksi efisien antar sistem, serta memastikan komunikasi data antara berbagai komponen platform berjalan dengan lancar, memfasilitasi akses dan pemrosesan informasi yang tepat.

Mana yang Lebih Baik: XML atau JSON? Mengapa JSON Lebih Populer?
JSON lebih populer dibandingkan XML karena memiliki format yang lebih sederhana dan mudah dibaca. JSON menggunakan {} untuk merepresentasikan objek dan array, sementara XML menggunakan tag <tag>...</tag> untuk setiap elemen, membuatnya lebih panjang dan sulit dibaca. XML cocok untuk dokumen yang membutuhkan struktur kompleks dan detil, sedangkan JSON lebih sering digunakan untuk aplikasi yang membutuhkan komunikasi data cepat dan efisien.

Jelaskan fungsi dari method is_valid() pada Form Django dan Pentingnya
Method is_valid() pada form Django digunakan untuk memvalidasi data input yang dimasukkan ke dalam form, memastikan data tersebut sesuai dengan aturan yang telah ditentukan (misalnya tipe data, panjang maksimal, atau format yang benar). Jika data valid, method ini mengembalikan nilai True, dan jika tidak valid, mengembalikan False. Method ini penting untuk mencegah data yang tidak sesuai masuk ke dalam sistem.

Mengapa csrf_token Diperlukan di Form Django dan Apa Risikonya Tanpa CSRF?
csrf_token digunakan dalam form Django untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery), di mana penyerang mencoba memanipulasi pengguna agar melakukan tindakan yang tidak diinginkan. Dengan menambahkan csrf_token dalam form, aplikasi dapat memverifikasi bahwa permintaan berasal dari sumber yang sah. Jika tidak menambahkan csrf_token, penyerang bisa mengeksploitasi sesi pengguna yang sudah login untuk melakukan tindakan yang merugikan, seperti mengubah pengaturan akun atau mencuri data pribadi tanpa persetujuan pengguna. Tanpa CSRF token, aplikasi dapat memproses permintaan palsu yang tampak seperti berasal dari pengguna yang sah.

Langkah-langkah Implementasi Checklist pada Django
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
