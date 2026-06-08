website = {
    "theme": "Продаж побутової техніки та електроніки",
    "informational_queries": [
        "як вибрати ноутбук",
        "який смартфон купити",
        "найкращі телевізори 2026"
    ],
    "navigational_queries": [
        "COMFY",
        "COMFY офіційний сайт",
        "COMFY каталог товарів"
    ],
    "commercial_queries": [
        "купити ноутбук",
        "купити смартфон",
        "телевізор ціна",
        "холодильник COMFY"
    ]
}

print("СЕМАНТИЧНИЙ АНАЛІЗ ВЕБСАЙТУ COMFY")
print("-" * 50)

print(f"Основна тематика: {website['theme']}")

print("\nІнформаційні запити:")
for query in website["informational_queries"]:
    print(f"- {query}")

print("\nНавігаційні запити:")
for query in website["navigational_queries"]:
    print(f"- {query}")

print("\nКомерційні запити:")
for query in website["commercial_queries"]:
    print(f"- {query}")