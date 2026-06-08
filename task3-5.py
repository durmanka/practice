def count_even_numbers(numbers: list) -> int:
    """
    Повертає кількість парних чисел у списку
    """
    count = 0

    for num in numbers:
        if num % 2 == 0:
            count += 1

    return count


if __name__ == "__main__":
    user_input = input("Введіть числа через пробіл: ")

    numbers = list(map(int, user_input.split()))

    result = count_even_numbers(numbers)

    print("Вхідні дані:", numbers)
    print("Кількість парних чисел:", result)