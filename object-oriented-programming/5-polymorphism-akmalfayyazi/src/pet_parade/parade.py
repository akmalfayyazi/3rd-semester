from .hewan import *

class ParadeHewan:
    def __init__(self):
        self._list_hewan: list[Hewan] = []

    def tambah_hewan(self, hewan: Hewan) -> None:
        if not isinstance(hewan, Hewan):
            raise TypeError("Hanya objek turunan Hewan yang dapat ditambahkan")
        self._list_hewan.append(hewan)

    def hapus_hewan(self, hewan: Hewan) -> None:
        if hewan in self._list_hewan:
            self._list_hewan.remove(hewan)

    def mulai_parade(self, putaran: int) -> list[str]:
        if not isinstance(putaran, int):
            raise TypeError("Putaran harus berupa integer")
        if putaran <= 0:
            raise ValueError("Putaran harus berupa bilangan bulat positif")

        hasil = []
        for _ in range(putaran):
            for h in self._list_hewan:
                hasil.append(f"{h.nama} bersuara: {h.bersuara()}")
        return hasil
    
if __name__ == '__main__':
    parade = ParadeHewan()
    kucing = Kucing('Mimi')
    anjing = Anjing('Dodo')

    parade.tamhab_hewan(kucing)
    parade.tamhab_hewan(anjing)

    hasil = parade.mulai_parade(2)
    print(hasil)