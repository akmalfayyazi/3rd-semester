class Invoice:
    def __init__(self, part_number: str, part_description: str, quantity: int, price:float):
        self._part_number = part_number
        self._part_description = part_description
        self._quantity = max(0, quantity)
        self._price = max(0, price)

    @property
    def part_number(self):
        return self._part_number
    
    @part_number.setter
    def part_number(self, value):
        self._part_number = value

    @property
    def part_description(self):
        return self._part_description
    
    @part_description.setter
    def part_description(self, value):
        self._part_description = value

    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        if value < 0:
            self._quantity = 0
        else:
            self._quantity = value

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            self._price = 0
        else:
            self._price = value

    def get_invoice_amount(self) -> float:
        return self.quantity * self.price

if __name__ == '__main__':
    invoice = Invoice("001", "Screw", 10, 5.0)
    print(invoice.quantity)
    print(invoice.get_invoice_amount())