class PeralatanOlahraga:
    def __init__(self, jenis: str, merek: str):
        self._jenis = jenis
        self._merek = merek

    @property
    def jenis(self):
        return self._jenis

    @property
    def merek(self):
        return self._merek

    def tampilkan_informasi(self):
        print(f"Peralatan Olahraga Jenis: {self.jenis}, Merek: {self.merek}")

class Bola(PeralatanOlahraga):
    def __init__(self, jenis, merek, jenis_olahraga: str, bahan: str):
        super().__init__(jenis, merek)
        self._jenis_olahraga = jenis_olahraga
        self._bahan = bahan

    @property
    def jenis_olahraga(self):
        return self._jenis_olahraga

    @property
    def bahan(self):
        return self._bahan

    def tampilkan_informasi(self):
        print(f"Peralatan Olahraga Jenis: {self.jenis}, Merek: {self.merek}")

    def tampilkan_spesifikasi(self):
        print(f"Jenis Olahraga: {self.jenis_olahraga}, Bahan: {self.bahan}")

class BolaProfesional(Bola):
    def __init__(self, jenis, merek, jenis_olahraga, bahan, standar_internasional: bool):
        super().__init__(jenis, merek, jenis_olahraga, bahan)
        self._standar_internasional = standar_internasional

    @property
    def standar_internasional(self):
        return self._standar_internasional

    def tampilkan_standar(self):
        status = "Ya" if self.standar_internasional else "Tidak"
        print(f"Jenis Olahraga: {self.jenis_olahraga}, Bahan: {self.bahan}, Standar Internasional: {status}")

class BolaLatihan(Bola):
    def __init__(self, jenis, merek, jenis_olahraga, bahan, harga: int):
        super().__init__(jenis, merek, jenis_olahraga, bahan)
        self._harga = harga

    @property
    def harga(self):
        return self._harga

if __name__ == "__main__":
    bola_pro = BolaProfesional("Bola", "Nike", "Sepakbola", "Kulit Sintetis", True)
    bola_lat = BolaLatihan("Bola", "Adidas", "Basket", "Karet", 300)

    print("=== Bola Profesional ===")
    bola_pro.tampilkan_informasi()
    bola_pro.tampilkan_spesifikasi()
    bola_pro.tampilkan_standar()

    print("\n=== Bola Latihan ===")
    bola_lat.tampilkan_informasi()
    bola_lat.tampilkan_spesifikasi()
    print(f"Harga: ${bola_lat.harga}")