def find_product(products: list, target: str) -> int:
    for i in range(len(products)):
        if products[i] == target:
            return i + 1
    return -1

products = [
    "Ноутбук",
    "Смартфон",
    "Навушники",
    "Клавіатура",
    "Миша",
    "Монітор",
    "Веб-камера",
    "Принтер"
]

print("Товари в магазині:")
for i in range(len(products)):
    print(f"  {i + 1}. {products[i]}")

print()

search_queries = ["Миша", "Монітор", "Планшет", "Ноутбук"]

for query in search_queries:
    result = find_product(products, query)
    if result != -1:
        print(f'Пошук "{query}": знайдено на позиції {result}')
    else:
        print(f'Пошук "{query}": Товар не знайдено')