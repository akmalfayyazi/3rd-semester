from medical_record.exceptions import DataTidakLengkapError, DataTidakValidError

class Pasien:
    def __init__(self, nama: str, umur: int, alamat: str):
        self._nama = nama
        self._umur = umur
        self._alamat = alamat

    def validasi_data(self) -> None:
        if self._nama.strip() == "" or self._alamat.strip() == "":
            raise DataTidakLengkapError()
        if self._umur < 0 or self._umur > 120:
            raise DataTidakValidError()
