class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for idx, (k, v) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][idx] = (key, value)
                    return
            self.table[index].append((key, value))

    def search(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

    def delete(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for idx, (k, v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][idx]
                    return True
        return False

    def resize(self):
        new_size = self.size * 2
        new_table = [None] * new_size
        for bucket in self.table:
            if bucket:
                for key, value in bucket:
                    index = hash(key) % new_size
                    if new_table[index] is None:
                        new_table[index] = [(key, value)]
                    else:
                        new_table[index].append((key, value))
        self.size = new_size
        self.table = new_table

    def get(self, key):
        index = self._hash(key)
        return self.table[index]
