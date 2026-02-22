class PushSender:
    def __init__(self, token: str | None = None):
        self.token = token

    def kirim(self, pesan: str) -> str:
        return f"Push terkirim: {pesan}"
