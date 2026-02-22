class Makanan:
    def __init__(self, nama: str, harga: float):
        if harga < 0:
            raise ValueError("Harga tidak boleh negatif")
        self._nama = nama
        self._harga = harga

    @property
    def nama(self):
        return self._nama

    @property
    def harga(self):
        return self._harga

class MakananRingan(Makanan):
    def __init__(self, nama, harga, jenis: str):
        super().__init__(nama, harga)
        self._jenis = jenis

    @property
    def jenis(self):
        return self._jenis

    def tampilkan_info(self):
        print(f"Makanan Ringan: {self.nama}, Harga: ${self.harga}, Jenis: {self.jenis}")

class MakananBerat(Makanan):
    def __init__(self, nama, harga, porsi: str):
        super().__init__(nama, harga)
        self._porsi = porsi

    @property
    def porsi(self):
        return self._porsi

    def tampilkan_info(self):
        print(f"Makanan Berat: {self.nama}, Harga: ${self.harga}, Porsi: {self.porsi}")

if __name__ == "__main__":
    snack = MakananRingan("Keripik Singkong", 5000, "Keripik")
    main_course = MakananBerat("Nasi Goreng", 20000, "Single")

    print("=== Demo Menu Makanan ===")
    snack.tampilkan_info()
    main_course.tampilkan_info()
