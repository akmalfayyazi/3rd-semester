from online_course.peserta import Peserta

class KursusOnline:
    def __init__(self):
        self._peserta: list[Peserta] = []

    def daftar_peserta(self, peserta: Peserta) -> None:
        peserta.cek_kelayakan()
        self._peserta.append(peserta)

    def get_daftar_peserta(self) -> list[Peserta]:
        return self._peserta
