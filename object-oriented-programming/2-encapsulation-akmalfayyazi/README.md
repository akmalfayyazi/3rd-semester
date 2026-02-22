[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/RUSzDLFr)
# oop-encapsulation-python

## Capaian Pembelajaran

1. Mahasiswa mampu menyembunyikan atau mengekspos atribut menggunakan konvensi Python (`_atribut` untuk private, `property` untuk getter/setter).
2. Mahasiswa mampu menggunakan mekanisme public dan private sesuai kebutuhan.
3. Mahasiswa mampu menjaga integritas objek dengan melakukan validasi pada property maupun method.

---

## Lingkungan Pengembangan

1. Platform: Python 3.10+
2. Bahasa: Python
3. Editor/IDE yang disarankan:
   - VS Code + Python Extension
   - Terminal

---

## Cara Menjalankan Project

1. Clone repositori project `oop-encapsulation-python` ke direktori lokal Anda:
   ```bash
   git clone https://github.com/USERNAME/oop-encapsulation-python.git
   cd oop-encapsulation-python
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

### 1. Invoice

Implementasi di file `src/invoicing/invoice.py`.

Buatlah kelas `Invoice` untuk merepresentasikan faktur barang. Kelas ini memiliki empat atribut privat: `_part_number` (string), `_part_description` (string), `_quantity` (int), dan `_price` (float).

Sediakan property publik `part_number`, `part_description`, `quantity`, dan `price`.

* Setter `quantity`: jika nilai < 0, set ke 0.
* Setter `price`: jika nilai < 0, set ke 0.0.

Buat konstruktor `__init__` yang menginisialisasi keempat atribut dengan validasi sesuai aturan di atas.

Tambahkan metode `get_invoice_amount(self) -> float` yang menghitung jumlah faktur (`quantity * price`).

Tambahkan blok demo `if __name__ == "__main__":` yang membuat objek `Invoice` dan menampilkan hasil pemanggilan `get_invoice_amount`.

---

### 2. Employee

Implementasi di file `src/employment/employee.py`.

Buat kelas `Employee` dengan tiga atribut privat: `_first_name`, `_last_name`, `_monthly_salary`.

* Property `first_name`, `last_name`, dan `monthly_salary`.
* Konstruktor memvalidasi:

  * `first_name` dan `last_name` tidak boleh kosong; jika kosong → `"Unknown"`.
  * `monthly_salary` harus ≥ 0, jika < 0 → set ke 0.0.

Metode:

* `raise_salary(self, raise_percentage: int)` → menaikkan gaji bulanan **maksimal 20%**. Jika lebih, abaikan.
* `get_yearly_salary(self) -> float` → mengembalikan gaji tahunan.

Tambahkan blok demo `if __name__ == "__main__":` yang membuat dua objek `Employee`, menampilkan gaji tahunan, menaikkan gaji 10%, lalu menampilkan kembali.

---

### 3. Date

Implementasi di file `src/mycalendar/date.py`.

Buat kelas `Date` dengan tiga atribut: `_month`, `_day`, `_year`. Gunakan property dengan `getter` publik dan `setter` privat (gunakan Python `@property` untuk getter dan validasi di konstruktor).

Validasi konstruktor:

* `month` harus 1–12, `day` harus 1–31. Jika invalid, set default `1/1/1970`.

Metode:

* `display_date(self) -> str` → menampilkan tanggal dalam format `MM/DD/YYYY`.

Tambahkan blok demo `if __name__ == "__main__":`.

---

### 4. Banking

Implementasi di file `src/banking/bank_account.py`.

Buat kelas `BankAccount` dengan tiga atribut privat: `_account_number`, `_account_holder`, `_balance`.

* Validasi konstruktor:

  * `account_number` & `account_holder` tidak boleh kosong → jika kosong set `"Unknown"`.
  * `balance` awal harus ≥ 0 → jika negatif set 0.0.

Metode:

* `deposit(self, amount: float)` → tambah saldo, abaikan jika amount < 0.
* `withdraw(self, amount: float)` → kurangi saldo jika amount ≥ 0 dan tidak melebihi saldo.
* `get_balance(self) -> float` → mengembalikan saldo saat ini.

Tambahkan blok demo `if __name__ == "__main__":` yang mendemonstrasikan deposit, withdraw, dan menampilkan saldo akhir.

---

### 5. Extra

Buat soal dan solusi buatan Anda sendiri di file `src/extra/extra.py`.

Spesifikasi soal harus memuat:

* Nama kelas dan kegunaannya.
* Atribut dan property yang harus ada.
* Metode yang dibutuhkan.
* Validasi atau aturan khusus.

Tambahkan blok demo `if __name__ == "__main__":` untuk menjalankan contoh.

---