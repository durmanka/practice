def merge_orders(web_orders: list, app_orders: list) -> list:
    i, j = 0, 0
    merged = []

    while i < len(web_orders) and j < len(app_orders):
        if web_orders[i]["time"] <= app_orders[j]["time"]:
            merged.append(web_orders[i])
            i += 1
        else:
            merged.append(app_orders[j])
            j += 1

    while i < len(web_orders):
        merged.append(web_orders[i])
        i += 1

    while j < len(app_orders):
        merged.append(app_orders[j])
        j += 1

    return merged


if __name__ == "__main__":
    web_orders = [
        {"id": 1, "time": 10},
        {"id": 3, "time": 25},
        {"id": 5, "time": 40},
    ]

    app_orders = [
        {"id": 2, "time": 15},
        {"id": 4, "time": 30},
        {"id": 6, "time": 50},
    ]

    result = merge_orders(web_orders, app_orders)

    for order in result:
        print(order)