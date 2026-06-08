site = {
    "name": "COMFY",
    "url": "https://comfy.ua",
    "topic": "Online electronics and appliances store",
    "type": "E-commerce",
    "audience": [
        "individuals",
        "families",
        "students",
        "businesses"
    ],
    "purpose": "Online sales of electronics, appliances, gadgets and accessories",
    "categories": [
        "Smartphones",
        "Laptops",
        "Televisions",
        "Home Appliances",
        "Gaming",
        "Audio",
        "Smart Home",
        "Accessories"
    ]
}

print("Характеристика вебсайту COMFY")
print("-" * 50)

for key, value in site.items():
    if isinstance(value, list):
        value = ", ".join(value)
    print(f"{key:<12}: {value}")