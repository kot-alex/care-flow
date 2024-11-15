## Array

### Design Principles

An **Array** is a collection of elements stored in contiguous memory locations. It allows random access to elements and is efficient for accessing, adding, or removing elements at known indices. Arrays are used in scenarios where fast access to elements by index is required, like in sorting algorithms, searching, and storing sequential data.

### Functionalities

- **append(item)**: Adds an item to the end of the array.
- **insert(index, item)**: Inserts an item at a specified index.
- **remove(item)**: Removes the first occurrence of the item from the array.
- **pop(index=None)**: Removes and returns the element at the specified index. If no index is specified, it removes the last item.
- **get(index)**: Returns the item at the specified index.
- **set(index, item)**: Sets the value of the item at the specified index.
- **size()**: Returns the number of elements in the array.
- **is_empty()**: Returns `True` if the array is empty.

### Time and Space Complexity

- **append(item)**: O(1)
- **insert(index, item)**: O(n)
- **remove(item)**: O(n)
- **pop(index)**: O(n) if specific index; O(1) for last element
- **get(index)**: O(1)
- **set(index, item)**: O(1)
- **size()**: O(1)

- **Space Complexity**: O(n), where `n` is the number of elements in the array.

### Usage Example

```python
arr = Array()
arr.append(10)
arr.append(20)
arr.insert(1, 15)

print(arr.get(1))  # 15
arr.remove(15)
print(arr.size())  # 2
print(arr.pop())   # 20
```

## Stack

### Design Principles

A **Stack** follows the **LIFO (Last In, First Out)** principle, where the last element added is the first to be removed. Common use cases include undo mechanisms, expression evaluation, and function call management.

### Functionalities

- **push(item)**: Adds item to the top.
- **pop()**: Removes and returns the top item.
- **peek()**: Returns the top item without removing it.
- **is_empty()**: Returns `True` if empty.
- **size()**: Returns the number of elements.

### Time and Space Complexity

- **push(item)**: O(1)
- **pop()**: O(1)
- **peek()**: O(1)
- **is_empty()**: O(1)
- **size()**: O(1)

- **Space Complexity**: O(n), where `n` is the number of elements in the stack.

### Usage Example

```python
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek())  # 30
print(stack.pop())   # 30
print(stack.size())  # 2
```

## Queue

### Design Principles

A **Queue** follows the **FIFO (First In, First Out)** principle, where the first element added is the first to be removed. Common use cases include task scheduling, handling requests in web servers, and managing buffers in streaming data.

### Functionalities

- **enqueue(item)**: Adds item to the end.
- **dequeue()**: Removes and returns the front item.
- **peek()**: Returns the front item without removing it.
- **is_empty()**: Returns `True` if empty.
- **size()**: Returns the number of elements.

### Time and Space Complexity

- **enqueue(item)**: O(1)
- **dequeue()**: O(n)
- **peek()**: O(1)
- **is_empty()**: O(1)
- **size()**: O(1)

- **Space Complexity**: O(n), where `n` is the number of elements in the queue.

### Usage Example

```python
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)

print(queue.peek())  # 10
print(queue.dequeue())  # 10
print(queue.size())  # 1
```

## Linked List

### Design Principles

A **Linked List** is a linear data structure where elements are stored in nodes. Each node contains two parts: data and a reference (or link) to the next node in the sequence. Linked lists are useful when frequent insertions and deletions are required because adding or removing elements doesn't require shifting other elements, unlike arrays.

### Functionalities

- **append(data)**: Adds a new node with the provided data to the end of the list.
- **insert(index, data)**: Inserts a new node with the provided data at the specified index.
- **remove(data)**: Removes the first occurrence of the node containing the specified data.
- **pop(index=None)**: Removes and returns the node at the specified index. If no index is provided, it removes the first node.
- **get(index)**: Returns the data of the node at the specified index.
- **set(index, data)**: Sets the data of the node at the specified index.
- **size()**: Returns the number of nodes in the list.
- **is_empty()**: Returns `True` if the list is empty.

### Time and Space Complexity

- **append(data)**: O(n)
- **insert(index, data)**: O(n)
- **remove(data)**: O(n)
- **pop(index)**: O(n)
- **get(index)**: O(n)
- **set(index, data)**: O(n)
- **size()**: O(n)
- **is_empty()**: O(1)

- **Space Complexity**: O(n), where `n` is the number of nodes in the list.

### Usage Example

```python
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.insert(1, 15)

print(ll.get(1))  # 15
ll.remove(15)
print(ll.size())  # 2
print(ll.pop())   # 20
```

## Binary Tree

### Design Principles

A **Binary Tree** is a hierarchical data structure where each node has at most two children, typically referred to as the left and right children. There is no ordering of nodes, which makes it useful for representing hierarchical relationships like file systems or organizational charts.

### Functionalities

- **insert(data)**: Adds a new node with the given data.
- **inorder_traversal(node)**: Traverses the tree in in-order (left, root, right).
- **preorder_traversal(node)**: Traverses the tree in pre-order (root, left, right).
- **postorder_traversal(node)**: Traverses the tree in post-order (left, right, root).
- **search(data)**: Searches for a node with the given data.
- **is_empty()**: Checks if the tree is empty.

