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