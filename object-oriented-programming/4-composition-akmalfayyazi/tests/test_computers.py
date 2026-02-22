import pytest
from computers.processor import Processor
from computers.memory import Memory
from computers.computer import Computer


# ---------- Processor ----------
def test_processor_constructor_and_properties():
    p = Processor("Intel", 3.5)
    assert p.brand == "Intel"
    assert p.speed == 3.5

def test_processor_brand_trim_and_speed_cast():
    p = Processor("  AMD  ", "4.2")
    assert p.brand == "AMD"      # trim
    assert isinstance(p.speed, float)
    assert p.speed == 4.2        # cast to float

# ---------- Memory ----------
def test_memory_constructor_and_properties():
    m = Memory(16, "DDR5")
    assert m.capacity == 16
    assert m.memory_type == "DDR5"

def test_memory_capacity_cast_and_type_trim():
    m = Memory("32", "  DDR4 ")
    assert isinstance(m.capacity, int)
    assert m.capacity == 32
    assert m.memory_type == "DDR4"   # trim

# ---------- Computer (composition) ----------
def test_computer_composition_and_get_info_format():
    p = Processor("Intel", 3.9)
    m = Memory(16, "DDR5")
    c = Computer(p, m)

    # Komposisi terset dengan benar
    assert isinstance(c.processor, Processor)
    assert isinstance(c.memory, Memory)

    # Format string tepat
    expected = (
        "Processor Brand: Intel, Kecepatan: 3.9, "
        "Memory Kapasitas: 16, Tipe: DDR5"
    )
    assert c.get_info() == expected

def test_computer_setters_type_validation():
    p = Processor("Intel", 3.0)
    m = Memory(8, "DDR4")
    c = Computer(p, m)

    with pytest.raises(TypeError):
        c.processor = "bukan-processor"   # type: ignore[assignment]
    with pytest.raises(TypeError):
        c.memory = 123                    # type: ignore[assignment]

def test_computer_mutation_reflects_in_get_info():
    p = Processor("AMD", 4.0)
    m = Memory(32, "DDR5")
    c = Computer(p, m)

    # Ubah komponen dan cek refleksi pada output
    c.processor.brand = "AMD Ryzen"
    c.processor.speed = 4.2
    c.memory.capacity = 64
    c.memory.memory_type = "DDR5X"

    expected = (
        "Processor Brand: AMD Ryzen, Kecepatan: 4.2, "
        "Memory Kapasitas: 64, Tipe: DDR5X"
    )
    assert c.get_info() == expected

def test_processor_speed_negative_allowed_and_reflected():
    p = Processor("Intel", -3.0)   # implementasi sekarang tidak melarang negatif
    assert p.speed == -3.0
    # dipakai di Computer.get_info
    c = Computer(p, Memory(8, "DDR4"))
    assert "Kecepatan: -3.0" in c.get_info()


def test_processor_speed_zero_and_large_value():
    p0 = Processor("AMD", 0.0)
    assert p0.speed == 0.0

    p_big = Processor("AMD", 12.75)  # nilai besar/pecahan
    assert p_big.speed == 12.75


def test_processor_speed_invalid_raises_value_error():
    with pytest.raises(ValueError):
        Processor("Intel", "na")  # float("na") -> ValueError

    p = Processor("Intel", 3.0)
    with pytest.raises(ValueError):
        p.speed = "x.y"  # setter float() gagal


def test_memory_capacity_zero_and_negative():
    m0 = Memory(0, "DDR5")
    assert m0.capacity == 0

    mneg = Memory(-16, "DDR4")  # implementasi sekarang tidak melarang negatif
    assert mneg.capacity == -16


def test_memory_capacity_invalid_raises_value_error():
    with pytest.raises(ValueError):
        Memory("enam belas", "DDR5")  # int("enam belas") -> ValueError

    m = Memory(8, "DDR4")
    with pytest.raises(ValueError):
        m.capacity = "delapan"  # setter int() gagal


def test_strings_trim_and_allow_empty_brand_model_types():
    p = Processor("   Intel   ", 3.1)
    m = Memory(16, "   DDR5  ")
    assert p.brand == "Intel"
    assert m.memory_type == "DDR5"

    # string kosong tetap diperbolehkan (dipangkas menjadi "")
    p.brand = "   "
    m.memory_type = "   "
    assert p.brand == ""
    assert m.memory_type == ""


def test_computer_get_info_with_zero_values():
    c = Computer(Processor("", 0.0), Memory(0, ""))
    assert c.get_info() == (
        "Processor Brand: , Kecepatan: 0.0, "
        "Memory Kapasitas: 0, Tipe: "
    )


def test_computer_reassign_components_with_valid_instances():
    c = Computer(Processor("Intel", 3.0), Memory(8, "DDR4"))
    c.processor = Processor("AMD", 4.5)   # valid reassignment
    c.memory = Memory(32, "DDR5")
    assert c.processor.brand == "AMD"
    assert c.processor.speed == 4.5
    assert c.memory.capacity == 32
    assert c.memory.memory_type == "DDR5"