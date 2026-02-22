[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Xo1KpgUr)
# oop-composition-python

## Capaian Pembelajaran

1. Mahasiswa mampu memodelkan **komposisi** dengan atribut bertipe objek (non-primitif).
2. Mahasiswa mampu **menggunakan kembali** fungsionalitas objek lain melalui komposisi.

---

## Lingkungan Pengembangan

1. Platform: Python 3.10+
2. Bahasa: Python
3. Editor/IDE yang disarankan:
   - VS Code + Python Extension
   - Terminal

---

## Cara Menjalankan Project

1. Clone repositori project `oop-composition-python` ke direktori lokal Anda:
   ```bash
   git clone https://github.com/USERNAME/oop-composition-python.git
   cd oop-composition-python
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

### 1) Komputer dan Komponennya

**Lokasi:** `src/computers/`

* Buat kelas `Processor` pada `src/computers/processor.py` dengan atribut privat `_brand: str`, `_speed: float` (GHz).

  * Sediakan properti `brand` dan `speed` (getter & setter).
* Buat kelas `Memory` pada `src/computers/memory.py` dengan atribut privat `_capacity: int` (GB), `_memory_type: str` (mis. `"DDR4"`, `"DDR5"`).

  * Sediakan properti `capacity` dan `memory_type` (getter & setter).
* Buat kelas `Computer` pada `src/computers/computer.py` dengan **komposisi**:

  * Atribut privat `_processor: Processor`, `_memory: Memory`.
  * Konstruktor menerima objek `Processor` dan `Memory`.
  * Properti `processor` dan `memory` (getter & setter).
  * Metode `get_info(self) -> str` yang **mengembalikan string**:

    ```
    Processor Brand: {brand}, Kecepatan: {speed}, Memory Kapasitas: {capacity}, Tipe: {memory_type}
    ```
* Tambahkan blok demo:

  ```python
  if __name__ == "__main__":
      # buat Processor, Memory, rakit ke Computer, cetak get_info()
  ```

---

### 2) Toko Buku

**Lokasi:** `src/bookstore/`

* Buat kelas `Buku` pada `src/bookstore/buku.py` dengan atribut privat `_isbn: str`, `_judul: str`, `_harga: float`.

  * Konstruktor menginisialisasi semua atribut.
  * Properti **getter-only**: `isbn`, `judul`, `harga`.
  * Metode:

    * `is_isbn_match(self, isbn: str) -> bool` → `True` jika cocok.
    * `get_info(self) -> str` → `"ISBN: {isbn}, Judul: {judul}, Harga: {harga}"`.
* Buat kelas `TokoBuku` pada `src/bookstore/toko_buku.py` dengan **komposisi** daftar buku:

  * Atribut privat `_daftar_buku: list[Buku]` (mulai dari list kosong).
  * Properti `daftar_buku(self, value: list[Buku])` **setter-only** untuk mengganti daftar sekaligus (opsional; tetap sediakan akses lewat metode di bawah).
  * Metode:

    * `tambah_buku(self, buku: Buku) -> None`
    * `hapus_buku(self, isbn: str) -> None` (hapus buku dengan ISBN cocok)
    * `cari_buku(self, isbn: str) -> Buku | None` (gunakan `is_isbn_match`)
    * `get_daftar_buku(self) -> list[str]` (kembalikan **list string** hasil `get_info()` dari tiap `Buku`)
* Demo:

  ```python
  if __name__ == "__main__":
      # buat TokoBuku, tambah/hapus buku, tampilkan hasil get_daftar_buku()
  ```

---

### 3) Toko Elektronik

**Lokasi:** `src/electronic_store/`

* Kelas `Produk` di `src/electronic_store/produk.py`:

  * Atribut privat `_nama: str`, `_harga: float`; properti `nama`, `harga` (getter & setter).
* Kelas `ItemBelanja` di `src/electronic_store/item_belanja.py` **(komposisi Produk)**:

  * Atribut privat `_produk: Produk`, `_kuantitas: int`
  * Properti `produk` (getter & setter), `kuantitas` (getter & setter; minimal 0 → jika <0 set 0).
  * Metode `hitung_total(self) -> float` → `produk.harga * kuantitas`.
* Kelas `KeranjangBelanja` di `src/electronic_store/keranjang_belanja.py` **(komposisi ItemBelanja)**:

  * Atribut privat `_items: list[ItemBelanja]` (mulai kosong)
  * Properti **getter-only** `items` → mengembalikan list item (read-only view; jangan return salinan mendalam).
  * Metode:

    * `tambah_item_belanja(self, produk: Produk, kuantitas: int) -> None` (buat `ItemBelanja` dan tambahkan)
    * `hitung_total_belanja(self) -> float` → jumlah `hitung_total()` semua item
* Demo:

  ```python
  if __name__ == "__main__":
      # buat KeranjangBelanja, tambah beberapa produk, cetak total belanja
  ```

---

### 4) Extra

**Lokasi:** `src/extra/extra.py`
Buat soal dan implementasi **buatan sendiri** yang memanfaatkan komposisi (kelas A memiliki objek dari kelas B/C, dan memanggil fungsionalitasnya). Spesifikasi minimal:

* Nama kelas dan kegunaannya.
* Atribut komposisi & properti yang ada.
* Metode yang dibutuhkan.
* Validasi/aturan khusus.
* Menunjukkan **penggunaan kembali** fungsionalitas objek lain melalui komposisi.

Tambahkan blok demo `if __name__ == "__main__":`.

---

=== Selesai ===