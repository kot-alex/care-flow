# Care Flow

The **Hospital Management System (HMS)** is a Python application designed to manage patient records efficiently using various data structures and algorithms. The system allows for adding, admitting, searching, sorting, and retrieving patient information. It integrates data structures such as **LinkedList**, **Queue**, **Stack**, **HashTable**, and **Binary Search Tree (BST)** to optimize patient data handling.

## Directory Structure

```
care-flow/
├── algorithms/
│ ├── searching.py               # Searching algorithms
│ ├── sorting.py                 # Sorting algorithms
│ └── tree_traversal.py          # Tree traversal algorithms
├── data_structures/
│ ├── array.py                   # Array implementation
│ ├── binary_tree.py             # Binary tree implementation
│ ├── hash_table.py              # Hash Table implementation
│ ├── linked_list.py             # Linked list implementation
│ ├── queue.py                   # Queue implementation
│ └── stack.py                   # Stack implementation
├── docs/
│ └── components_overview.md     # Overview of data structures and algorithms
├── models/
│ └── patient.py                 # Patient class
├── tests/
│ ├── test_array.py              # Unit tests for array operations
│ ├── test_binary_tree.py        # Unit tests for binary tree operations
│ ├── test_hash_table.py         # Unit tests for hash table operations
│ ├── test_queue.py              # Unit tests for queue operations
│ ├── test_searching.py          # Unit tests for searching algorithms
│ ├── test_sorting.py            # Unit tests for sorting algorithms
│ ├── test_stack.py              # Unit tests for stack operations
│ └── test_tree_traversal.py     # Unit tests for tree traversal algorithms
│
├── HMS.py                       # Hospital Management System implementation
├── README.md                    # Project description and instructions
├── requirements.txt             # Package dependencies
├── space_complexity.py          # Analyzes the space complexity of algorithms
└── time_complexity.py           # Analyzes the time complexity of algorithms
```

## Features

1. **Patient Data Management**:

   - **LinkedList**: Stores all patients for sequential access.
   - **Queue**: Manages admitted patients (first-in-first-out) for appointment scheduling.
   - **HashTable**: Stores and looks up patient records efficiently by their unique ID.
   - **Stack**: Keeps track of recently admitted patients (last-in-first-out).
   - **Binary Search Tree (BST)**: Enables efficient retrieval of patients by their ID.

2. **Patient Operations**:
   - **Add Patient**: Adds a new patient with a randomly generated ID to the LinkedList, HashTable, and BST.
   - **Admit Patient**: Admits a patient into the queue for appointment scheduling and the stack for quick access.
   - **Schedule Appointment**: Schedules an appointment for the first patient in the queue (FIFO).
   - **Search Patient by ID**: Searches for a patient using binary search on the sorted patient list.
   - **Display Patients**: Displays all patients sorted by their ID.
   - **Find Patient by ID**: Finds a patient in the HashTable using their ID.
   - **Recent Admitted Patients**: Displays the most recently admitted patients using the stack (LIFO).
   - **Sort Patients by Age (Bubble Sort)**: Sorts and displays patients by their age using Bubble Sort.
   - **Sort Patients by Age (Insertion Sort)**: Sorts and displays patients by their age using Insertion Sort.
   - **Search Patient by Name**: Searches for a patient by name using linear search.
   - **Get Patient from BST**: Retrieves a patient from the Binary Search Tree by ID.
   - **Traverse BST**: Traverses the Binary Search Tree in different orders (in-order, pre-order, post-order).

## Components

### Data Structures:

- **LinkedList**: Stores patient objects for sequential access.
- **Queue**: Manages admitted patients in a first-come-first-served manner for appointment scheduling.
- **Stack**: Tracks recently admitted patients for quick retrieval.
- **HashTable**: Provides fast lookup for patient records by patient ID.
- **Binary Search Tree (BST)**: Efficient storage and retrieval of patients by ID.

### Algorithms:

- **Searching**:
  - Binary Search for sorted patient lists.
  - Linear Search for patient names.
- **Sorting**:
  - Bubble Sort to sort patients by age.
  - Insertion Sort to sort patients by age.
- **Tree Traversal**:
  - Methods for **in-order**, **pre-order**, and **post-order** traversal of the Binary Search Tree.

### For a more detailed explanation of the data structures and algorithms, see the [Components Overview](docs/components_overview.md)

## Getting Started

**Set Up Environment**:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Example Usage

```python
hms = HospitalManagementSystem()

hms.add_patient("Alice", 30, "Flu")
hms.add_patient("Bob", 45, "Cough")
hms.add_patient("Charlie", 35, "Fever")

hms.admit_patient("David", 28, "Headache")
print()
hms.display_patients()  # Display all patients sorted by ID
print()
hms.sort_patients_by_age()  # Sort patients by age using bubble sort
print()
hms.sort_patients_insertion()  # Sort patients by age using insertion sort
print()
hms.search_patient(1001)  # Search for patient by ID
hms.find_patient_by_id(1002)  # Find patient by ID from the HashTable
print()
hms.schedule_appointment()  # Schedule appointment for first patient in queue
print()
hms.recent_admitted_patients()  # Display recent admitted patients (LIFO)
print()
hms.search_patient_by_name("Alice")  # Search patient by name
hms.get_patient_from_bst(1001)  # Search for patient in Binary Search Tree
print()
hms.traverse_bst()  # Traverse the Binary Search Tree
```

## `time_complexity.py` - Time Complexity Analysis

### Overview

