class Mobil:
    def __init__(self, merk: str, model: str, tahun_produksi: int):
        self.merk = merk
        self.model = model
        self.tahun_produksi = tahun_produksi

    def tampilkan_spesifikasi(self):
        print(f"Merk: {self.merk}, Model: {self.model}, Tahun Produksi: {self.tahun_produksi}")

if __name__ == "__main__":
    mobil1 = Mobil("Toyota", "Innova", 2020)
    mobil1.tampilkan_spesifikasi()