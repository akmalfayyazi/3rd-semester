from .produk import *

class ItemBelanja:
    def __init__(self, produk, kuantitas):
        self.__produk = produk
        self.kuantitas = kuantitas

    @property
    def produk(self):
        return self.__produk
    
    @produk.setter
    def produk(self, value):
        if not isinstance(value, Produk):
            raise TypeError('bukan produk')
        self.__produk = value

    @property
    def kuantitas(self):
        return self.__kuantitas
    
    @kuantitas.setter
    def kuantitas(self, value):
        self.__kuantitas = max(0, int(value))

    def hitung_total(self):
        return self.produk.harga * self.kuantitas