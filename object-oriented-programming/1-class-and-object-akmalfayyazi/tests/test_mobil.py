import pytest
from auto.mobil import Mobil


def test_mobil_constructor_and_properties():
    # Arrange
    merk = "Toyota"
    model = "Corolla"
    tahun_produksi = 2020

    # Act
    mobil = Mobil(merk, model, tahun_produksi)

    # Assert
    assert mobil.merk == merk
    assert mobil.model == model
    assert mobil.tahun_produksi == tahun_produksi


def test_tampilkan_spesifikasi_output(capsys: pytest.CaptureFixture):
    # Arrange
    mobil = Mobil("Toyota", "Corolla", 2020)
    expected_output = "Merk: Toyota, Model: Corolla, Tahun Produksi: 2020\n"

    # Act
    mobil.tampilkan_spesifikasi()
    captured = capsys.readouterr()

    # Assert
    assert captured.out == expected_output
