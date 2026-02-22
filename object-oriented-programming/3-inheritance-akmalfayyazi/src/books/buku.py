class Buku:
    def __init__(self, judul: str, pengarang: str):
        self._judul = judul
        self._pengarang = pengarang

    @property
    def judul(self):
        return self._judul
    
    @judul.setter
    def judul(self, value):
        self._judul = value.strip()

    @property
    def pengarang(self):
        return self._pengarang
    
    @pengarang.setter
    def pengarang(self, value):
        self._pengarang = value.strip()

class BukuFiksi(Buku):
    def __init__(self, judul, pengarang, genre: str):
        super().__init__(judul, pengarang)
        self._genre = genre
    
    @property
    def genre(self):
        return self._genre
    
    @genre.setter
    def genre(self, value):
        self._genre = value
    
    def tampilkan_info(self):
        print(f"Buku Fiksi - Judul: {self.judul}, Pengarang: {self.pengarang}, Genre: {self.genre}")

class BukuPelajaran(Buku):
    def __init__(self, judul, pengarang, subjek: str):
        super().__init__(judul, pengarang)
        self._subjek = subjek

    @property
    def subjek(self):
        return self._subjek
    
    @subjek.setter
    def subjek(self, value):
        self._subjek = value

    def tampilkan_info(self):
        print(f"Buku Pelajaran - Judul: {self.judul}, Pengarang: {self.pengarang}, Subjek: {self.subjek}")


if __name__ == "__main__":
    BukuFiksi1 = BukuFiksi('Bedebah Di Ujung Tanduk', 'Tereliye', 'Advanture')
    BukuPelajaran1 = BukuPelajaran('Money Management', 'Andrew Tate', 'Self-development')
    BukuFiksi1.tampilkan_info()
    BukuPelajaran1.tampilkan_info()