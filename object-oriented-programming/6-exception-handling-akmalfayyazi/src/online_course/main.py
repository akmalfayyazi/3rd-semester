from online_course.peserta import Peserta
from online_course.kursus import KursusOnline

def process_registration(kursus: KursusOnline, peserta: Peserta) -> None:
    try:
        kursus.daftar_peserta(peserta)
        print(f"Pendaftaran berhasil: {peserta.get_nama()}")
    except Exception as e:
        print(f"Gagal daftar ({peserta.get_nama()})")
        print(e)  # tampilkan pesan error yang dilempar
    finally:
        print("Proses pendaftaran selesai.")

if __name__ == "__main__":
    kursus = KursusOnline()
    daftar_calon = [
        Peserta("Akmal", 17, "SMA"),
        Peserta("Budi", 22, "Diploma"),
        Peserta("Citra", 25, "Sarjana"),
        Peserta("Dewi", 30, "Magister"),
    ]

    for p in daftar_calon:
        process_registration(p, kursus)

    print("Peserta yang berhasil terdaftar:")
    for peserta in kursus.get_daftar_peserta():
        print("-", peserta._nama)
