from .buku import *

class TokoBuku:
    def __init__(self, daftar_buku: list[Buku] = None):
        self.__daftar_buku = [Buku(*b) for b in daftar_buku] if daftar_buku else []
        
    @property
    def daftar_buku(self):
        raise AttributeError("write-only")

    @daftar_buku.setter
    def daftar_buku(self, value):
        if not isinstance(value, list) or not all(isinstance(b, Buku) for b in value):
            raise TypeError("daftar_buku harus list of Buku")
        self.__daftar_buku = value

    def tambah_buku(self, buku: Buku):
        if not isinstance(buku, Buku):
            raise TypeError("bukan Buku")
        self.__daftar_buku.append(buku)

    def hapus_buku(self, isbn: str):
        for lst in self.__daftar_buku:
            if lst.is_isbn_match(isbn):
                self.__daftar_buku.remove(lst)
                break

    def cari_buku(self, isbn):
        for b in self.__daftar_buku:
            if b.is_isbn_match(isbn):
                return b
        return None
        
    def get_daftar_buku(self):
        return [b.get_info() for b in self.__daftar_buku]
    
if __name__ == '__main__':
    buku = ['978-623-02-1769-2', 'Buku Budidaya Ikan Sistem Bioflok', 97000], ['978-623-02-1769-2', 'Buku Budidaya Ikan Sistem Bioflok', 970000]
    buku2 = ['978-623-02-1769-2', 'Buku Budidaya Ikan Sistem Bioflok', 9700]
    toko_buku = TokoBuku(buku)
    toko_buku.tambah_buku(buku2)
    print(toko_buku.get_daftar_buku())