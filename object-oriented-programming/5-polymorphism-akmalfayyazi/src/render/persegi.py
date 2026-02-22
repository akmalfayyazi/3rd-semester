class Persegi:
    def __init__(self, sisi):
        if not isinstance(sisi, (int, float)):
            raise TypeError("Sisi harus berupa angka")
        if sisi <= 0:
            raise ValueError("Sisi harus lebih besar dari nol")
        self._sisi = float(sisi)

    @property
    def sisi(self):
        return self._sisi

    def render(self) -> str:
        s_int = int(self._sisi) if self._sisi.is_integer() else self._sisi
        return f"Render Persegi (s={s_int})"