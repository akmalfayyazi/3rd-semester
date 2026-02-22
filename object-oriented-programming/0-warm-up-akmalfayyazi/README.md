[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/6N0kfd5e)
# oop-warmup-python

## Capaian Pembelajaran

1. Mahasiswa mampu menggunakan Git untuk mengerjakan soal-soal yang diberikan secara kolaboratif dan terdokumentasi.
2. Mahasiswa mampu menulis kode Python dengan pendekatan Pemrograman Berorientasi Objek (OOP).
3. Mahasiswa mampu menulis dan menjalankan unit test untuk memvalidasi solusi.
4. Mahasiswa mampu memanfaatkan integrasi CI/CD sederhana melalui GitHub Actions.

---

## Lingkungan Pengembangan

1. Platform: Python 3.10+
2. Bahasa: Python
3. Editor/IDE yang disarankan:
   - VS Code + Python Extension
   - Terminal

---

## Cara Menjalankan Project

1. Clone repositori project `oop-warmup-python` ke direktori lokal Anda:
   ```bash
   git clone https://github.com/USERNAME/oop-warmup-python.git
   cd oop-warmup-python
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

## Soal: Kalkulator Sederhana dengan OOP di Python

Buatlah solusi dari soal ini di dalam folder `src/calc/`.

Anda diminta untuk membuat aplikasi kalkulator sederhana yang mampu melakukan operasi dasar seperti penjumlahan, pengurangan, perkalian, dan pembagian.

---

## Langkah-langkah

1. **Kelas Calculator**
   Buat kelas `Calculator` di file `src/calc/calculator.py` yang menyediakan method:

   * `tambah(a, b)`
   * `kurang(a, b)`
   * `kali(a, b)`
   * `bagi(a, b)` → jika `b == 0`, tampilkan pesan kesalahan dan kembalikan `NaN`.

2. **Metode Helper**
   Tambahkan method privat `__tampilkan_hasil(operasi, hasil)` untuk mencetak hasil operasi.

3. **Program Utama**
   Buat `main.py` di dalam `src/calc/` yang membaca input dari pengguna dan memanggil method kalkulator yang sesuai.

4. **Program berjalan hingga pengguna mengetik `exit`**
   Jika operasi tidak valid, tampilkan pesan kesalahan.

---

## Contoh Output

```
Masukkan angka pertama: 5
Masukkan angka kedua: 3
Pilih operasi (Tambah, Kurang, Kali, Bagi): Tambah
Hasil operasi Penjumlahan: 8
Ketik 'exit' untuk keluar, atau tekan Enter untuk melanjutkan:

Masukkan angka pertama: 10
Masukkan angka kedua: 0
Pilih operasi (Tambah, Kurang, Kali, Bagi): Bagi
Kesalahan: Pembagian dengan nol tidak diperbolehkan.
```

---

## Struktur Project

```
oop-warmup-python/
├── src/
│   └── calc/
│       ├── __init__.py
│       ├── calculator.py
│       └── main.py
├── tests/
│   └── test_calculator.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Implementasi Kode

### 1. `src/calc/calculator.py`

```python
class Calculator:
    def __tampilkan_hasil(self, operasi: str, hasil: float) -> None:
        print(f"Hasil operasi {operasi}: {hasil}")

    def tambah(self, a: float, b: float) -> float:
        hasil = a + b
        self.__tampilkan_hasil("Penjumlahan", hasil)
        return hasil

    def kurang(self, a: float, b: float) -> float:
        hasil = a - b
        self.__tampilkan_hasil("Pengurangan", hasil)
        return hasil

    def kali(self, a: float, b: float) -> float:
        hasil = a * b
        self.__tampilkan_hasil("Perkalian", hasil)
        return hasil

    def bagi(self, a: float, b: float) -> float:
        if b == 0:
            print("Kesalahan: Pembagian dengan nol tidak diperbolehkan.")
            return float('nan')
        hasil = a / b
        self.__tampilkan_hasil("Pembagian", hasil)
        return hasil
```

---

### 2. `src/calc/main.py`

```python
from calculator import Calculator

def main():
    calc = Calculator()
    while True:
        try:
            a_input = input("Masukkan angka pertama: ")
            if a_input.lower() == "exit":
                break
            a = float(a_input)

            b_input = input("Masukkan angka kedua: ")
            if b_input.lower() == "exit":
                break
            b = float(b_input)

            operasi = input("Pilih operasi (Tambah, Kurang, Kali, Bagi): ").strip().lower()
            if operasi == "exit":
                break

            if operasi == "tambah":
                calc.tambah(a, b)
            elif operasi == "kurang":
                calc.kurang(a, b)
            elif operasi == "kali":
                calc.kali(a, b)
            elif operasi == "bagi":
                calc.bagi(a, b)
            else:
                print("Operasi tidak valid. Silakan pilih Tambah, Kurang, Kali, atau Bagi.")

        except ValueError:
            print("Input tidak valid. Pastikan Anda memasukkan angka.")

        lanjut = input("Ketik 'exit' untuk keluar, atau tekan Enter untuk melanjutkan: ").strip().lower()
        if lanjut == "exit":
            break

if __name__ == "__main__":
    main()
```

---