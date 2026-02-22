class SmsSender:
    def __init__(self, nomor: str | None = None):
        self.nomor = nomor

    def kirim(self, pesan: str) -> str:
        return f"SMS terkirim: {pesan}"