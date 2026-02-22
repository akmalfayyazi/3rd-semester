import pytest
from calc.kalkulator import Kalkulator


class TestKalkulator:
    def setup_method(self):
        # Initialize Kalkulator object before each test (setara [TestInitialize])
        self.kalkulator = Kalkulator()

    def test_tambah_returns_correct_value(self):
        assert self.kalkulator.tambah(5, 3) == 8

    def test_kurang_returns_correct_value(self):
        assert self.kalkulator.kurang(5, 3) == 2

    def test_kali_returns_correct_value(self):
        assert self.kalkulator.kali(5, 3) == 15

    def test_bagi_returns_correct_value(self):
        assert self.kalkulator.bagi(6, 3) == 2

    def test_bagi_by_zero_raises(self):
        # Implementasi Python Anda melempar ZeroDivisionError (bukan Infinity)
        with pytest.raises(ZeroDivisionError):
            self.kalkulator.bagi(1, 0)
