class PhoneBook:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.size = 0
        self.table = [[] for _ in range(capacity)]

    def _hash(self, key: str) -> int:
        hash_value = 0
        prime = 31

        for char in key:
            hash_value = (hash_value * prime + ord(char)) % self.capacity

        return hash_value

    def _resize(self):
        old_table = self.table
        self.capacity *= 2
        self.table = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_table:
            for key, value in bucket:
                self.add(key, value)

    def _load_factor(self):
        return self.size / self.capacity

    def add(self, name: str, phone: str) -> None:
        if self._load_factor() > 0.75:
            self._resize()

        index = self._hash(name)

        for i, (k, v) in enumerate(self.table[index]):
            if k == name:
                self.table[index][i] = (name, phone)
                return

        self.table[index].append((name, phone))
        self.size += 1

    def get(self, name: str):
        index = self._hash(name)

        for k, v in self.table[index]:
            if k == name:
                return v
        return None

    def delete(self, name: str) -> bool:
        index = self._hash(name)

        for i, (k, v) in enumerate(self.table[index]):
            if k == name:
                del self.table[index][i]
                self.size -= 1
                return True

        return False

    def contains(self, name: str) -> bool:
        return self.get(name) is not None

    def count(self) -> int:
        return self.size