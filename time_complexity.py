import random
import time
from algorithms.sorting import bubble_sort, insertion_sort, merge_sort
from algorithms.searching import (
    linear_search,
    jump_search,
    interpolation_search,
    exponential_search,
)
from algorithms.tree_traversal import TreeTraversal
from HMS import HospitalManagementSystem


# Measures the execution time of a function
def measure_time(func, *args, repetitions=1):
    start = time.time()
    for _ in range(repetitions):
        func(*args)
    end = time.time()
    average_duration = (end - start) / repetitions
    return average_duration


def analyze_sorting_algorithms(hms):
    print("\nSorting Algorithms Time Complexity:")

    # Extract patient ages for sorting
    ages = [patient.age for patient in hms.patients.to_list()]

    duration = measure_time(bubble_sort, ages.copy())
    print(f"Bubble Sort Time: {duration:.5f} seconds")

    duration = measure_time(insertion_sort, ages.copy())
    print(f"Insertion Sort Time: {duration:.5f} seconds")

    duration = measure_time(merge_sort, ages.copy())
    print(f"Merge Sort Time: {duration:.5f} seconds")


def analyze_search_algorithms(hms):
    print("\nSearching Algorithms Time Complexity:")

    # Linear Search on LinkedList (middle patient as target)
    linked_list_patients = hms.patients.to_list()  # Convert LinkedList to list
    target_patient = linked_list_patients[len(linked_list_patients) // 2]
    target_patient_id = target_patient.patient_id
    duration = measure_time(linear_search, linked_list_patients, target_patient)
    print(f"Linear Search Time (LinkedList): {duration:.5f} seconds")

    # Binary Search on Binary Search Tree
    bst = hms.patient_bst
    duration = measure_time(lambda: bst.search(target_patient.patient_id))
    print(f"Binary Search Time (Binary Search Tree): {duration:.5f} seconds")

    # Sorted List
    patients_sorted_by_id = sorted(linked_list_patients, key=lambda p: p.patient_id)

    # Jump Search on Sorted List
    duration = measure_time(jump_search, patients_sorted_by_id, target_patient_id)
    print(f"Jump Search Time: {duration:.5f} seconds")

    # Interpolation Search on Sorted List
    duration = measure_time(
        interpolation_search, patients_sorted_by_id, target_patient_id
    )
    print(f"Interpolation Search Time: {duration:.5f} seconds")

    # Exponential Search on Sorted List
    duration = measure_time(
        exponential_search, patients_sorted_by_id, target_patient_id
    )
    print(f"Exponential Search Time: {duration:.5f} seconds")


def analyze_tree_traversal(bst):
    print("\nTree Traversal Algorithms Time Complexity:")

    # In-Order Traversal
    duration = measure_time(TreeTraversal.in_order, bst.root)
    print(f"In-Order Traversal Time (BST): {duration:.5f} seconds")

    # Pre-Order Traversal
    duration = measure_time(TreeTraversal.pre_order, bst.root)
    print(f"Pre-Order Traversal Time (BST): {duration:.5f} seconds")

    # Post-Order Traversal
    duration = measure_time(TreeTraversal.post_order, bst.root)
    print(f"Post-Order Traversal Time (BST): {duration:.5f} seconds")


def main():
    # Random dataset for analysis
    data = random.sample(range(100000), 10000)

    # HospitalManagementSystem for patient management tasks
    hms = HospitalManagementSystem()
    for age in data:
        hms.add_patient("Patient", age, "Symptom")

    analyze_sorting_algorithms(hms)

    analyze_search_algorithms(hms)

    # Binary Search Tree from hms for Traversal
    analyze_tree_traversal(hms.patient_bst)
    print()


if __name__ == "__main__":
    main()
