class KapasitasPenuhError(Exception):
    def __init__(self, msg: str = "Kursi sudah penuh, tidak dapat memproses pemesanan."):
        super().__init__(msg)


class TiketSudahDipesanError(Exception):
    def __init__(self, msg: str = "Tiket sudah dipesan"):
        super().__init__(msg)


class NomorTiketTidakDitemukanError(Exception):
    def __init__(self, msg: str = "Nomor tiket tidak ditemukan dalam sistem."):
        super().__init__(msg)
