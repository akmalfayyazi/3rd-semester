# src/extra/extra.py

class NilaiTidakValidError(Exception):
    def __init__(self, message="Nilai harus antara 0 dan 100."):
        super().__init__(message)

class MahasiswaTidakDitemukanError(Exception):
    def __init__(self, message="Mahasiswa tidak ditemukan dalam sistem."):
        super().__init__(message)


class SistemNilai:
    def __init__(self):
        self._data_nilai: dict[str, float] = {}

    def tambah_nilai(self, nama: str, nilai: float) -> None:
        if not 0 <= nilai <= 100:
            raise NilaiTidakValidError()
        self._data_nilai[nama] = nilai

    def ambil_nilai(self, nama: str) -> float:
        try:
            return self._data_nilai[nama]
        except KeyError as e:
            raise MahasiswaTidakDitemukanError(f"Data nilai untuk '{nama}' tidak ditemukan.") from e


if __name__ == "__main__":
    sistem = SistemNilai()

    data_uji = [
        ("Akmal", 95),
        ("Budi", -5),       # Nilai tidak valid
        ("Citra", 110),     # Nilai tidak valid
    ]

    for nama, nilai in data_uji:
        try:
            sistem.tambah_nilai(nama, nilai)
            print(f"✅ Nilai {nilai} untuk {nama} berhasil ditambahkan.")
        except NilaiTidakValidError as e:
            print(f"❌ Error saat menambahkan nilai {nama}: {e}")
        finally:
            print("Proses input selesai.\n")

    # Coba ambil nilai yang tidak ada
    try:
        print("Nilai Dewa:", sistem.ambil_nilai("Dewa"))
    except MahasiswaTidakDitemukanError as e:
        print(f"❌ Error: {e}")
        if e.__cause__:
            print(f"   ↳ Penyebab asli: {e.__cause__}")
    finally:
        print("\nProgram berakhir normal meskipun ada error.")
