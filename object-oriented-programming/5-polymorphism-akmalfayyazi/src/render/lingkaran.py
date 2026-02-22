class Lingkaran:
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius harus berupa angka")
        if radius <= 0:
            raise ValueError("Radius harus lebih besar dari nol")
        self._radius = float(radius)

    @property
    def radius(self):
        return self._radius

    def render(self) -> str:
        r_int = int(self._radius) if self._radius.is_integer() else self._radius
        return f"Render Lingkaran (r={r_int})"