from typing import Any

class Notifier:
    def __init__(self):
        self._pengirim = []

    def tambah_pengirim(self, pengirim):
        self._pengirim.append(pengirim)

    def kirim(self, pesan):
        if not isinstance(pesan, str):
            raise TypeError("Pesan harus berupa string")

        hasil = []
        for p in self._pengirim:
            if hasattr(p, "kirim") and callable(p.kirim):
                res = p.kirim(pesan)      # 🚫 jangan ditangkap try-except
                hasil.append(str(res))    # pastikan hasil dikonversi ke str
        return hasil


if __name__ == "__main__":
    from .email_sender import EmailSender
    from .sms_sender import SmsSender
    from .push_sender import PushSender
    from .broken_sender import BrokenSender

    notifier = Notifier()
    notifier.tambah_pengirim(EmailSender())
    notifier.tambah_pengirim(SmsSender())
    notifier.tambah_pengirim(PushSender())
    notifier.tambah_pengirim(BrokenSender())

    hasil = notifier.kirim("Halo dunia!")
    for h in hasil:
        print(h)
