class EmailSender:
    def __init__(self, alamat: str | None = None):
        self.alamat = alamat  # disimpan tapi tidak wajib dipakai

    def kirim(self, pesan: str) -> str:
        return f"Email terkirim: {pesan}"