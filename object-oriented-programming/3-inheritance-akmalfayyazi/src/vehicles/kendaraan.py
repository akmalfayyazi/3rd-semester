class Kendaraan:
    def __init__(self, merk: str, model: str):
        self._merk = merk
        self._model = model

    @property
    def merk(self):
        return self._merk

    @property
    def model(self):
        return self._model

    def tampilkan_info(self):
        print(f"Kendaraan - Merk: {self.merk}, Model: {self.model}")

class Mobil(Kendaraan):
    def __init__(self, merk, model, tipe_bodi: str):
        super().__init__(merk, model)
        self._tipe_bodi = tipe_bodi

    @property
    def tipe_bodi(self):
        return self._tipe_bodi

    def tampilkan_info(self):
        print(f"Mobil - Merk: {self.merk}, Model: {self.model}, Tipe Bodi: {self.tipe_bodi}")
    
class Motor(Kendaraan):
    def __init__(self, merk, model, tipe_mesin: str):
        super().__init__(merk, model)
        self._tipe_mesin = tipe_mesin

    @property
    def tipe_mesin(self):
        return self._tipe_mesin

    def tampilkan_info(self):
        print(f"Motor - Merk: {self.merk}, Model: {self.model}, Tipe Mesin: {self.tipe_mesin}")

if __name__ == "__main__":
    mobil1 = Mobil('Toyota', 'Avanza', 'MPV')
    motor1 = Motor('Yamaha', 'R15', '4 Stroke')

    print(mobil1.cetak())
    print()
    print(motor1.cetak())