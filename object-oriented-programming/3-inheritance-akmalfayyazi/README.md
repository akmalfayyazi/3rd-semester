[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/xFfvg0uT)
# oop-inheritance-python

## Capaian Pembelajaran

1. Mahasiswa mampu mendeklarasikan relasi pewarisan (inheritance).
2. Mahasiswa mampu menggunakan *convention* `protected` di Python (nama atribut diawali `_`).
3. Mahasiswa mampu menggunakan kembali metode dan atribut dari kelas induk di kelas turunan.

---

## Lingkungan Pengembangan

1. Platform: Python 3.10+
2. Bahasa: Python
3. Editor/IDE yang disarankan:
   - VS Code + Python Extension
   - Terminal

---

## Cara Menjalankan Project

1. Clone repositori project `oop-inheritance-python` ke direktori lokal Anda:
   ```bash
   git clone https://github.com/USERNAME/oop-inheritance-python.git
   cd oop-inheritance-python
   ```

2. Buat dan aktifkan virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate        # Linux/macOS
   .venv\Scripts\activate           # Windows
   ```

3. Install dependensi:

   ```bash
   pip install -r requirements.txt
   ```

4. Jalankan unit test:

   ```bash
   pytest
   ```

> PERINGATAN: Lakukan push ke remote repository hanya jika seluruh unit test telah berhasil dijalankan (semua hijau).

---

## Soal-soal

> Catatan umum:
>
> * “Atribut `protected`” di Python menggunakan **konvensi** nama awalan `_` (mis. `_merk`). Ini bukan proteksi ketat, tetapi panduan enkapsulasi.
> * “Properti hanya GET” berarti sediakan `@property` (tanpa setter publik).
> * Untuk demonstrasi, gunakan blok:
>
>   ```python
>   if __name__ == "__main__":
>       # demo
>   ```
> * Gunakan **snake_case** untuk atribut/metode, **PascalCase** untuk nama kelas.

---

### 1) BookVehicle (Buku)

**Lokasi:** `src/books/buku.py`

**Spesifikasi:**

* Buat kelas `Buku` dengan atribut **protected** `_judul: str`, `_pengarang: str`.
* Konstruktor menginisialisasi kedua atribut.
* Sediakan properti publik `judul` dan `pengarang` (getter & setter).

Dari `Buku`, turunkan:

* `BukuFiksi` dengan atribut **protected** tambahan `_genre: str` (contoh: "Fantasi", "Horor", dll.).

  * Properti publik `genre` (getter & setter).
* `BukuPelajaran` dengan atribut **protected** tambahan `_subjek: str` (contoh: "Matematika", "Biologi", dll.).

  * Properti publik `subjek` (getter & setter).

**Demo:** Instansiasi 1 `BukuFiksi` dan 1 `BukuPelajaran`, set properti melalui konstruktor (dan/atau setter), lalu **cetak** informasi keduanya (judul, pengarang, dan atribut tambahannya).

---

### 2) Vehicles (Kendaraan)

**Lokasi:** `src/vehicles/kendaraan.py`

**Spesifikasi:**

* Buat kelas `Kendaraan` dengan atribut **protected** `_merk: str`, `_model: str`.
* Konstruktor menginisialisasi kedua atribut.
* Sediakan properti publik **hanya GET**: `merk`, `model`.

Dari `Kendaraan`, turunkan:

* `Mobil` dengan atribut **protected** tambahan `_tipe_bodi: str` (contoh: "Sedan", "SUV").

  * Properti publik **hanya GET** `tipe_bodi`.
* `Motor` dengan atribut **protected** tambahan `_tipe_mesin: str` (contoh: "2 Stroke", "4 Stroke").

  * Properti publik **hanya GET** `tipe_mesin`.

**Demo:** Instansiasi 1 `Mobil` dan 1 `Motor` melalui konstruktor (karena properti **GET-only**), lalu **cetak** informasi keduanya.

---

### 3) ElectronicDevices (Perangkat Elektronik)

**Lokasi:** `src/electronics/perangkat_elektronik.py`

**Spesifikasi:**

* Buat kelas `PerangkatElektronik` dengan atribut **protected** `_brand: str`, `_model: str`.
* Konstruktor menginisialisasi kedua atribut.
* Properti publik **hanya GET**: `brand`, `model`.
* Metode publik `tampilkan_identitas(self)` mencetak:

  ```
  Perangkat Brand: {brand}, Model: {model}
  ```

Turunan:

* `Smartphone` (turun dari `PerangkatElektronik`) dengan atribut **protected**:

  * `_sistem_operasi: str` (mis. "Android", "iOS")
  * `_fitur_dasar: str`
  * Properti publik **GET-only**: `sistem_operasi`, `fitur_dasar`
  * Metode `tampilkan_fitur_dasar(self)` mencetak:

    ```
    Fitur Dasar: {fitur_dasar}
    ```
* `FlagshipPhone` (turun dari `Smartphone`) dengan atribut **protected** tambahan `_fitur_premium: str`.

  * Properti publik **GET-only**: `fitur_premium`
  * Metode `tampilkan_fitur_premium(self)` yang:

    1. Memanggil `tampilkan_fitur_dasar()` (dari induknya) untuk mencetak fitur dasar,
    2. Lalu mencetak **baris terpisah**:

       ```
       Fitur Premium: {fitur_premium}
       ```
* `BudgetPhone` (turun dari `Smartphone`) dengan atribut **protected** tambahan `_harga: int`.

  * Properti publik **GET-only**: `harga`.

**Demo:** Instansiasi 1 `FlagshipPhone` dan 1 `BudgetPhone`, panggil `tampilkan_identitas()`, `tampilkan_fitur_dasar()`, dan khusus `FlagshipPhone` panggil juga `tampilkan_fitur_premium()`; cetak informasi `harga` untuk `BudgetPhone`.

> Catatan kecil: di teks asli ada salah ketik “Samrtphone”; gunakan `Smartphone`.

---

### 4) SportsEquipment (Peralatan Olahraga)

**Lokasi:** `src/sports/peralatan_olahraga.py`

**Spesifikasi:**

* Kelas `PeralatanOlahraga` dengan atribut **protected** `_jenis: str`, `_merek: str`.
* Konstruktor menginisialisasi kedua atribut.
* Properti publik **GET-only**: `jenis`, `merek`.
* Metode `tampilkan_informasi(self)` mencetak:

  ```
  Peralatan Olahraga Jenis: {jenis}, Merek: {merek}
  ```

Turunan:

* `Bola` (turun dari `PeralatanOlahraga`) dengan atribut **protected**:

  * `_jenis_olahraga: str` (mis. "Sepakbola", "Basket")
  * `_bahan: str`
  * Properti **GET-only**: `jenis_olahraga`, `bahan`
  * Metode `tampilkan_spesifikasi(self)` mencetak:

    ```
    Jenis Olahraga: {jenis_olahraga}, Bahan: {bahan}
    ```
* `BolaProfesional` (turun dari `Bola`) dengan atribut **protected** `_standar_internasional: bool`.

  * Properti **GET-only**: `standar_internasional`
  * Metode `tampilkan_standar(self)` yang mencetak **satu baris** gabungan:

    ```
    Jenis Olahraga: {jenis_olahraga}, Bahan: {bahan}, Standar Internasional: {Ya/Tidak}
    ```

    (Gunakan “Ya” jika `True`, “Tidak” jika `False`.)
* `BolaLatihan` (turun dari `Bola`) dengan atribut **protected** `_harga: int`.

  * Properti **GET-only**: `harga`.

**Demo:** Instansiasi 1 `BolaProfesional` dan 1 `BolaLatihan`, panggil `tampilkan_informasi()`, `tampilkan_spesifikasi()`, `tampilkan_standar()` (untuk profesional), dan **cetak** harga (untuk latihan).

---

### 5) Extra

**Lokasi:** `src/extra/extra.py`

Buat soal dan solusi Anda sendiri yang mencakup:

* Nama kelas dan kegunaannya serta hirarki turunannya.
* Atribut/properti yang harus ada.
* Metode yang dibutuhkan.
* Validasi/aturan khusus.

Tambahkan blok demo `if __name__ == "__main__":` untuk menjalankan contoh.

---

=== SELESAI ===