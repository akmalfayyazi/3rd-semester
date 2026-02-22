class Date:
    def __init__(self, month, day, year):
        try:
            month = int(month)
            day = int(day)
            year = int(year)
        except (TypeError, ValueError):
            month, day, year = 1, 1, 1970
            
        if 1 <= month <= 12 and 1 <= day <= 31:
            self._day = day
            self._month = month
            self._year = year
        else:
            self._day = 1
            self._month = 1
            self._year = 1970

    @property
    def day(self):
        return self._day

    @property
    def month(self):
        return self._month

    @property
    def year(self):
        return self._year
    
    def display_date(self):
        return f'{self.month}/{self.day}/{self.year}'
    
if __name__ == '__main__':
    date1 = Date(12, 30, 2024)
    print(date1.display_date())