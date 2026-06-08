def find_product(products: list, target: str) -> int:
    for i in range(len(products)):
        if products[i].lower() == target.lower():
            return i + 1  # індексація з 1
    return -1


products = [
    "iPhone 15",
    "Samsung Galaxy S25",
    "Xiaomi Redmi Note 14",
    "Lenovo IdeaPad",
    "Apple Watch Series 10"
]

target = input("Введіть назву товару: ")

result = find_product(products, target)

if result != -1:
    print(f"Товар знайдено на позиції {result}")
else:
    print("Товар не знайдено")