import pytest
from vehicles.kendaraan import Kendaraan, Mobil, Motor


def test_kendaraan_get_only_properties_and_info(capsys: pytest.CaptureFixture):
    k = Kendaraan("Toyota", "Avanza")
    assert k.merk == "Toyota"
    assert k.model == "Avanza"

    k.tampilkan_info()
    out = capsys.readouterr().out
    assert out == "Kendaraan - Merk: Toyota, Model: Avanza\n"


def test_mobil_inheritance_and_output(capsys: pytest.CaptureFixture):
    m = Mobil("Toyota", "Camry", "Sedan")
    assert m.merk == "Toyota"
    assert m.model == "Camry"
    assert m.tipe_bodi == "Sedan"

    m.tampilkan_info()
    out = capsys.readouterr().out
    assert out == "Mobil - Merk: Toyota, Model: Camry, Tipe Bodi: Sedan\n"


def test_motor_inheritance_and_output(capsys: pytest.CaptureFixture):
    mt = Motor("Honda", "CBR150R", "4 Stroke")
    assert mt.merk == "Honda"
    assert mt.model == "CBR150R"
    assert mt.tipe_mesin == "4 Stroke"

    mt.tampilkan_info()
    out = capsys.readouterr().out
    assert out == "Motor - Merk: Honda, Model: CBR150R, Tipe Mesin: 4 Stroke\n"
