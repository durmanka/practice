def sort_by_length(strings: list) -> list:
    """
    Повертає список рядків, відсортований за довжиною (зростанням)
    """
    return sorted(strings, key=len)


if __name__ == "__main__":
    user_input = input("Введіть рядки через кому: ")

    strings = [s.strip() for s in user_input.split(",")]

    result = sort_by_length(strings)

    print("Вхідні дані:", strings)
    print("Відсортований масив:", result)