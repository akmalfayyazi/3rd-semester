from medical_record.pasien import Pasien
from medical_record.pemeriksaan import Pemeriksaan
from medical_record.exceptions import DataTidakLengkapError, DataTidakValidError

if __name__ == "__main__":
    pemeriksaan = Pemeriksaan()

    daftar_pasien = [
        Pasien("", 25, "Jl. Merdeka"),         # Nama kosong
        Pasien("Budi", 30, ""),                # Alamat kosong
        Pasien("Citra", 150, "Jl. Sudirman"),  # Umur tidak valid
        Pasien("Dewi", 35, "Jl. Gajah Mada"),  # Valid
    ]

    for p in daftar_pasien:
        try:
            hasil = pemeriksaan.periksa_data(p)
            print(f"{p._nama or '(tanpa nama)'}: {hasil}")
        except (DataTidakLengkapError, DataTidakValidError) as e:
            print(f"Error: {e}")
            if e.__cause__:
                print(f"Penyebab asli: {e.__cause__}")
        finally:
            print("Proses pemeriksaan selesai.\n")
