import pytest
from banking.bank_account import BankAccount


def test_bank_account_constructor_and_validation():
    acc = BankAccount("", None, -500.0)  # kosong/None -> "Unknown", saldo negatif -> 0.0
    assert acc.account_number == "Unknown"
    assert acc.account_holder == "Unknown"
    assert acc.get_balance() == 0.0


def test_deposit_and_withdraw_rules():
    acc = BankAccount("ACC-001", "Rizky", 1000.0)

    # deposit negatif -> abaikan
    acc.deposit(-50.0)
    assert acc.get_balance() == 1000.0

    # deposit valid
    acc.deposit(250.0)
    assert acc.get_balance() == 1250.0

    # withdraw negatif -> abaikan
    acc.withdraw(-10.0)
    assert acc.get_balance() == 1250.0

    # withdraw melebihi saldo -> abaikan
    acc.withdraw(1300.0)
    assert acc.get_balance() == 1250.0

    # withdraw valid
    acc.withdraw(200.0)
    assert acc.get_balance() == 1050.0


def test_account_number_and_holder_normalization():
    acc = BankAccount("   ", "   ", 0.0)
    # setter akan trim dan karena kosong -> "Unknown"
    assert acc.account_number == "Unknown"
    assert acc.account_holder == "Unknown"
