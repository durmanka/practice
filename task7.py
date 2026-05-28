class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class PhoneBook:
    def __init__(self):
        self.capacity = 8
        self.size = 0
        self.table = [None] * self.capacity

    def _hash(self, key):
        result = 0
        for char in key:
            result = result * 31 + ord(char)
        return result % self.capacity

    def _resize(self):
        old_table = self.table
        self.capacity = self.capacity * 2
        self.table = [None] * self.capacity
        self.size = 0

        for node in old_table:
            current = node
            while current is not None:
                self.add(current.key, current.value)
                current = current.next

    def add(self, name, phone):
        if self.size / self.capacity > 0.75:
            self._resize()

        index = self._hash(name)
        current = self.table[index]

        while current is not None:
            if current.key == name:
                current.value = phone
                return
            current = current.next

        new_node = Node(name, phone)
        new_node.next = self.table[index]
        self.table[index] = new_node
        self.size += 1

    def get(self, name):
        index = self._hash(name)
        current = self.table[index]

        while current is not None:
            if current.key == name:
                return current.value
            current = current.next

        return "Контакт не знайдено"

    def remove(self, name):
        index = self._hash(name)
        current = self.table[index]
        prev = None

        while current is not None:
            if current.key == name:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return True
            prev = current
            current = current.next

        return False

    def contains(self, name):
        index = self._hash(name)
        current = self.table[index]

        while current is not None:
            if current.key == name:
                return True
            current = current.next

        return False

    def count(self):
        return self.size

    def show(self):
        print(f"Довідник ({self.size} контактів):")
        for i in range(self.capacity):
            current = self.table[i]
            while current is not None:
                print(f"  {current.key}: {current.value}")
                current = current.next

pb = PhoneBook()

pb.add("Олег",    "+380991234567")
pb.add("Марія",   "+380992345678")
pb.add("Іван",    "+380993456789")
pb.add("Софія",   "+380994567890")
pb.add("Дмитро",  "+380995678901")
pb.add("Анна",    "+380996789012")
pb.add("Микола",  "+380997890123")

print("--- Додавання ---")
pb.show()

print("\n--- Отримання ---")
print(f"Олег:   {pb.get('Олег')}")
print(f"Марія:  {pb.get('Марія')}")
print(f"Хтось:  {pb.get('Хтось')}")

print("\n--- Оновлення ---")
pb.add("Олег", "+380990000000")
print(f"Олег після оновлення: {pb.get('Олег')}")

print("\n--- Перевірка наявності ---")
print(f"Містить 'Іван':  {pb.contains('Іван')}")
print(f"Містить 'Петро': {pb.contains('Петро')}")

print("\n--- Видалення ---")
pb.remove("Дмитро")
print(f"Після видалення Дмитра: {pb.contains('Дмитро')}")
print(f"Кількість контактів: {pb.count()}")

print("\n--- Автоматичне розширення ---")
print(f"Ємність до: {pb.capacity}")
pb.add("Петро",   "+380991111111")
pb.add("Галина",  "+380992222222")
print(f"Ємність після: {pb.capacity}")