website = {
    "name": "COMFY",
    "url": "https://comfy.ua",
    "url_structure": "Зрозуміла та ієрархічна",
    "sitemap": "Наявний (sitemap.xml)",
    "robots": "Наявний (robots.txt)",
    "page_speed": "Висока",
    "mobile_friendly": "Так"
}

print("ТЕХНІЧНИЙ АНАЛІЗ ВЕБСАЙТУ COMFY")
print("-" * 50)

for key, value in website.items():
    print(f"{key:<20}: {value}")