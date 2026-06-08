def check_password(input_password: str, correct_password: str) -> bool:
    """
    Перевіряє правильність пароля
    """
    return input_password == correct_password


def password_system(correct_password: str, max_attempts: int = 3):
    """
    Система введення пароля з обмеженням спроб
    """
    attempts = 0

    while attempts < max_attempts:
        user_input = input("Введіть пароль: ")

        if check_password(user_input, correct_password):
            print("Доступ дозволено")
            return True
        else:
            attempts += 1
            print(f"Невірний пароль. Спроба {attempts} з {max_attempts}")

    print("Доступ заблоковано")
    return False


if __name__ == "__main__":
    password_system(correct_password="1234")