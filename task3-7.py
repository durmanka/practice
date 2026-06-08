def filter_long_strings(strings: list) -> list:
    """
    Повертає список рядків, довжина яких > 3 символів
    """
    result = []

    for s in strings:
        if len(s) > 3:
            result.append(s)

    return result


if __name__ == "__main__":
    user_input = input("Введіть рядки через кому: ")

    strings = [s.strip() for s in user_input.split(",")]

    filtered = filter_long_strings(strings)

    print("Вхідні дані:", strings)
    print("Відфільтрований масив:", filtered)