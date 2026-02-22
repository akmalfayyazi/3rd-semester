from online_course.exceptions import (
    UsiaTidakMemenuhiSyaratError,
    PendidikanTidakMemenuhiSyaratError,
)

class Peserta:
    def __init__(self, nama: str, usia: int, tingkat_pendidikan: str):
        if not nama or str(nama).strip() == "":
            raise ValueError("Nama tidak boleh kosong.")
        if not isinstance(usia, int):
            raise ValueError("Usia harus bertipe int.")
        if usia < 0:
            raise ValueError("Usia tidak boleh negatif.")

        # ❌ Jangan raise error kalau pendidikan kosong
        self._nama = nama
        self._usia = usia
        self._tingkat_pendidikan = tingkat_pendidikan or ""


    def get_nama(self) -> str:
        return self._nama

    def get_usia(self) -> int:
        return self._usia

    def get_tingkat_pendidikan(self) -> str:
        return self._tingkat_pendidikan

    def cek_kelayakan(self) -> None:
        if self._usia < 18:
            raise UsiaTidakMemenuhiSyaratError()
        if self._tingkat_pendidikan not in {"Sarjana", "Magister"}:
            raise PendidikanTidakMemenuhiSyaratError()
