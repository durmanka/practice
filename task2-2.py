def search_dictionary(dictionary: list, word: str) -> str:
    left = 0
    right = len(dictionary) - 1

    while left <= right:
        middle = (left + right) // 2
        current_word = dictionary[middle][0]

        if current_word.lower() == word.lower():
            return dictionary[middle][1]
        elif current_word.lower() < word.lower():
            left = middle + 1
        else:
            right = middle - 1

    return "Слово не знайдено"


dictionary = [
    ("алгоритм", "Послідовність дій для розв'язання задачі"),
    ("браузер", "Програма для перегляду вебсторінок"),
    ("дані", "Відомості, представлені у формалізованому вигляді"),
    ("інтернет", "Глобальна комп'ютерна мережа"),
    ("сервер", "Комп'ютер або програма, що надає послуги клієнтам")
]

word = input("Введіть слово для пошуку: ")

result = search_dictionary(dictionary, word)

print(result)