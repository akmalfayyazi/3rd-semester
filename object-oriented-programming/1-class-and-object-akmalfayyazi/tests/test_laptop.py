import pytest
from electronic.laptop import Laptop


def test_laptop_constructor_properties_set_correctly():
    # Arrange
    expected_merk = "Dell"
    expected_prosesor = "Intel Core i7"
    expected_ram = 16
    expected_penyimpanan = 512

    # Act
    laptop = Laptop(expected_merk, expected_prosesor, expected_ram, expected_penyimpanan)

    # Assert
    assert laptop.merk == expected_merk, "Merk laptop tidak sesuai dengan yang diharapkan."
    assert laptop.prosesor == expected_prosesor, "Prosesor laptop tidak sesuai dengan yang diharapkan."
    assert laptop.ram == expected_ram, "RAM laptop tidak sesuai dengan yang diharapkan."
    assert laptop.penyimpanan == expected_penyimpanan, "Penyimpanan laptop tidak sesuai dengan yang diharapkan."


def test_tampilkan_spesifikasi_output(capsys: pytest.CaptureFixture):
    # Arrange
    laptop = Laptop("Dell", "Intel Core i7", 16, 512)
    expected_output = "Merk: Dell, Prosesor: Intel Core i7, RAM: 16 GB, Penyimpanan: 512 GB\n"

    # Act
    laptop.tampilkan_spesifikasi()
    captured = capsys.readouterr()

    # Assert
    assert captured.out == expected_output
