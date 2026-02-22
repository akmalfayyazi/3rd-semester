from bank_account.exceptions import RekeningTidakDitemukanError
from bank_account.rekening import Rekening

class Bank:
    def __init__(self):
        self._daftar: dict[str, Rekening] = {}

    def tambah_rekening(self, rek: Rekening) -> None:
        if rek.get_nomor() in self._daftar:
            raise ValueError("Nomor rekening sudah ada")
        self._daftar[rek.get_nomor()] = rek

    def cari_rekening(self, nomor: str) -> Rekening:
        if nomor not in self._daftar:
            raise RekeningTidakDitemukanError()
        return self._daftar[nomor]
