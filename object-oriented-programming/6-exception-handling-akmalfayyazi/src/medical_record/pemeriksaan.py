from medical_record.exceptions import DataTidakLengkapError, DataTidakValidError
from medical_record.pasien import Pasien

class Pemeriksaan:
    def periksa_data(self, pasien: Pasien) -> str:
        try:
            pasien.validasi_data()
        except DataTidakLengkapError as e:
            raise DataTidakLengkapError("Validasi gagal: nama/alamat kosong.") from e
        except DataTidakValidError as e:
            # ✅ perbaiki pesan sesuai test
            raise DataTidakValidError("Validasi gagal: umur di luar rentang 0–120.") from e
        else:
            return "Data pasien valid"
