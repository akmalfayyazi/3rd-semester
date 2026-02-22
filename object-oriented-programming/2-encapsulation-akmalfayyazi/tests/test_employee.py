import pytest
from employment.employee import Employee


def test_employee_constructor_validation():
    e = Employee("", None, -1000.0)  # nama kosong/None -> "Unknown", salary negatif -> 0.0
    assert e.first_name == "Unknown"
    assert e.last_name == "Unknown"
    assert e.monthly_salary == 0.0


def test_employee_monthly_salary_setter_ignores_non_positive():
    e = Employee("Alice", "Santoso", 1_000_000)
    before = e.monthly_salary
    e.monthly_salary = 0
    assert e.monthly_salary == before
    e.monthly_salary = -500_000
    assert e.monthly_salary == before
    # valid set
    e.monthly_salary = 1_200_000
    assert e.monthly_salary == 1_200_000


def test_employee_raise_salary_max_20_percent_and_ignores_invalid():
    e = Employee("Bob", "Wijaya", 2_000_000)

    # valid 10%
    e.raise_salary(10)
    assert pytest.approx(e.monthly_salary, rel=1e-9) == 2_200_000.0

    # boundary 20% valid
    e.raise_salary(20)
    assert pytest.approx(e.monthly_salary, rel=1e-9) == 2_640_000.0  # 2.2M * 1.2

    # >20% ignored
    e.raise_salary(21)
    assert pytest.approx(e.monthly_salary, rel=1e-9) == 2_640_000.0

    # <=0 ignored
    e.raise_salary(0)
    e.raise_salary(-5)
    assert pytest.approx(e.monthly_salary, rel=1e-9) == 2_640_000.0


def test_employee_get_yearly_salary():
    e = Employee("Cara", "Lim", 3_000_000)
    assert e.get_yearly_salary() == 36_000_000.0
