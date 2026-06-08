tools_analysis = {
    "Google PageSpeed Insights": {
        "performance": 88,
        "accessibility": 92,
        "best_practices": 95,
        "seo": 97
    },
    "Ahrefs": {
        "domain_rating": 74,
        "backlinks": "Велика кількість зовнішніх посилань",
        "organic_keywords": "Тисячі ключових запитів",
        "organic_traffic": "Високий рівень органічного трафіку"
    }
}

print("ІНСТРУМЕНТАЛЬНИЙ АНАЛІЗ ВЕБСАЙТУ COMFY")
print("-" * 60)

for tool, results in tools_analysis.items():
    print(f"\n{tool}:")
    for metric, value in results.items():
        print(f"  {metric}: {value}")