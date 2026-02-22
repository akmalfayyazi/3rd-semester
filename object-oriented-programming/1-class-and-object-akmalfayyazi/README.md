[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/axAelSnu)
# oop-class-and-object-python

## Capaian Pembelajaran

1. Mahasiswa mampu mendeklarasikan kelas yang berisi atribut dan metode sesuai spesifikasi.
2. Mahasiswa mampu menginstansiasi kelas menjadi objek dan mengoperasikan metode-metode di objek tersebut.

---

## Lingkungan Pengembangan

1. Platform: Python 3.10+
2. Bahasa: Python
3. Editor/IDE yang disarankan:
   - VS Code + Python Extension
   - Terminal

---

## Cara Menjalankan Project

1. Clone repositori project `oop-class-and-object-python` ke direktori lokal Anda (sesuaikan nama repositorinya):
   ```bash
   git clone https://github.com/USERNAME/oop-class-and-object-python.git
   cd oop-class-and-object-python
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

### 1. Buku

Implementasikan solusi di file `src/library/buku.py`.

Buatlah kelas bernama `Buku` yang merepresentasikan informasi tentang buku. Kelas ini memiliki tiga atribut:

* `judul` (string)
* `penulis` (string)
* `tahun_terbit` (int)

Buat konstruktor `__init__` untuk menginisialisasi atribut-atribut tersebut.

Tambahkan metode `tampilkan_info(self)` yang mencetak:

```
Judul: [judul], Penulis: [penulis], Tahun Terbit: [tahun_terbit]
```

Tambahkan blok eksekusi `if __name__ == "__main__":` untuk membuat objek `Buku` dan menampilkan informasinya.

---

### 2. Mobil

Implementasikan solusi di file `src/auto/mobil.py`.

Buatlah kelas bernama `Mobil` dengan atribut:

* `merk` (string)
* `model` (string)
* `tahun_produksi` (int)

Buat konstruktor `__init__` untuk menginisialisasi atribut-atribut tersebut.

Tambahkan metode `tampilkan_spesifikasi(self)` yang mencetak:

```
Merk: [merk], Model: [model], Tahun Produksi: [tahun_produksi]
```

Tambahkan blok eksekusi `if __name__ == "__main__":` untuk membuat objek `Mobil` dan menampilkan spesifikasinya.

---

### 3. Laptop

Implementasikan solusi di file `src/electronic/laptop.py`.

Buatlah kelas bernama `Laptop` dengan atribut:

* `merk` (string)
* `prosesor` (string)
* `ram` (int, dalam GB)
* `penyimpanan` (int, dalam GB)

Buat konstruktor `__init__` untuk menginisialisasi atribut-atribut tersebut.

Tambahkan metode `tampilkan_spesifikasi(self)` yang mencetak:

```
Merk: [merk], Prosesor: [prosesor], RAM: [ram] GB, Penyimpanan: [penyimpanan] GB
```

Tambahkan blok eksekusi `if __name__ == "__main__":` untuk membuat objek `Laptop` dan menampilkan spesifikasinya.

---

### 4. Sepeda

Implementasikan solusi di file `src/bicycle/sepeda.py`.

Buatlah kelas bernama `Sepeda` dengan atribut:

* `merk` (string)
* `tipe` (string)
* `berat` (float, dalam kg)

Buat konstruktor `__init__` untuk menginisialisasi atribut-atribut tersebut.

Tambahkan metode `tampilkan_informasi(self)` yang mencetak:

```
Merek: [merk], Tipe: [tipe], Berat: [berat] kg
```

Tambahkan blok eksekusi `if __name__ == "__main__":` untuk membuat objek `Sepeda` dan menampilkan informasinya.

---

### 5. Kalkulator

Implementasikan solusi di file `src/calc/kalkulator.py`.

Buatlah kelas bernama `Kalkulator` yang memiliki empat metode:

* `tambah(self, a: float, b: float) -> float`
* `kurang(self, a: float, b: float) -> float`
* `kali(self, a: float, b: float) -> float`
* `bagi(self, a: float, b: float) -> float` (pastikan menangani pembagi nol).

Tambahkan blok eksekusi `if __name__ == "__main__":` untuk membuat objek `Kalkulator`, melakukan beberapa operasi (penjumlahan, pengurangan, perkalian, pembagian), dan mencetak hasilnya.

=== Selesai ===