def process_order(order_id: int, items: list, stock: dict, balance: float, prices: dict):
    """
    Обробка замовлення:
    - перевірка наявності товарів
    - перевірка балансу
    - розрахунок суми
    """

    total = 0

    # перевірка наявності товарів
    for item in items:
        if item not in stock or stock[item] <= 0:
            return f"Замовлення {order_id}: товар '{item}' відсутній"

        total += prices[item]

    # перевірка балансу
    if balance < total:
        return f"Замовлення {order_id}: недостатньо коштів"

    # списання товарів зі складу
    for item in items:
        stock[item] -= 1

    balance -= total

    return f"Замовлення {order_id}: успішно оброблено, сума = {total}"


if __name__ == "__main__":
    stock_data = {"phone": 5, "headphones": 2, "charger": 0}
    price_data = {"phone": 500, "headphones": 80, "charger": 20}

    result = process_order(
        order_id=1,
        items=["phone", "headphones"],
        stock=stock_data,
        balance=1000,
        prices=price_data
    )

    print(result)