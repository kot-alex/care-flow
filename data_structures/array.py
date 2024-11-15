class Array:
    def __init__(self):
        self.array = []

    def append(self, item):
        self.array.append(item)

    def insert(self, index, item):
        self.array.insert(index, item)

    def remove(self, item):
        if item in self.array:
            self.array.remove(item)

    def pop(self, index=None):
        if index is not None and 0 <= index < len(self.array):
            return self.array.pop(index)
        elif index is None:
            return self.array.pop()
        return None

    def get(self, index):
        if 0 <= index < len(self.array):
            return self.array[index]
        return None

    def set(self, index, item):
        if 0 <= index < len(self.array):
            self.array[index] = item

    def size(self):
        return len(self.array)

    def is_empty(self):
        return len(self.array) == 0
