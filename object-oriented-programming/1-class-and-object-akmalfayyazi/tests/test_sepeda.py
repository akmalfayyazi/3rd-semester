import pytest
from bicycle.sepeda import Sepeda


def test_sepeda_constructor_properties_set_correctly():
    # Arrange
    expected_merk = "Polygon"
    expected_tipe = "Mountain Bike"
    expected_berat = 14.5

    # Act
    sepeda = Sepeda(expected_merk, expected_tipe, expected_berat)

    # Assert
    assert sepeda.merk == expected_merk
    assert sepeda.tipe == expected_tipe
    assert sepeda.berat == expected_berat


def test_tampilkan_informasi_output(capsys: pytest.CaptureFixture):
    # Arrange
    sepeda = Sepeda("Polygon", "Mountain Bike", 14.5)
    expected_output = "Merek: Polygon, Tipe: Mountain Bike, Berat: 14.5 kg\n"

    # Act
    sepeda.tampilkan_informasi()
    captured = capsys.readouterr()

    # Assert
    assert captured.out == expected_output
