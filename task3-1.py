def print_language_analysis():
    data = [
        {
            "language": "Python",
            "paradigm": "Мультипарадигмова (об'єктно-орієнтована, процедурна, функціональна)",
            "typing": "Динамічна, сильна типізація",
            "usage": "Веб-розробка, Data Science, автоматизація, AI/ML"
        },
        {
            "language": "Java",
            "paradigm": "Об'єктно-орієнтована (з елементами процедурної)",
            "typing": "Статична, сильна типізація",
            "usage": "Корпоративні системи, Android-розробка, серверні застосунки"
        },
        {
            "language": "Haskell",
            "paradigm": "Функціональна",
            "typing": "Статична, сильна, з виведенням типів",
            "usage": "Наукові обчислення, фінансові системи, дослідження мов програмування"
        }
    ]

    print("АНАЛІТИЧНИЙ ОПИС МОВ ПРОГРАМУВАННЯ\n")

    for item in data:
        print(f"Мова: {item['language']}")
        print(f"Парадигма: {item['paradigm']}")
        print(f"Типізація: {item['typing']}")
        print(f"Застосування: {item['usage']}")
        print("-" * 50)


if __name__ == "__main__":
    print_language_analysis()