class PerangkatElektronik:
    def __init__(self, brand: str, model: str):
        self._brand = brand
        self._model = model

    @property
    def brand(self):
        return self._brand

    @property
    def model(self):
        return self._model

    def tampilkan_identitas(self):
        print(f"Perangkat Brand: {self.brand}, Model: {self.model}")

class Smartphone(PerangkatElektronik):
    def __init__(self, brand, model, sistem_operasi: str, fitur_dasar: str):
        super().__init__(brand, model)
        self._sistem_operasi = sistem_operasi
        self._fitur_dasar = fitur_dasar

    @property
    def sistem_operasi(self):
        return self._sistem_operasi

    @property
    def fitur_dasar(self):
        return self._fitur_dasar

    def tampilkan_fitur_dasar(self):
        print(f"Fitur Dasar: {self.fitur_dasar}")

class FlagshipPhone(Smartphone):
    def __init__(self, brand, model, sistem_operasi, fitur_dasar, fitur_premium: str):
        super().__init__(brand, model, sistem_operasi, fitur_dasar)
        self._fitur_premium = fitur_premium

    @property
    def fitur_premium(self):
        return self._fitur_premium

    def tampilkan_fitur_premium(self):
        self.tampilkan_fitur_dasar()
        print(f"Fitur Premium: {self.fitur_premium}")

class BudgetPhone(Smartphone):
    def __init__(self, brand, model, sistem_operasi, fitur_dasar, harga: int):
        super().__init__(brand, model, sistem_operasi, fitur_dasar)
        self._harga = harga

    @property
    def harga(self):
        return self._harga

if __name__ == "__main__":
    flagship = FlagshipPhone("Apple", "iPhone 15 Pro", "iOS", "Panggilan & SMS", "Face ID, Kamera ProRAW")
    budget = BudgetPhone("Xiaomi", "Redmi 12", "Android", "Panggilan & SMS", 2000)

    print("=== Flagship Phone ===")
    flagship.tampilkan_identitas()
    flagship.tampilkan_fitur_premium()

    print("\n=== Budget Phone ===")
    budget.tampilkan_identitas()
    budget.tampilkan_fitur_dasar()
    print(f"Harga: ${budget.harga}")
