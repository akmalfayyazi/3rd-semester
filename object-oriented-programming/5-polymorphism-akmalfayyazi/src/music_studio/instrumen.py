from abc import abstractmethod, ABC

class Instrumen(ABC):
    def __init__(self, nama: str):
        if not isinstance(nama, str):
            raise TypeError("Nama harus berupa string")
        nama = nama.strip()
        if not nama:
            raise ValueError("Nama tidak boleh kosong")
        self._nama = nama

    @property
    def nama(self):
        return self._nama

    @nama.setter
    def nama(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Nama harus berupa string")
        value = value.strip()
        if not value:
            raise ValueError("Nama tidak boleh kosong")
        self._nama = value

    @abstractmethod
    def mainkan(self) -> str:
        pass

class Gitar(Instrumen):
    def mainkan(self) -> str:
        return "tring tring"
    
class Piano(Instrumen):
    def mainkan(self) -> str:
        return "tink tink"