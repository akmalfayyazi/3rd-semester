class Sepeda:
    def __init__(self, merk: str, tipe: str, berat: float):
        self.merk = merk
        self.tipe = tipe
        self.berat = berat

    def tampilkan_informasi(self):
        print(f"Merek: {self.merk}, Tipe: {self.tipe}, Berat: {self.berat} kg")

if __name__ == "__main__":
    sepeda1 = Sepeda("POLYGON", "BMX", 9.8)
    sepeda1.tampilkan_informasi()