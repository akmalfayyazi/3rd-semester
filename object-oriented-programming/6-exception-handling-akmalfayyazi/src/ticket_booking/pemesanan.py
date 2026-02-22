from ticket_booking.penumpang import Penumpang
from ticket_booking.exceptions import (
    KapasitasPenuhError,
    TiketSudahDipesanError,
    NomorTiketTidakDitemukanError,
)

class PemesananTiket:
    def __init__(self, kapasitas: int):
        if not isinstance(kapasitas, int) or kapasitas <= 0:
            raise ValueError("Kapasitas harus berupa bilangan positif.")
        self._kapasitas = kapasitas
        self._data_tiket = {}

    def pesan_tiket(self, nomor_tiket: str, penumpang: Penumpang) -> None:
        if not nomor_tiket or str(nomor_tiket).strip() == "":
            raise ValueError("Nomor tiket tidak boleh kosong.")
        if len(self._data_tiket) >= self._kapasitas:
            raise KapasitasPenuhError("Kursi sudah penuh")
        if nomor_tiket in self._data_tiket:
            raise TiketSudahDipesanError("Tiket sudah dipesan")
        self._data_tiket[nomor_tiket] = penumpang


    def batalkan_tiket(self, nomor_tiket: str):
        if nomor_tiket not in self._data_tiket:
            raise NomorTiketTidakDitemukanError("Nomor tiket tidak ditemukan.")
        del self._data_tiket[nomor_tiket]

    def ada_tiket(self, nomor_tiket: str) -> bool:
        return nomor_tiket in self._data_tiket

    def get_jumlah_terpesan(self) -> int:
        return len(self._data_tiket)

    def get_kapasitas(self) -> int:
        return self._kapasitas