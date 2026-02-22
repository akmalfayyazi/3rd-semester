from .karya_seni import *

class StudioSeni:
    def __init__(self):
        self._list_karya: list[KaryaSeni] = []

    def tambah_karya_seni(self, karya: KaryaSeni) -> None:
        if not isinstance(karya, KaryaSeni):
            raise TypeError("Objek harus turunan dari KaryaSeni")
        self._list_karya.append(karya)

    def tampilkan_semua_karya(self) -> list[str]:
        return [karya.tampilkan() for karya in self._list_karya]

if __name__ == '__main__':
    studio = StudioSeni()
    lukisan = Lukisan("Pemandangan Senja")
    patung = Patung("Patung Kuda")

    studio.tambah_karya_seni(lukisan)
    studio.tambah_karya_seni(patung)

    hasil = studio.tampilkan_semua_karya()
    for h in hasil:
        print(h)