class SaldoTidakCukupError(Exception):
    def __init__(self, message="Saldo tidak mencukupi!"):
        super().__init__(message)

class RekeningTidakDitemukanError(Exception):
    def __init__(self, message="Rekening tidak ditemukan!"):
        super().__init__(message)

class BatasPenarikanError(Exception):
    def __init__(self, message="Melebihi batas penarikan harian."):
        super().__init__(message)