from abc import ABC, abstractmethod

class Transportasi(ABC):
    def __init__(self, nama: str, kecepatan: float):
        if kecepatan <= 0:
            raise ValueError("Kecepatan harus positif")
        self._nama = nama.strip()
        self._kecepatan = kecepatan

    @property
    def nama(self):
        return self._nama

    @property
    def kecepatan(self):
        return self._kecepatan

    @abstractmethod
    def bergerak(self) -> str:
        """Harus mengembalikan cara kendaraan bergerak."""
        pass

class Mobil(Transportasi):
    def bergerak(self) -> str:
        return f"{self.nama} melaju di jalan dengan kecepatan {self.kecepatan} km/jam"

class Perahu(Transportasi):
    def bergerak(self) -> str:
        return f"{self.nama} berlayar di air dengan kecepatan {self.kecepatan} knot"


class Pesawat(Transportasi):
    def bergerak(self) -> str:
        return f"{self.nama} terbang di udara dengan kecepatan {self.kecepatan} km/jam"

class Robot:
    def bergerak(self) -> str:
        return "Robot berjalan menggunakan roda"

def mulai_perjalanan(kendaraan_list: list):
    hasil = []
    for k in kendaraan_list:
        if hasattr(k, "bergerak") and callable(k.bergerak):
            hasil.append(k.bergerak())
    return hasil

if __name__ == "__main__":
    mobil = Mobil("Avanza", 100)
    perahu = Perahu("Ferry", 25)
    pesawat = Pesawat("Boeing", 850)
    robot = Robot()  # tidak mewarisi Transportasi tapi punya metode bergerak()

    semua = [mobil, perahu, pesawat, robot]
    for hasil in mulai_perjalanan(semua):
        print(hasil)