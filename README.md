##### Nama: Taniella 
##### NPM: 2206082316

# **TUGAS 4**
### **1.** Apa itu Django ```UserCreationForm```, dan jelaskan apa kelebihan dan kekurangannya?

```UserCreationForm``` merupakan sistem autentikasi pengguna milik Django yang digunakan untuk melakukan registrasi terhadap pengguna-pengguna baru ke dalam sistem situs web. Sistem ini menyimpan data pengguna yang telah melakukan registrasi ke dalam database dan juga dapat melakukan validasi terhadap username dan password yang di-input oleh pengguna.

- Kelebihan
UserCreationForm memungkinkan pembuatan formulir registrasi yang lengkap dengan cepat, mengintegrasikan berbagai fitur yang umumnya dibutuhkan dalam proses registrasi. Selain itu, sistem ini juga mengatasi keamanan kata sandi dengan mengukur tingkat kekuatan kata sandi dan otomatis melakukan proses hashing untuk meningkatkan keamanan.

- Kekurangan
UserCreationForm hanya menyediakan bidang (fields) standar seperti username, kata sandi, alamat email, nama depan, dan nama belakang. Untuk menambahkan fitur tambahan seperti gambar profil atau deskripsi, perlu dilakukan penyesuaian secara manual. Form ini juga memiliki keterbatasan dalam menangani validasi yang lebih kompleks, sehingga mungkin memerlukan modifikasi atau pembuatan formulir tambahan secara manual. Selain itu, untuk meningkatkan keamanan registrasi, seperti verifikasi email, pengembang perlu mengimplementasikannya secara terpisah karena tidak disediakan oleh UserCreationForm.

### **2.** Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

Dalam konteks Django, autentikasi dan otorisasi adalah dua konsep penting. Autentikasi adalah proses verifikasi identitas pengguna yang mencoba mengakses aplikasi, sementara otorisasi mengendalikan hak akses pengguna dalam aplikasi. Autentikasi memastikan bahwa hanya pengguna yang sah yang dapat masuk, sedangkan otorisasi menentukan apa yang dapat dilakukan oleh pengguna yang telah diotentikasi. Keduanya bekerja bersama untuk memberikan pengalaman pengguna yang aman dan terstruktur, melindungi data sensitif, dan mengatur tindakan yang diizinkan dalam aplikasi web.

### **3.** Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

Cookies dalam konteks aplikasi web adalah data kecil yang disimpan pada perangkat pengguna oleh server web untuk berbagai tujuan, termasuk pengelolaan data sesi pengguna. Django menggunakan cookies untuk mengidentifikasi pengguna dan menyimpan data sesi mereka. Django menghasilkan *session id* untuk pengguna yang disimpan dalam cookie, yang digunakan untuk mengambil dan menyimpan data sesi seperti preferensi pengguna dan informasi login. Meskipun secara default isi sesi disimpan dalam database, Django memungkinkan konfigurasi untuk penyimpanan di lokasi lain sesuai kebutuhan.

### **4.** Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Penggunaan cookies dalam pengembangan web dapat menjadi aman jika diterapkan dengan benar, namun juga membawa potensi risiko yang harus diwaspadai. Cookies adalah alat yang berguna untuk menyimpan informasi di sisi klien dan menjaga keadaan sesi pengguna. Namun, risiko keamanan privasi menjadi perhatian utama, karena cookies dapat menyimpan data sensitif yang rentan terhadap pencurian jika tidak dienkripsi atau diatur dengan baik. Risiko Man-in-the-Middle (MitM) dan serangan Cross-Site Request Forgery (CSRF) juga harus dihadapi, serta perlu perhatian terhadap keamanan transport layer dengan selalu menggunakan HTTPS.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. membuat fungsi registrasi, login, logout, pada views.py
2. melakukan import untuk kepentingan fungsi tersebut
3. membuat html untuk register dan login, serta membuat validasi
4. membuat 2 akun pengguna dan mengisi dummy data
5. menyambungkan item dengan user sehingga item akun A tidak diakses akun B
6. menampilkan detail login seperti cookies
7. mengerjakan bonus, namun tidak increment atau decrement melainkan edit langsung data.

---
# **TUGAS 3**
### **1.** Apa perbedaan antara form POST dan GET dalam Django?

