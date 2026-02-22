import pytest
from books.buku import Buku, BukuFiksi, BukuPelajaran


def test_buku_base_properties_get_set():
    b = Buku("Judul A", "Pengarang A")
    assert b.judul == "Judul A"
    assert b.pengarang == "Pengarang A"

    # uji setter
    b.judul = "  Judul B  "
    b.pengarang = "  Pengarang B  "
    assert b.judul == "Judul B"
    assert b.pengarang == "Pengarang B"


def test_buku_fiksi_inheritance_and_output(capsys: pytest.CaptureFixture):
    bf = BukuFiksi("Laut Bercerita", "Leila S. Chudori", "Drama")
    assert bf.judul == "Laut Bercerita"
    assert bf.pengarang == "Leila S. Chudori"
    assert bf.genre == "Drama"

    bf.tampilkan_info()
    out = capsys.readouterr().out
    assert out == "Buku Fiksi - Judul: Laut Bercerita, Pengarang: Leila S. Chudori, Genre: Drama\n"


def test_buku_pelajaran_inheritance_and_output(capsys: pytest.CaptureFixture):
    bp = BukuPelajaran("Kalkulus Dasar", "James Stewart", "Matematika")
    assert bp.judul == "Kalkulus Dasar"
    assert bp.pengarang == "James Stewart"
    assert bp.subjek == "Matematika"

    bp.tampilkan_info()
    out = capsys.readouterr().out
    assert out == "Buku Pelajaran - Judul: Kalkulus Dasar, Pengarang: James Stewart, Subjek: Matematika\n"