### Time and Space Complexity

- **insert(data)**: O(n) - In the worst case (unbalanced tree), traversal could require visiting all nodes.
- **search(data)**: O(n) - Worst case for an unbalanced tree.
- **Traversal**: O(n) - All nodes must be visited.
- **Space Complexity**: O(n) - Space used is proportional to the number of nodes.

### Usage Example

```python
bt = BinaryTree()
bt.insert(5)
bt.insert(3)
bt.insert(8)
bt.inorder_traversal(bt.root)  # Output: 3 5 8
```

## Binary Search Tree (BST)

### Design Principles

A **Binary Search Tree (BST)** is a type of binary tree where for any node:

- All values in the left subtree are less than the node’s value.
- All values in the right subtree are greater than the node’s value.

This property allows efficient searching, insertion, and deletion operations, with an average time complexity of O(log n) in a balanced tree.

### Functionalities

- **insert(data)**: Inserts data while maintaining BST properties (left < node < right).
- **search(data)**: Searches for a node with the given data.
- **inorder_traversal(node)**: Traverses the tree in in-order (left, root, right).
- **is_empty()**: Checks if the tree is empty.

### Time and Space Complexity

- **insert(data)**: O(log n) - For a balanced tree, insertion is O(log n), but O(n) in the worst case (unbalanced tree).
- **search(data)**: O(log n) - In a balanced tree, searching is O(log n), but O(n) in the worst case (unbalanced tree).
- **Traversal**: O(n) - All nodes must be visited.
- **Space Complexity**: O(n) - Space used is proportional to the number of nodes.

### Usage Example

```python
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(20)
bst.insert(15)
bst.insert(30)

print(bst.search(15))  # True
print(bst.search(100))  # False
bst.inorder_traversal(bst.root)  # 5 10 15 20 30
```

## Balanced Binary Search Tree (AVL Tree)

### Design Principles

A **Balanced Binary Search Tree (AVL Tree)** is a self-balancing binary search tree where the difference between the heights of the left and right subtrees of any node (called the balance factor) is at most 1. This ensures that the tree remains balanced, providing O(log n) time complexity for search, insertion, and deletion operations.

The main property of an AVL Tree:

- For every node in the tree, the difference between the height of its left and right subtree is no more than 1.

### Functionalities

- **insert(data)**: Inserts data while maintaining the AVL properties and re-balancing the tree if necessary.
- **delete(data)**: Removes a node and re-balances the tree to maintain the AVL property.
- **search(data)**: Searches for a node with the given data.
- **inorder_traversal(node)**: Traverses the tree in in-order (left, root, right).
- **is_empty()**: Checks if the tree is empty.
- **rotate_left()**: Performs a left rotation to maintain balance.
- **rotate_right()**: Performs a right rotation to maintain balance.

### Time and Space Complexity

- **insert(data)**: O(log n) - Inserting in an AVL tree takes O(log n) time as the tree remains balanced.
- **delete(data)**: O(log n) - Deletion also takes O(log n) time since balancing operations (rotations) ensure the tree's height remains logarithmic.
- **search(data)**: O(log n) - Searching in a balanced AVL tree takes O(log n) time.
- **Traversal**: O(n) - All nodes must be visited in a traversal.
- **Space Complexity**: O(n) - Space used is proportional to the number of nodes.

## Hash Table

### Design Principles

A **Hash Table** is a data structure that stores key-value pairs. It uses a hash function to compute an index where the key-value pair will be stored. The efficiency of a hash table is driven by the hash function and the collision resolution technique used (e.g., chaining or open addressing).

- **Efficiency**: Offers constant-time average complexity for search, insert, and delete operations (O(1)) when the hash function is well-distributed and the table is not too full.
- **Collisions**: Occur when two keys hash to the same index. This is handled using techniques like **chaining** (linked list at each table index) or **open addressing** (finding another empty slot).

### Functionalities

- **insert(key, value)**: Inserts a key-value pair into the table. If the key already exists, it updates the value.
- **search(key)**: Searches for a value by key and returns the value if found.
- **delete(key)**: Deletes the key-value pair associated with the given key.
- **resize()**: Doubles the size of the hash table and rehashes all the elements when the load factor exceeds a threshold.

### Time and Space Complexity

- **insert(key, value)**: O(1) on average. In the worst case, when there are many collisions, it can degrade to O(n).
- **search(key)**: O(1) on average. In the worst case, due to collisions, it can degrade to O(n).
- **delete(key)**: O(1) on average. In the worst case, due to collisions, it can degrade to O(n).
- **resize()**: O(n), as it involves rehashing all existing elements.
- **Space Complexity**: O(n), where `n` is the number of elements in the table.

### Usage Example

