class Produk:
    def __init__(self, nama: str, harga):
        self.__nama = nama.strip()
        self.__harga = float(harga)

    @property
    def nama(self):
        return self.__nama
    
    @nama.setter
    def nama(self, value: str):
        self.__nama = value.strip()

    @property
    def harga(self):
        return self.__harga
    
    @harga.setter
    def harga(self, value):
        self.__harga = float(value)