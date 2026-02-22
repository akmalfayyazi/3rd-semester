import pytest
from sports.peralatan_olahraga import PeralatanOlahraga, Bola, BolaProfesional, BolaLatihan


def test_peralatan_olahraga_info(capsys: pytest.CaptureFixture):
    p = PeralatanOlahraga("Raket", "Yonex")
    assert p.jenis == "Raket"
    assert p.merek == "Yonex"

    p.tampilkan_informasi()
    out = capsys.readouterr().out
    assert out == "Peralatan Olahraga Jenis: Raket, Merek: Yonex\n"


def test_bola_spesifikasi(capsys: pytest.CaptureFixture):
    b = Bola("Bola", "Molten", "Basket", "Karet")
    assert b.jenis_olahraga == "Basket"
    assert b.bahan == "Karet"

    b.tampilkan_spesifikasi()
    out = capsys.readouterr().out
    assert out == "Jenis Olahraga: Basket, Bahan: Karet\n"


def test_bola_profesional_standar_print(capsys: pytest.CaptureFixture):
    bp = BolaProfesional("Bola", "FIFA Pro", "Sepakbola", "Kulit Sintetis", True)
    bp.tampilkan_standar()
    out = capsys.readouterr().out
    assert out == "Jenis Olahraga: Sepakbola, Bahan: Kulit Sintetis, Standar Internasional: Ya\n"

    bp2 = BolaProfesional("Bola", "Local", "Futsal", "PU", False)
    bp2.tampilkan_standar()
    out2 = capsys.readouterr().out
    assert out2 == "Jenis Olahraga: Futsal, Bahan: PU, Standar Internasional: Tidak\n"


def test_bola_latihan_harga_property():
    bl = BolaLatihan("Bola", "StreetPlay", "Basket", "Karet", 350000)
    assert bl.harga == 350000
