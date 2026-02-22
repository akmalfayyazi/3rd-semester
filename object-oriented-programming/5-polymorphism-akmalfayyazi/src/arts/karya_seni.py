from abc import ABC, abstractmethod

class KaryaSeni(ABC):
    def __init__(self, judul: str):
        if not isinstance(judul, str):
            raise TypeError("Judul harus berupa string")
        judul = judul.strip()
        if not judul:
            raise ValueError("Judul tidak boleh kosong")
        self._judul = judul

    @property
    def judul(self):
        return self._judul

    @judul.setter
    def judul(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Judul harus berupa string")
        value = value.strip()
        if not value:
            raise ValueError("Judul tidak boleh kosong")
        self._judul = value

    @abstractmethod
    def deskripsi(self) -> str:
        pass

    @abstractmethod
    def tampilkan(self) -> str:
        pass

class Lukisan(KaryaSeni):
    def deskripsi(self) -> str:
        return "Sebuah gambar yang dilukis di atas kanvas"

    def tampilkan(self) -> str:
        return "Digantung di dinding"


class Patung(KaryaSeni):
    def deskripsi(self) -> str:
        return "Sebuah objek tiga dimensi yang dibentuk"

    def tampilkan(self) -> str:
        return "Diletakkan di atas meja atau lantai"
