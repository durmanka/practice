def reverse_string(text: str) -> str:
    """
    Приймає рядок, зберігає його та повертає у зворотному порядку
    """
    return text[::-1]


if __name__ == "__main__":
    user_input = input("Введіть рядок: ")

    reversed_text = reverse_string(user_input)

    print("Початковий рядок:", user_input)
    print("Зворотний рядок:", reversed_text)