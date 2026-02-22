from bank_account.exceptions import (
    SaldoTidakCukupError,
    BatasPenarikanError,
    RekeningTidakDitemukanError,
)
from bank_account.rekening import Rekening
from bank_account.bank import Bank

if __name__ == "__main__":
    bank = Bank()

    # Tambah rekening
    r1 = Rekening("001", 150_000)
    r2 = Rekening("002", 80_000)
    bank.tambah_rekening(r1)
    bank.tambah_rekening(r2)

    try:
        # Kasus: rekening tidak ditemukan
        rek = bank.cari_rekening("003")

        # Kasus: penarikan melebihi saldo
        rek.penarikan(200_000)

        # Kasus: penarikan melebihi batas harian
        rek.penarikan(150_000)

        # Kasus: penarikan valid
        rek.penarikan(50_000)

    except SaldoTidakCukupError as e:
        print("Error:", e)
    except BatasPenarikanError as e:
        print("Error:", e)
    except RekeningTidakDitemukanError as e:
        print("Error:", e)
    except Exception as e:
        print("Error tidak terduga:", e)
    finally:
        print("\nSaldo akhir:")
        for nomor in ["001", "002"]:
            rek = bank.cari_rekening(nomor)
            print(f"Rekening {rek.get_nomor()}: Rp{rek.get_saldo():,.0f}")