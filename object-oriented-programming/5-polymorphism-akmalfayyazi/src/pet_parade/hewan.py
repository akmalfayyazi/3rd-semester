from abc import ABC, abstractmethod

class Hewan(ABC):
    def __init__(self, nama: str):
        self.nama = nama

    @property
    def nama(self):
        return self._nama

    @nama.setter
    def nama(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Nama harus berupa string")
        if not value.strip():
            raise ValueError("Nama tidak boleh kosong atau spasi saja")
        self._nama = value.strip()

    @abstractmethod
    def bersuara(self) -> str:
        pass

class Kucing(Hewan):
    def bersuara(self) -> str:
        return "Meong"

class Anjing(Hewan):
    def bersuara(self) -> str:
        return "Guk"