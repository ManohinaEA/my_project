class BankAccount:
    _accounts = []
    _id_counter = 1

    def __init__(self, owner_name, initial_balance=0):
        self.owner_name = owner_name
        self.balance = initial_balance
        self.account_number = BankAccount._id_counter
        BankAccount._id_counter += 1
        self._history = [f"Счёт создан. Баланс: {initial_balance}"]
        BankAccount._accounts.append(self)

    def deposit(self, amount):
        if amount > 50000:
            msg = f"Ошибка: максимальная сумма пополнения 50000"
            print(msg)
            self._history.append(msg)
            return False
        if amount <= 0:
            msg = f"Ошибка: сумма пополнения должна быть положительной"
            print(msg)
            self._history.append(msg)
            return False
        self.balance += amount
        msg = f"Пополнение на {amount}. Баланс {self.balance}"
        print(msg)
        self._history.append(msg)
        return True

    def withdraw(self, amount):
        if amount > 50000:
            msg = f"Ошибка: максимальная сумма снятия 50000"
            print(msg)
            self._history.append(msg)
            return False
        if amount <= 0:
            msg = f"Ошибка: сумма снятия должна быть положительной"
            print(msg)
            self._history.append(msg)
            return False
        if amount > self.balance:
            msg = f"Ошибка: недостаточно средств. Баланс {self.balance}"
            print(msg)
            self._history.append(msg)
            return False
        self.balance -= amount
        msg = f"Снятие {amount}. Баланс {self.balance}"
        print(msg)
        self._history.append(msg)
        return True

    def get_owner_info(self):
        print(f"Владелец: {self.owner_name}")
        print(f"Номер счета: {self.account_number}")
        print(f"Баланс: {self.balance}")

    def transfer(self, target_account, amount):
        if amount > 20000:
            msg = f"Ошибка: максимальная сумма перевода 20000"
            print(msg)
            self._history.append(msg)
            return False
        if amount <= 0:
            msg = f"Ошибка: сумма перевода должна быть положительной"
            print(msg)
            self._history.append(msg)
            return False
        if amount > self.balance:
            msg = f"Ошибка: недостаточно средств для перевода"
            print(msg)
            self._history.append(msg)
            return False
        self.balance -= amount
        target_account.balance += amount
        msg = f"Перевод {amount} со счета {self.account_number} на счет {target_account.account_number}"
        print(msg)
        self._history.append(msg)
        target_account._history.append(f"Поступление {amount} со счета {self.account_number}. Баланс {target_account.balance}")
        print(f"Баланс отправителя: {self.balance}")
        print(f"Баланс получателя: {target_account.balance}")
        return True

    def get_account_info(self):
        print(f"Счет #{self.account_number}")
        print(f"Владелец: {self.owner_name}")
        print(f"Баланс: {self.balance}")

    def get_history(self):
        print(f"История операций по счету #{self.account_number} ({self.owner_name}):")
        for i, record in enumerate(self._history, 1):
            print(f" {i}. {record}")

    @classmethod
    def get_all_accounts(cls):
        if not cls._accounts:
            print("Список счетов пуст")
            return
        print("Список всех счетов:")
        for acc in cls._accounts:
            print(f" Счет #{acc.account_number}: {acc.owner_name} - {acc.balance}")

    @classmethod
    def find_account(cls, account_number):
        for acc in cls._accounts:
            if acc.account_number == account_number:
                return acc
        print(f"Счет #{account_number} не найден")
        return None

    @classmethod
    def bank_transfer(cls, from_number, to_number, amount):
        from_account = cls.find_account(from_number)
        to_account = cls.find_account(to_number)
        if from_account is None or to_account is None:
            return False
        return from_account.transfer(to_account, amount)


def main():
    print("=== Демонстрация работы банковских счетов ===\n")
    
    acc1 = BankAccount("Иванов Иван Иванович", 100000)
    acc2 = BankAccount("Петрова Мария Сергеевна", 50000)
    acc3 = BankAccount("Сидоров Алексей Петрович", 30000)
    
    print("Информация о владельце acc1:")
    acc1.get_owner_info()
    print()
    
    acc1.deposit(30000)
    acc1.withdraw(20000)
    print()
    
    print("Перевод 15000 с acc1 на acc2:")
    acc1.transfer(acc2, 15000)
    print()
    
    print("Поиск счета по номеру 3:")
    found = BankAccount.find_account(3)
    if found:
        found.get_account_info()
    print()
    
    print("Банковский перевод со счета 2 на счет 3 (5000):")
    BankAccount.bank_transfer(2, 3, 5000)
    print()
    
    print("Информация о счете acc3:")
    acc3.get_account_info()
    print()
    
    print("История операций acc1:")
    acc1.get_history()
    print()
    
    BankAccount.get_all_accounts()


if __name__ == "__main__":
    main()
