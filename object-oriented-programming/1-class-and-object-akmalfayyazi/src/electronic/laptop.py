class Laptop:
    def __init__(self, merk: str, prosesor: str, ram: int, penyimpanan: int):
        self.merk = merk
        self.prosesor = prosesor
        self.ram = ram
        self.penyimpanan = penyimpanan
        
    def tampilkan_spesifikasi(self):
        print(f"Merk: {self.merk}, Prosesor: {self.prosesor}, RAM: {self.ram} GB, Penyimpanan: {self.penyimpanan} GB")

if __name__ == "__main__":
    laptop1 = Laptop("ASUS", "Intel I5", 16, 512)
    laptop1.tampilkan_spesifikasi()