from bank_account.exceptions import (
    SaldoTidakCukupError,
    BatasPenarikanError,
)

class Rekening:
    BATAS_PENARIKAN_HARIAN = 100_000

    def __init__(self, nomor: str, saldo: float = 0):
        if not nomor or str(nomor).strip() == "":
            raise ValueError("Nomor rekening tidak boleh kosong.")
        if saldo < 0:
            raise ValueError("Saldo awal tidak boleh negatif.")
        self._nomor = nomor
        self._saldo = saldo

    def penarikan(self, jumlah: float) -> None:
        # 🔹 Tambahan validasi tipe data
        if not isinstance(jumlah, (int, float)):
            raise ValueError("Jumlah penarikan harus berupa angka.")

        if jumlah <= 0:
            raise ValueError("Jumlah penarikan harus > 0")
        if jumlah > self.BATAS_PENARIKAN_HARIAN:
            raise BatasPenarikanError()
        if jumlah > self._saldo:
            raise SaldoTidakCukupError()
        self._saldo -= jumlah


    def get_saldo(self) -> float:
        return self._saldo

    def get_nomor(self) -> str:
        return self._nomor