class Penumpang:
    def __init__(self, nama: str, nomor_identitas: str):
        if not nama or str(nama).strip() == "":
            raise ValueError("Nama penumpang tidak boleh kosong.")
        if not nomor_identitas or str(nomor_identitas).strip() == "":
            raise ValueError("Nomor identitas tidak boleh kosong.")
        self._nama = nama
        self._nomor_identitas = nomor_identitas

    def get_nama(self) -> str:
        return self._nama

    def get_identitas(self) -> str:
        return self._nomor_identitas