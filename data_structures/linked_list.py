class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def insert(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 0
        while current and count < index - 1:
            count += 1
            current = current.next
        if current is None:
            raise IndexError("Index out of range")
        new_node.next = current.next
        current.next = new_node

    def remove(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current is None:
            raise ValueError(f"{data} not found in the list")
        prev.next = current.next
        current = None

    def pop(self, index=None):
        if index is None:
            if self.head is None:
                raise IndexError("pop from empty list")
            popped = self.head
            self.head = self.head.next
            popped.next = None
            return popped.data
        current = self.head
        count = 0
        while current and count < index - 1:
            count += 1
            current = current.next
        if current is None or current.next is None:
            raise IndexError("Index out of range")
        popped = current.next
        current.next = popped.next
        popped.next = None
        return popped.data

    def get(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        raise IndexError("Index out of range")

    def set(self, index, data):
        current = self.head
        count = 0
        while current:
            if count == index:
                current.data = data
                return
            count += 1
            current = current.next
        raise IndexError("Index out of range")

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def to_list(self):
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        return result

    # Make LinkedList iterable by defining __iter__ and __next__ methods
    def __iter__(self):
        self._current = self.head
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration
        data = self._current.data
        self._current = self._current.next
        return data

    def is_empty(self):
        return self.head is None
