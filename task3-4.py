def count_colon_elements(text: str) -> int:
    """
    Повертає кількість елементів, розділених символом ':'
    """
    if not text:
        return 0

    return len(text.split(":"))


if __name__ == "__main__":
    user_input = input("Введіть рядок: ")

    result = count_colon_elements(user_input)

    print("Вхідний рядок:", user_input)
    print("Кількість елементів:", result)