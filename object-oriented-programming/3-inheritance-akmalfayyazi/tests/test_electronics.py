import pytest
from electronics.perangkat_elektronik import PerangkatElektronik, Smartphone, FlagshipPhone, BudgetPhone


def test_perangkat_elektronik_identitas(capsys: pytest.CaptureFixture):
    p = PerangkatElektronik("Acme", "X100")
    assert p.brand == "Acme"
    assert p.model == "X100"

    p.tampilkan_identitas()
    out = capsys.readouterr().out
    assert out == "Perangkat Brand: Acme, Model: X100\n"


def test_smartphone_fitur_dasar(capsys: pytest.CaptureFixture):
    s = Smartphone("Acme", "S1", "Android", "LCD, RAM, dll.")
    assert s.brand == "Acme"
    assert s.model == "S1"
    assert s.sistem_operasi == "Android"
    assert s.fitur_dasar == "LCD, RAM, dll."

    s.tampilkan_fitur_dasar()
    out = capsys.readouterr().out
    assert out == "Fitur Dasar: LCD, RAM, dll.\n"


def test_flagship_fitur_premium_prints_two_lines(capsys: pytest.CaptureFixture):
    f = FlagshipPhone("Acme", "Pro X", "Android", "LCD, RAM, dll.", "Camera Telephoto")
    f.tampilkan_fitur_premium()
    out = capsys.readouterr().out.splitlines()
    assert out == ["Fitur Dasar: LCD, RAM, dll.", "Fitur Premium: Camera Telephoto"]


def test_budget_harga_and_fitur(capsys: pytest.CaptureFixture):
    b = BudgetPhone("Acme", "Lite A1", "Android", "LCD, RAM, dll.", 2999000)
    assert b.harga == 2999000

    b.tampilkan_fitur_dasar()
    out = capsys.readouterr().out
    assert out == "Fitur Dasar: LCD, RAM, dll.\n"
