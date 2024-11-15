import random
import psutil
from algorithms.sorting import bubble_sort, insertion_sort, merge_sort
from algorithms.searching import (
    linear_search,
    jump_search,
    interpolation_search,
    exponential_search,
)
from algorithms.tree_traversal import TreeTraversal
from HMS import HospitalManagementSystem


# Function to get current process memory usage (in bytes)
def get_process_memory():
    process = psutil.Process()
    return process.memory_info().rss  # in bytes


# Measure memory
def measure_space_complexity(func, *args):
    initial_memory = get_process_memory()
    print(
        f"Initial memory usage before running {func.__name__}: {initial_memory / (1024 * 1024):.5f} MB"
    )

    func(*args)
    final_memory = get_process_memory()
    memory_used = (final_memory - initial_memory) / (1024 * 1024)  # MB
    print(f"Memory used by {func.__name__}: {memory_used:.5f} MB")


def analyze_sorting_algorithms(hms):
    print("\nSorting Algorithms Space Complexity:")

    ages = [patient.age for patient in hms.patients.to_list()]

    print("\nBubble Sort (O(1) Space):")
    print("In-place, no extra memory used.")
    measure_space_complexity(bubble_sort, ages.copy())

    print("\nInsertion Sort (O(1) Space):")
    print("In-place, no extra memory used.")
    measure_space_complexity(insertion_sort, ages.copy())

    print("\nMerge Sort (O(n) Space):")
    print("Requires extra space for merging subarrays.")
    measure_space_complexity(merge_sort, ages.copy())


def analyze_search_algorithms(hms):
    print("\nSearching Algorithms Space Complexity:")

    # Linear Search on LinkedList (middle patient as target)
    linked_list_patients = hms.patients.to_list()  # Convert LinkedList to list
    target_patient = linked_list_patients[len(linked_list_patients) // 2]

    print("\nLinear Search (O(1) Space):")
    print("In-place, no extra memory used.")
    measure_space_complexity(linear_search, linked_list_patients, target_patient)

    bst = hms.patient_bst
    print("\nBinary Search Tree Search (O(log n) Space):")
    print("Recursive, space depends on tree depth.")
    measure_space_complexity(lambda: bst.search(target_patient.patient_id))

    print("\nJump Search (O(1) Space):")
    print("In-place, no extra memory used.")
    patients_sorted_by_id = sorted(linked_list_patients, key=lambda p: p.patient_id)
    measure_space_complexity(
        jump_search, patients_sorted_by_id, target_patient.patient_id
    )

    print("\nInterpolation Search (O(1) Space):")
    print("In-place, no extra memory used.")
    measure_space_complexity(
        interpolation_search, patients_sorted_by_id, target_patient.patient_id
    )

    print("\nExponential Search (O(1) Space):")
    print("In-place, no extra memory used.")
    measure_space_complexity(
        exponential_search, patients_sorted_by_id, target_patient.patient_id
    )


def analyze_tree_traversal(bst):
    print("\nTree Traversal Space Complexity:")

    print("\nIn-Order Traversal (O(log n) Space):")
    print("Recursive, space depends on tree height.")
    measure_space_complexity(TreeTraversal.in_order, bst.root)

    print("\nPre-Order Traversal (O(log n) Space):")
    print("Recursive, space depends on tree height.")
    measure_space_complexity(TreeTraversal.pre_order, bst.root)

    print("\nPost-Order Traversal (O(log n) Space):")
    print("Recursive, space depends on tree height.")
    measure_space_complexity(TreeTraversal.post_order, bst.root)


def main():
    # Random dataset for analysis
    data = random.sample(range(100000), 10000)

    # HospitalManagementSystem for patient management tasks
    hms = HospitalManagementSystem()
    for age in data:
        hms.add_patient("Patient", age, "Symptom")

    analyze_sorting_algorithms(hms)

    analyze_search_algorithms(hms)

    analyze_tree_traversal(hms.patient_bst)
    print()


if __name__ == "__main__":
    main()
