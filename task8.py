class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def is_palindrome(phrase):
    deque = Deque()

    for char in phrase.lower():
        if char.isalpha() or char.isdigit():
            deque.add_rear(char)

    while deque.size() > 1:
        if deque.remove_front() != deque.remove_rear():
            return False

    return True

phrases = [
    "Пили лип",
    "А роза упала на лапу Азора",
    "racecar",
    "Never odd or even",
    "Привіт",
    "Was it a car or a cat I saw",
    "Python",
]

print("Перевірка паліндромів:")
print("-" * 45)

for phrase in phrases:
    result = is_palindrome(phrase)
    mark = "✓" if result else "✗"
    print(f"  {mark} '{phrase}'")