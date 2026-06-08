website = {
    "name": "COMFY",
    "domain": "comfy.ua",
    "search_engine": "Google",
    "indexed": True,
    "pages": [
        "https://comfy.ua/",
        "https://comfy.ua/ua/smartfon.html",
        "https://comfy.ua/ua/noutbuk.html",
        "https://comfy.ua/ua/televizory.html",
        "https://comfy.ua/ua/holodilniki.html"
    ]
}

print("АНАЛІЗ ІНДЕКСАЦІЇ ВЕБСАЙТУ")
print("-" * 50)
print(f"Назва сайту: {website['name']}")
print(f"Домен: {website['domain']}")
print(f"Пошукова система: {website['search_engine']}")
print(f"Факт індексації: {'Так' if website['indexed'] else 'Ні'}")

print("\nСторінки, знайдені у пошуковій видачі Google:")
for i, page in enumerate(website["pages"], start=1):
    print(f"{i}. {page}")