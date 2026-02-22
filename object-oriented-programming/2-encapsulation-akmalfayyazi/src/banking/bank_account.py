class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self._account_number = account_number.strip() if account_number and account_number.strip() else 'Unknown'
        self._account_holder = account_holder.strip() if account_holder and account_holder.strip() else 'Unknown'
        self._balance = max(0, balance)

    @property
    def account_number(self):
        return self._account_number
    
    @property
    def account_holder(self):
        return self._account_holder
        
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        self._balance = value

    def deposit(self, amount: float):
        amount = max(0, amount)
        self.balance += amount
    
    def withdraw(self, amount: float):
        if amount >= 0 and amount < self.balance:
            self.balance -= amount
        else:
            None
    
    def get_balance(self):
        return self.balance
    
if __name__ == '__main__':
    account1 = BankAccount(' ', 'Krisna', 250000)
    account1.deposit(250000)
    print(account1.account_number)
    print(account1.get_balance())