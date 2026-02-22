from ticket_booking.pemesanan import PemesananTiket
from ticket_booking.penumpang import Penumpang
from ticket_booking.exceptions import (
    KapasitasPenuhError,
    TiketSudahDipesanError,
    NomorTiketTidakDitemukanError,
)

def process_booking(sistem: PemesananTiket, nomor_tiket: str, penumpang: Penumpang) -> None:
    try:
        sistem.pesan_tiket(nomor_tiket, penumpang)
        print(f"Pesan tiket berhasil: {nomor_tiket}")
    except (KapasitasPenuhError, TiketSudahDipesanError) as e:
        print(f"Gagal pesan ({nomor_tiket})")
        print(e)  # tampilkan pesan asli, misal "Kursi sudah penuh"
    except Exception as e:
        print(f"Terjadi kesalahan tak terduga: {e}")
    finally:
        print(f"Jumlah tiket terpesan: {sistem.get_jumlah_terpesan()} dari {sistem.get_kapasitas()}")
        print("Proses pemesanan selesai.")

if __name__ == "__main__":
    sistem = PemesananTiket(kapasitas=3)
    data = [
        ("T001", Penumpang("Akmal", "ID001")),
        ("T002", Penumpang("Budi", "ID002")),
        ("T003", Penumpang("Citra", "ID003")),
        ("T004", Penumpang("Dewi", "ID004")),
    ]
    for nomor, p in data:
        process_booking(sistem, nomor, p)
