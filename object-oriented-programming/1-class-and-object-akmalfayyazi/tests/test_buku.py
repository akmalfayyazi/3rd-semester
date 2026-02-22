import pytest
from library.buku import Buku


def test_buku_constructor_properties_set_correctly():
    # Arrange
    expected_judul = "Nama Buku"
    expected_penulis = "Penulis Buku"
    expected_tahun_terbit = 2021

    # Act
    buku = Buku(expected_judul, expected_penulis, expected_tahun_terbit)

    # Assert
    assert buku.judul == expected_judul, "Judul buku tidak sesuai dengan yang diharapkan."
    assert buku.penulis == expected_penulis, "Penulis buku tidak sesuai dengan yang diharapkan."
    assert buku.tahun_terbit == expected_tahun_terbit, "Tahun terbit buku tidak sesuai dengan yang diharapkan."


def test_tampilkan_info_output(capsys: pytest.CaptureFixture):
    # Arrange
    buku = Buku("Nama Buku", "Penulis Buku", 2021)
    expected = "Judul: Nama Buku, Penulis: Penulis Buku, Tahun Terbit: 2021\n"

    # Act
    buku.tampilkan_info()
    captured = capsys.readouterr()

    # Assert
    assert captured.out == expected
