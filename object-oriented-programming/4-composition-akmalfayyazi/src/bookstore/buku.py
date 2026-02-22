class Buku:
    def __init__(self, isbn, judul, harga):
        self.__isbn = isbn
        self.__judul = judul
        self.__harga = float(harga)

    @property
    def isbn(self):
        return self.__isbn

    @property
    def judul(self):
        return self.__judul

    @property
    def harga(self):
        return self.__harga
    
    def is_isbn_match(self, isbn):
        return self.__isbn.strip() == isbn.strip()
        
    def get_info(self):
        return f"ISBN: {self.__isbn.strip()}, Judul: {self.__judul.strip()}, Harga: {self.__harga}"