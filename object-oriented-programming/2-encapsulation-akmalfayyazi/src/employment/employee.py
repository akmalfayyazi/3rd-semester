class Employee:
    def __init__(self, first_name, last_name, monthly_salary):
        self._first_name = first_name if first_name else 'Unknown'
        self._last_name = last_name if last_name else 'Unknown'
        self._monthly_salary = max(0, monthly_salary)
    
    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name

    @property
    def monthly_salary(self):
        return self._monthly_salary
    
    @monthly_salary.setter
    def monthly_salary(self, value):
        if value > 0:  # boleh 0 tapi tidak negatif
            self._monthly_salary = value
    
    def raise_salary(self, raise_percentage: int):
        if raise_percentage <= 0 or raise_percentage > 20:
            return
        self._monthly_salary += self._monthly_salary * (raise_percentage / 100)

    def get_yearly_salary(self) -> float:
        return self._monthly_salary * 12


if __name__ == '__main__':
    e = Employee("Bob", "Wijaya", 2_000_000)
    print(e.monthly_salary)  # 2000000
    e.raise_salary(10)
    print(e.monthly_salary)  # 2200000
    e.raise_salary(21)
    print(e.monthly_salary)  # 2640000, karena maksimal raise 20%
