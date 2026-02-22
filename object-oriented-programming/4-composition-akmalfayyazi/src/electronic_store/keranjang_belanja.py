from .item_belanja import *

class KeranjangBelanja:
    def __init__(self, items: list = None):
        self.__items = [ItemBelanja(*item) for item in items] if items else []
    
    @property
    def items(self):
        return self.__items
    
    def tambah_item_belanja(self, produk, kuantitas):
        if not isinstance(produk, Produk):
            raise TypeError('bukan produk')
        self.__items.append(ItemBelanja(produk, kuantitas))

    def hitung_total_belanja(self):
        return sum(item.hitung_total() for item in self.__items)

if __name__ == '__main__':
    produk = ['Piring', 20000]
    items = [produk, 5]
    keranjang1 = KeranjangBelanja(items)
    print(keranjang1.hitung_total_belanja())