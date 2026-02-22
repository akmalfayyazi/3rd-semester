import pytest
from bookstore.buku import Buku
from bookstore.toko_buku import TokoBuku


# ---------- Buku ----------
def test_buku_constructor_and_getters():
    b = Buku("978-1234567890", "Pemrograman Python", 125000.0)
    assert b.isbn == "978-1234567890"
    assert b.judul == "Pemrograman Python"
    assert b.harga == 125000.0


def test_buku_is_isbn_match_and_get_info_format():
    b = Buku(" 978-6020324788 ", " Struktur Data ", 99000)
    # is_isbn_match harus strip input
    assert b.is_isbn_match("978-6020324788") is True
    assert b.is_isbn_match("978-xxxx") is False

    # get_info harus sesuai format
    assert b.get_info() == "ISBN: 978-6020324788, Judul: Struktur Data, Harga: 99000.0"


def test_buku_getters_are_read_only():
    b = Buku("X", "Y", 1.0)
    with pytest.raises(AttributeError):
        b.isbn = "Z"    # type: ignore[attr-defined]
    with pytest.raises(AttributeError):
        b.judul = "Z"   # type: ignore[attr-defined]
    with pytest.raises(AttributeError):
        b.harga = 2.0   # type: ignore[attr-defined]


# ---------- TokoBuku ----------
def test_toko_buku_add_find_remove_and_list():
    toko = TokoBuku()
    b1 = Buku("111", "A", 10_000)
    b2 = Buku("222", "B", 20_000)
    b3 = Buku("333", "C", 30_000)

    # tambah
    toko.tambah_buku(b1)
    toko.tambah_buku(b2)
    toko.tambah_buku(b3)

    # cari
    found = toko.cari_buku("222")
    assert isinstance(found, Buku) and found.judul == "B"

    # list (pakai get_info dari Buku)
    daftar = toko.get_daftar_buku()
    assert daftar == [
        "ISBN: 111, Judul: A, Harga: 10000.0",
        "ISBN: 222, Judul: B, Harga: 20000.0",
        "ISBN: 333, Judul: C, Harga: 30000.0",
    ]

    # hapus
    toko.hapus_buku("222")
    daftar2 = toko.get_daftar_buku()
    assert daftar2 == [
        "ISBN: 111, Judul: A, Harga: 10000.0",
        "ISBN: 333, Judul: C, Harga: 30000.0",
    ]


def test_toko_buku_remove_nonexistent_is_silent():
    toko = TokoBuku()
    toko.tambah_buku(Buku("111", "A", 10_000))
    toko.hapus_buku("999")  # tidak ada -> tidak error
    assert toko.get_daftar_buku() == ["ISBN: 111, Judul: A, Harga: 10000.0"]


def test_toko_buku_daftar_buku_is_write_only_and_validates_type():
    toko = TokoBuku()

    # getter harus raise AttributeError (write-only)
    with pytest.raises(AttributeError):
        _ = toko.daftar_buku  # type: ignore[attr-defined]

    # setter: salah tipe -> TypeError
    with pytest.raises(TypeError):
        toko.daftar_buku = ["bukan Buku"]  # type: ignore[assignment]

    # setter: campuran tipe -> TypeError
    with pytest.raises(TypeError):
        toko.daftar_buku = [Buku("111", "A", 1.0), "salah"]  # type: ignore[list-item]

    # setter: list Buku valid -> mengganti seluruh daftar
    new_list = [Buku("222", "B", 2.0), Buku("333", "C", 3.0)]
    toko.daftar_buku = new_list  # OK
    assert toko.get_daftar_buku() == [
        "ISBN: 222, Judul: B, Harga: 2.0",
        "ISBN: 333, Judul: C, Harga: 3.0",
    ]


def test_toko_buku_tambah_buku_type_check():
    toko = TokoBuku()
    with pytest.raises(TypeError):
        toko.tambah_buku("bukan buku")  # type: ignore[arg-type]
