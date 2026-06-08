def deposit(balance: float, amount: float) -> float:
    """
    Поповнення рахунку
    """
    if amount <= 0:
        print("Сума поповнення повинна бути більшою за 0")
        return balance

    balance += amount
    print(f"Рахунок поповнено на {amount}")
    return balance


def withdraw(balance: float, amount: float, limit: float) -> float:
    """
    Зняття коштів з урахуванням ліміту
    """
    if amount <= 0:
        print("Сума зняття повинна бути більшою за 0")
        return balance

    if amount > limit:
        print("Перевищено ліміт операції")
        return balance

    if amount > balance:
        print("Недостатньо коштів на рахунку")
        return balance

    balance -= amount
    print(f"Знято {amount}")
    return balance


def check_balance(balance: float):
    """
    Перевірка балансу
    """
    print(f"Поточний баланс: {balance}")


if __name__ == "__main__":
    balance = 1000
    limit = 500

    check_balance(balance)

    balance = deposit(balance, 200)
    balance = withdraw(balance, 300, limit)
    balance = withdraw(balance, 700, limit)

    check_balance(balance)