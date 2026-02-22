import pytest
from invoicing.invoice import Invoice


def test_invoice_constructor_and_properties():
    inv = Invoice("PN-001", "Keyboard", 2, 150000.0)
    assert inv.part_number == "PN-001"
    assert inv.part_description == "Keyboard"
    assert inv.quantity == 2
    assert inv.price == 150000.0
    assert inv.get_invoice_amount() == 300000.0


def test_invoice_quantity_negative_becomes_zero():
    inv = Invoice("PN-002", "Mouse", -5, 50000.0)
    assert inv.quantity == 0
    assert inv.get_invoice_amount() == 0.0  # 0 * price


def test_invoice_price_negative_becomes_zero():
    inv = Invoice("PN-003", "Cable", 3, -10000.0)
    assert inv.price == 0.0
    assert inv.get_invoice_amount() == 0.0  # quantity * 0.0


def test_invoice_setters_validate_after_init():
    inv = Invoice("PN-004", "Headset", 1, 250000.0)
    inv.quantity = -1
    inv.price = -5.0
    assert inv.quantity == 0
    assert inv.price == 0.0
    assert inv.get_invoice_amount() == 0.0