```POST``` mencakup semua request yang bisa menambahkan, menghapus, atau merubah keadaan server, seperti penambahan data baru pada server. Sedangkan ```GET```  sendiri merupakan command untuk mengambil dan menerima data baru dan tidak mengubah server dalam hal apapun.

### **2.** Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

**HTML** merupakan cara untuk menampilkan data melalui format penulisan yang sudah dibuat pada web. **XML** dan **JSON** sendiri merupakan tempat untuk penyimpanan data agar dapat diakses degnan mudah dan juga merupakan salah satu bentuk data yang diterima untuk penampilan **HTML**.

Perbedaan dari **XML** dan **JSON** sendiri adalah bagaimana data tersebut disimpan, pada **JSON** data disimpan dalam bentuk seperti dictionary, dengan key dan value, namun **XML** menampilkan datanya seperti pohon.

### **3.** Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

**JSON** sendiri merupakan bahasa yang irngkas dan mudah dibaca, struktur datanya yang fleksibel juga membuat **JSON** banyak diminati. Selain itu **JSON** juga menggunakan struktur array yang membuat transmisi data lebih cepat dan mudah dibaca dibandingkan dengan **XML**

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Pertama-tama saya membuat *skeleton* untuk menjadi base objek model.
2. Membuat data input form untuk menambahkan item pada database
3. Membuat 5 cara viewing, HTML, XML, XML by id, JSON, dan JSON by id
4. Menambahkan routing pada masing-masing views.
5. Memastikan tampilan berjalan dengan bendar dan melakukan beberapa pembetulan untuk data type dan views

### Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
#### HTML
![Alt text](images\2html.png)
#### XML
![Alt text](images\2xml.png)
#### XML by id
![Alt text](images\2xmlid.png)
#### JSON
![Alt text](images\2json.png)
#### JSON by id
![Alt text](images\2jsonid.png)

---
# **TUGAS 2**
>Link Adaptable: https://florist.adaptable.app/main

### **1.** Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Pertama-tama membuat repository baru dan membuat path local dan menyambungkannya pada repository yang sudah dibuat. 
- Membuat virtual environment sebelum membuat project, menginstall semua requirements yang dibutuhkan lalu membuat Django project bernama florist [dengan command: django-admin startproject florist .]
- Lalu membuat app main dalam project dengan command: [python manage.py startapp main] yang akan membuat path main dalam path florist. Jangan lupa memasukan 'main' ke dalam INSTALLED_APPS pada settings.py
- Setelah itu melakukan routing dengan memasukan path main pada url patterns di urls.py pada path florist.
- Lalu mulai mengisi models dan views juga membuat template htmlnya untuk menampilkan datanya.
- Melakukan deployment ke Adaptable.



### **2.** Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
 ![mvt](images\1mvt.png) 
- urls.py menentukan views.py dan models.py yang akan di akses untuk tampilan dari berkas html yang dijadikan response ke user.



### **3.** Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
- Dalam penggunaan Virtual Environment, kita akan lebih mudah dalam mengerjakan dengan mengisolasi proyek sehingga tidak tercampur dengan proyek-proyek lainnya. Hal ini memastikan versi yang digunakan dari tiap pustaka merupakan versi yang konsisten dan tidak berubah-ubah walau proyek dikerjakan di device yang berbeda dalam tahapan pengembangan.

- Secara teori tentunya kita bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual env namun hal itu akan memiliki resiko konflik dependensi dan mempersulit kolaborasi antar tim yang tidak dapat memastikan versi yang digunakan untuk tetap konstan.



#### **4.** Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
- MVC atau Model-View-Controller adalah pola desain yang memisahkan aplikasi menjadi 3 bagian, Model untuk data dan logika, View untuk presentasi, dan Controller untuk pengendalian logika.

- MVT atau Model-View-Template adalah pola desain seperti MVC yang dikemas dalam kerangka web Django, perbedaannya hanya dalam Controller yang diganti menjadi Template dan digunakan untuk pengaturan tampilan web

- MVVM atau Model-View-ViewModel merupakan basis yang digunakan untuk pengembangan aplikasi yang lebih kompleks seperti aplikasi mobile dan desktop modern, perbedaannya berada pada ViewModel yang merupakan konsep unik untuk MVVM yang merupakan perantara antara Model dan View yang mengkonversi data dari Model untuk menjadi format yang dapat ditampilkan oleh view. 