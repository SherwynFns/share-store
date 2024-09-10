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