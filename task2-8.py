class Deque:
    def __init__(self):
        self.data = []

    def add_front(self, item):
        self.data.insert(0, item)

    def add_rear(self, item):
        self.data.append(item)

    def remove_front(self):
        if self.is_empty():
            return None
        return self.data.pop(0)

    def remove_rear(self):
        if self.is_empty():
            return None
        return self.data.pop()

    def is_empty(self):
        return len(self.data) == 0


def is_palindrome(phrase: str) -> bool:
    cleaned = []

    for char in phrase:
        if char.isalnum():
            cleaned.append(char.lower())

    dq = Deque()

    for ch in cleaned:
        dq.add_rear(ch)

    while not dq.is_empty() and len(dq.data) > 1:
        front = dq.remove_front()
        rear = dq.remove_rear()

        if front != rear:
            return False

    return True


if __name__ == "__main__":
    tests = [
        "A man a plan a canal Panama",
        "racecar",
        "hello",
        "Was it a car or a cat I saw",
        "Python"
    ]

    for t in tests:
        print(t, "->", is_palindrome(t))