This Python file is responsible for analyzing the **time complexity** of various algorithms used in the **Hospital Management System (HMS)**. It evaluates the performance of **sorting algorithms**, **searching algorithms**, and **tree traversal algorithms** by measuring their execution times. The goal is to identify how efficient these algorithms are when processing patient data.

### Key Functions

1. **`measure_time(func, *args, repetitions=1)`**:

   - This function measures the execution time of a given function (`func`) over a specified number of repetitions (default is 1). It calculates the average time taken to execute the function and returns it.
   - This helps to understand the time efficiency of algorithms in practice.

2. **`analyze_sorting_algorithms(hms)`**:

   - This function analyzes the performance of three sorting algorithms—**Bubble Sort**, **Insertion Sort**, and **Merge Sort**—on a list of patient ages extracted from the Hospital Management System (HMS).
   - It measures and prints the execution time of each sorting algorithm.

3. **`analyze_search_algorithms(hms)`**:

   - This function evaluates the performance of five different searching algorithms on patient data:
     - **Linear Search**: Used on a linked list of patients.
     - **Binary Search**: Used on a Binary Search Tree (BST) containing patient data.
     - **Jump Search**, **Interpolation Search**, and **Exponential Search**: Used on a sorted list of patients by ID.
   - It measures and prints the time taken for each search operation.

4. **`analyze_tree_traversal(bst)`**:

   - This function analyzes the time complexity of three tree traversal algorithms (**In-Order**, **Pre-Order**, and **Post-Order**) on a Binary Search Tree (BST).
   - It measures and prints the execution time of each traversal method.

5. **`main()`**:
   - This is the main driver function that generates a random dataset of patient ages and adds them to the HMS.
   - It then runs the analysis functions for sorting, searching, and tree traversal algorithms to evaluate their time complexities.

### Purpose

The purpose of this file is to assess and compare the efficiency of different algorithms in terms of execution time. This is especially useful for understanding how the HMS performs with larger datasets and for identifying potential areas for optimization.

### Why is this Important?

- **Optimization**: By analyzing the time complexity of algorithms, you can make informed decisions about which algorithms are most suitable for large datasets.
- **Performance Evaluation**: Measuring execution times helps ensure that the algorithms in the HMS perform well under real-world conditions.
- **Scalability**: Understanding the time complexity allows you to predict how the system will behave as the number of patients (or data size) increases.

In summary, this file is essential for evaluating the time efficiency of sorting, searching, and tree traversal algorithms within the Hospital Management System, helping to optimize and ensure the system can handle large-scale data effectively.

## `space_complexity.py` - Space Complexity Analysis

### Overview

This Python file is responsible for analyzing the **space complexity** of various algorithms used in the **Hospital Management System (HMS)**. It evaluates how much memory is used by sorting, searching, and tree traversal algorithms when handling patient data.

### Key Functions

1. **`get_process_memory()`**:

   - This function uses the `psutil` library to get the current memory usage of the process in bytes. It returns the memory usage, which is helpful for measuring how much memory is used by different functions.

2. **`measure_space_complexity(func, *args)`**:

   - This function measures the space (memory) used by a given function (`func`) by comparing the memory usage before and after the function execution.
   - It prints the initial memory usage, executes the function, and then prints the memory used by the function during its execution.

3. **`analyze_sorting_algorithms(hms)`**:

   - This function analyzes the space complexity of three sorting algorithms—**Bubble Sort**, **Insertion Sort**, and **Merge Sort**—using patient ages extracted from the HMS.
   - It explains the space complexity of each algorithm and measures the memory used during their execution.
   - **Bubble Sort** and **Insertion Sort** are both **O(1)** (constant space) algorithms, while **Merge Sort** requires **O(n)** space due to its merging process.

4. **`analyze_search_algorithms(hms)`**:

   - This function evaluates the space complexity of five different searching algorithms:
     - **Linear Search**: Performed on a linked list of patients.
     - **Binary Search**: Performed on a Binary Search Tree (BST) of patients.
     - **Jump Search**, **Interpolation Search**, and **Exponential Search**: Performed on a sorted list of patients by ID.
   - It explains and measures the memory used by each algorithm. Linear Search, Jump Search, Interpolation Search, and Exponential Search are **O(1)** (constant space), while Binary Search requires **O(log n)** space due to recursion.

5. **`analyze_tree_traversal(bst)`**:

   - This function analyzes the space complexity of three tree traversal algorithms (**In-Order**, **Pre-Order**, and **Post-Order**) on a Binary Search Tree (BST).
   - Each traversal algorithm has a space complexity of **O(log n)**, as they are recursive and the space usage depends on the depth of the tree.

6. **`main()`**:
   - This is the main driver function that generates a random dataset of patient ages and adds them to the Hospital Management System (HMS).
   - It then runs the analysis functions for sorting, searching, and tree traversal algorithms to evaluate their space complexities.

### Purpose

The purpose of this file is to assess and compare the space usage (memory consumption) of various algorithms in the HMS. By understanding the space complexity, we can determine how much memory the system will require as the size of the patient data grows.

### Why is this Important?

- **Memory Optimization**: By analyzing space complexity, you can identify which algorithms are more memory-efficient and avoid unnecessary memory overhead.
- **Scalability**: Measuring space usage helps ensure that the HMS can handle large amounts of patient data without running into memory issues.
- **Performance Evaluation**: Understanding memory usage ensures the system's efficiency in terms of both space and time, making it more reliable in real-world applications.

In summary, this file is important for evaluating the memory efficiency of sorting, searching, and tree traversal algorithms used in the Hospital Management System, helping to ensure optimal resource usage as the system scales.
