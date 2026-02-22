class Kalkulator:
    def tambah(self, a: float, b: float) -> float:
        return a + b 

    def kurang(self, a: float, b: float) -> float:
        return a - b 

    def kali(self, a: float, b: float) -> float:
        return a * b 

    def bagi(self, a: float, b: float) -> float:
        return a / b 


if __name__ == "__main__":
    kalkulator = Kalkulator()
    print(kalkulator.tambah(132.2, 20))
    print(kalkulator.kurang(2.3, 23.43))
    print(kalkulator.kali(12.3, 3))
    print(kalkulator.bagi(33, 21))