```python
hash_table = HashTable()

# Inserting key-value pairs
hash_table.insert('name', 'Alice')
hash_table.insert('age', 25)
hash_table.insert('city', 'New York')

# Searching for a value by key
print(hash_table.search('name'))  # Output: Alice

# Deleting a key-value pair
hash_table.delete('city')

# Searching for the deleted key
print(hash_table.search('city'))  # Output: None
```

## Searching Algorithms

### Design Principles

**Linear Search** and **Binary Search** are two fundamental algorithms used to find an element in a collection:

1. **Linear Search**:

   - **Principle**: Scans each element in the list sequentially until the target element is found or the end is reached.
   - **Use Case**: Suitable for unsorted data or small datasets where simple implementation is preferred.

2. **Binary Search**:
   - **Principle**: Uses a divide-and-conquer approach to reduce the search space by half each time. Only works on sorted arrays.
   - **Use Case**: Efficient for large sorted datasets as it reduces time complexity from O(n) to O(log n).

### Functionalities

- **linear_search(arr, target)**: Returns the index of `target` in the array if found, else returns -1.
- **binary_search(arr, target)**: Returns the index of `target` in the sorted array if found, else returns -1.

### Time and Space Complexity

1. **Linear Search**:

   - **Time Complexity**: O(n) - Each element might need to be checked once.
   - **Space Complexity**: O(1) - No additional space used apart from input.

2. **Binary Search**:
   - **Time Complexity**: O(log n) - Reduces search space by half with each step.
   - **Space Complexity**: O(1) - No additional space used apart from input.

### Usage Example

```python
arr = [10, 20, 30, 40, 50]

# Linear Search
print(linear_search(arr, 30))  # Output: 2

# Binary Search (array must be sorted)
print(binary_search(arr, 30))  # Output: 2
```

## Sorting Algorithms

### Bubble Sort

- **Description**: Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
- **Complexity**:
  - **Time Complexity**: O(n²) in the worst and average case; O(n) when nearly sorted.
  - **Space Complexity**: O(1) (in-place sorting).

### Insertion Sort

- **Description**: Builds the sorted array one item at a time by repeatedly inserting the next unsorted item in its correct position.
- **Complexity**:
  - **Time Complexity**: O(n²) in the average and worst case; O(n) when nearly sorted.
  - **Space Complexity**: O(1) (in-place sorting).

### Merge Sort

- **Description**: A divide-and-conquer algorithm that splits the array in half, recursively sorts each half, and then merges them.
- **Complexity**:
  - **Time Complexity**: O(n log n) for all cases.
  - **Space Complexity**: O(n) for the auxiliary space used during merging.

### Usage Example

```python
arr = [64, 25, 12, 22, 11]

# Bubble Sort
sorted_arr = bubble_sort(arr.copy())
print("Bubble Sort Result:", sorted_arr)

# Insertion Sort
sorted_arr = insertion_sort(arr.copy())
print("Insertion Sort Result:", sorted_arr)

# Merge Sort
sorted_arr = merge_sort(arr.copy())
print("Merge Sort Result:", sorted_arr)
```

### Complexity Analysis

| Algorithm          | Average Time Complexity | Worst-Case Time Complexity | Space Complexity |
| ------------------ | ----------------------- | -------------------------- | ---------------- |
| **Bubble Sort**    | O(n²)                   | O(n²)                      | O(1)             |
| **Insertion Sort** | O(n²)                   | O(n²)                      | O(1)             |
| **Merge Sort**     | O(n log n)              | O(n log n)                 | O(n)             |

## Tree Traversal Algorithms

### Design Principles

Tree traversal refers to the process of visiting all nodes in a tree data structure in a specific order. The three most common types of tree traversal are:

- **In-Order Traversal**: Visits nodes in ascending order (left, root, right). It’s often used for binary search trees.
- **Pre-Order Traversal**: Visits nodes in the order (root, left, right). Useful for creating a copy of the tree.
- **Post-Order Traversal**: Visits nodes in the order (left, right, root). Often used for deleting a tree.

### Functionalities

- **in_order_traversal(node)**: Traverses the tree in-order.
- **pre_order_traversal(node)**: Traverses the tree pre-order.
- **post_order_traversal(node)**: Traverses the tree post-order.

### Time and Space Complexity

- **Time Complexity**: O(n) for all types of traversal, as each node is visited once.
- **Space Complexity**: O(h), where `h` is the height of the tree. In the worst case, this is O(n) for an unbalanced tree.

### Usage Example

```python
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("In-Order Traversal: ", end="")
TreeTraversal.in_order(root)  # Output: 4 2 5 1 3

print("\nPre-Order Traversal: ", end="")
TreeTraversal.pre_order(root)  # Output: 1 2 4 5 3

print("\nPost-Order Traversal: ", end="")
TreeTraversal.post_order(root)  # Output: 4 5 2 3 1
```

### Complexity Analysis

| Traversal Type | Time Complexity | Space Complexity |
| -------------- | --------------- | ---------------- |
| **In-Order**   | O(n)            | O(h)             |
| **Pre-Order**  | O(n)            | O(h)             |
| **Post-Order** | O(n)            | O(h)             |

Where `n` is the number of nodes in the tree and `h` is the height of the tree.
