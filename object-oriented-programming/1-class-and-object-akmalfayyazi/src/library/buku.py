class Buku:
    def __init__(self, Judul: str, Penulis: str, Tahun_Terbit: int):
        self.judul = Judul
        self.penulis = Penulis
        self.tahun_terbit = Tahun_Terbit

    def tampilkan_info(self):
        print(f"Judul: {self.judul}, Penulis: {self.penulis}, Tahun Terbit: {self.tahun_terbit}")

if __name__ == "__main__":
    buku1 = Buku()
    buku1.tampilkan_info()