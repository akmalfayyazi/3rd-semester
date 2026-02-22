from calculator import Calculator

def main():
    calc = Calculator()
    while True:
        try:
            a_input = input("Masukkan angka pertama: ")
            if a_input.lower() == "exit":
                break
            a = float(a_input)

            b_input = input("Masukkan angka kedua: ")
            if b_input.lower() == "exit":
                break
            b = float(b_input)

            operasi = input("Pilih operasi (Tambah, Kurang, Kali, Bagi): ").strip().lower()
            if operasi == "exit":
                break

            if operasi == "tambah":
                calc.tambah(a, b)
            elif operasi == "kurang":
                calc.kurang(a, b)
            elif operasi == "kali":
                calc.kali(a, b)
            elif operasi == "bagi":
                calc.bagi(a, b)
            else:
                print("Operasi tidak valid. Silakan pilih Tambah, Kurang, Kali, atau Bagi.")

        except ValueError:
            print("Input tidak valid. Pastikan Anda memasukkan angka.")

        lanjut = input("Ketik 'exit' untuk keluar, atau tekan Enter untuk melanjutkan: ").strip().lower()
        if lanjut == "exit":
            break

if __name__ == "__main__":
    main()