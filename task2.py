def search_dictionary(dictionary, word):
    left = 0
    right = len(dictionary) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_word = dictionary[mid][0]

        if mid_word == word:
            return dictionary[mid][1]
        elif mid_word < word:
            left = mid + 1
        else:
            right = mid - 1

    return "Слово не знайдено"

dictionary = [
    ("алгоритм",   "послідовність інструкцій для вирішення задачі"),
    ("масив",      "список елементів одного типу"),
    ("рекурсія",   "виклик функцією самої себе"),
    ("функція",    "блок коду з іменем"),
    ("цикл",       "повторення блоку коду"),
]

print(search_dictionary(dictionary, "масив"))
print(search_dictionary(dictionary, "цикл"))
print(search_dictionary(dictionary, "хмара"))