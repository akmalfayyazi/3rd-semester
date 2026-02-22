import pytest
from electronic_store.produk import Produk
from electronic_store.item_belanja import ItemBelanja
from electronic_store.keranjang_belanja import KeranjangBelanja


# ---------- Produk ----------
def test_produk_constructor_and_properties():
    p = Produk("Kipas Angin", 199_000)
    assert p.nama == "Kipas Angin"
    assert p.harga == 199_000

def test_produk_setters_trim_and_cast():
    p = Produk("  TV  ", "2500000")
    assert p.nama == "TV"                  # trim
    assert isinstance(p.harga, float)
    assert p.harga == 2_500_000.0          # cast ke float

# ---------- ItemBelanja ----------
def test_item_belanja_basic_and_total():
    p = Produk("Keyboard", 499_000)
    item = ItemBelanja(p, 2)
    assert item.produk is p
    assert item.kuantitas == 2
    assert item.hitung_total() == 998_000

def test_item_belanja_negative_quantity_becomes_zero():
    item = ItemBelanja(Produk("USB Hub", 99_000), -5)
    assert item.kuantitas == 0
    assert item.hitung_total() == 0.0

def test_item_belanja_setters_validation_and_coercion():
    item = ItemBelanja(Produk("Mouse", 150_000), 1)

    # produk harus instance Produk
    with pytest.raises(TypeError):
        item.produk = "bukan produk"  # type: ignore[assignment]

    # kuantitas di-cast ke int dan dibatasi minimal 0
    item.kuantitas = "3"
    assert item.kuantitas == 3
    item.kuantitas = -1
    assert item.kuantitas == 0

# ---------- KeranjangBelanja ----------
def test_keranjang_tambah_item_and_total():
    cart = KeranjangBelanja()
    cart.tambah_item_belanja(Produk("Headset", 349_000), 1)
    cart.tambah_item_belanja(Produk("Keyboard", 499_000), 2)
    cart.tambah_item_belanja(Produk("USB Hub", 99_000), 3)

    # items getter-only mengembalikan list yang bisa diiterasi
    assert len(cart.items) == 3
    # total = 349000*1 + 499000*2 + 99000*3
    expected = 349_000 + 998_000 + 297_000
    assert cart.hitung_total_belanja() == expected

def test_keranjang_rejects_wrong_product_type():
    cart = KeranjangBelanja()
    with pytest.raises(TypeError):
        cart.tambah_item_belanja("bukan produk", 1)  # type: ignore[arg-type]

def test_keranjang_items_is_live_reference():
    cart = KeranjangBelanja()
    cart.tambah_item_belanja(Produk("Router", 750_000), 1)

    # 'items' mengacu ke list internal (read-only via properti, tapi referensinya live)
    items_ref = cart.items
    assert len(items_ref) == 1

    cart.tambah_item_belanja(Produk("Switch", 500_000), 1)
    assert len(items_ref) == 2  # bertambah juga karena referensi live
