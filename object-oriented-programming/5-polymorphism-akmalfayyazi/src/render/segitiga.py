class Segitiga:
    def __init__(self, alas, tinggi):
        if not isinstance(alas, (int, float)) or not isinstance(tinggi, (int, float)):
            raise TypeError("Alas dan tinggi harus berupa angka")
        if alas <= 0 or tinggi <= 0:
            raise ValueError("Alas dan tinggi harus lebih besar dari nol")
        self._alas = float(alas)
        self._tinggi = float(tinggi)

    @property
    def alas(self):
        return self._alas

    @property
    def tinggi(self):
        return self._tinggi

    def render(self) -> str:
        a_int = int(self._alas) if self._alas.is_integer() else self._alas
        t_int = int(self._tinggi) if self._tinggi.is_integer() else self._tinggi
        return f"Render Segitiga (a={a_int}, t={t_int})"