# src/render/renderer.py
from typing import Any

class ShapeRenderer:
    def __init__(self):
        self._bentuk_list = []

    def tambah_bentuk(self, bentuk):
        self._bentuk_list.append(bentuk)

    def render_semua(self) -> list[str]:
        hasil = []
        for bentuk in self._bentuk_list:
            if hasattr(bentuk, "render") and callable(bentuk.render):
                hasil.append(str(bentuk.render()))
        return hasil


if __name__ == "__main__":
    from .lingkaran import Lingkaran
    from .persegi import Persegi
    from .segitiga import Segitiga
    from .bukan_bentuk import BukanBentuk

    renderer = ShapeRenderer()
    renderer.tambah_bentuk(Lingkaran(5))
    renderer.tambah_bentuk(Persegi(4))
    renderer.tambah_bentuk(Segitiga(6, 3))
    renderer.tambah_bentuk(BukanBentuk())

    hasil = renderer.render_semua()
    for h in hasil:
        print(h)
