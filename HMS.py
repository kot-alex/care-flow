from models.patient import Patient
from data_structures.linked_list import LinkedList
from data_structures.queue import Queue
from data_structures.stack import Stack
from data_structures.hash_table import HashTable
from data_structures.binary_tree import BinarySearchTree
from algorithms.searching import binary_search, linear_search
from algorithms.sorting import bubble_sort, merge_sort, insertion_sort
from algorithms.tree_traversal import TreeTraversal
import random


class HospitalManagementSystem:
    def __init__(self):
        self.patients = LinkedList()
        self.patient_queue = Queue()
        self.patient_records = HashTable()  # HashTable for fast lookups
        self.patient_stack = Stack()  # Stack to manage recently admitted patients
        self.patient_bst = (
            BinarySearchTree()
        )  # Binary Search Tree for efficient patient retrieval
        self.tree_traversal = TreeTraversal()  # TreeTraversal for traversing BST

    def add_patient(self, name, age, condition):
        patient_id = random.randint(1000, 9999)
        patient = Patient(patient_id, name, age, condition)
        self.patients.append(patient)
        self.patient_records.insert(patient_id, patient)  # Add to HashTable
        self.patient_bst.insert(patient)  # Insert into Binary Search Tree
        # print(f"Patient {name} added with ID {patient_id}.")

    def admit_patient(self, name, age, condition):
        patient_id = random.randint(1000, 9999)
        patient = Patient(patient_id, name, age, condition)
        self.patient_queue.enqueue(patient)
        self.patient_stack.push(
            patient
        )  # Add admitted patient to stack for quick access
        print(f"Patient {name} admitted with ID {patient_id}.")

    def schedule_appointment(self):
        if self.patient_queue.is_empty():
            print("No patients in the queue to schedule an appointment.")
        else:
            patient = self.patient_queue.dequeue()
            print(
                f"Scheduled appointment for {patient.name}, ID: {patient.patient_id}."
            )

    def search_patient(self, patient_id):
        patient_list = self.patients.to_list()
        patient_list = merge_sort(patient_list, key=lambda x: x.patient_id)
        patient = binary_search(patient_list, patient_id)
        if patient:
            print(f"Patient found: {patient}")
        else:
            print("Patient not found.")

    def display_patients(self):
        patient_list = self.patients.to_list()
        sorted_patients = merge_sort(patient_list, key=lambda x: x.patient_id)
        print("Patient records:")
        for patient in sorted_patients:
            print(patient)

    def find_patient_by_id(self, patient_id):
        patient = self.patient_records.get(patient_id)  # HashTable lookup
        if patient:
            print(f"Patient found: {patient}")
        else:
            print("Patient not found in records.")

    def recent_admitted_patients(self):
        print("Recent admitted patients (using Stack):")
        while not self.patient_stack.is_empty():
            print(self.patient_stack.pop())

    def sort_patients_by_age(self):
        patient_list = self.patients.to_list()
        sorted_patients = bubble_sort(
            patient_list, key=lambda x: x.age
        )  # Bubble sort by age
        print("Patients sorted by age:")
        for patient in sorted_patients:
            print(patient)

    def sort_patients_insertion(self):
        patient_list = self.patients.to_list()
        sorted_patients = insertion_sort(
            patient_list, key=lambda x: x.age
        )  # Insertion sort by age
        print("Patients sorted by age (Insertion Sort):")
        for patient in sorted_patients:
            print(patient)

    def search_patient_by_name(self, name):
        patient_list = self.patients.to_list()
        patient = linear_search(
            patient_list, name, key=lambda x: x.name
        )  # Linear search by name
        if patient:
            print(f"Patient found: {patient}")
        else:
            print("Patient not found by name.")

    def get_patient_from_bst(self, patient_id):
        patient = self.patient_bst.search(patient_id)  # Search in Binary Search Tree
        if patient:
            print(f"Patient found in BST: {patient}")
        else:
            print("Patient not found in BST.")

    def traverse_bst(self):
        print("Traversing the Binary Search Tree:")
        print("In-order traversal:")
        print(self.tree_traversal.in_order(self.patient_bst.root))
        print("\nPre-order traversal:")
        print(self.tree_traversal.pre_order(self.patient_bst.root))
        print("\nPost-order traversal:")
        print(self.tree_traversal.post_order(self.patient_bst.root))


if __name__ == "__main__":
    hms = HospitalManagementSystem()

    hms.add_patient("Alice", 30, "Flu")
    hms.add_patient("Bob", 45, "Cough")
    hms.add_patient("Charlie", 35, "Fever")

    hms.admit_patient("David", 28, "Headache")
    print()
    hms.display_patients()
    print()
    hms.sort_patients_by_age()
    print()
    hms.sort_patients_insertion()
    print()
    hms.search_patient(1001)
    hms.find_patient_by_id(1002)
    print()
    hms.schedule_appointment()
    print()
    hms.recent_admitted_patients()
    print()
    hms.search_patient_by_name("Alice")

    hms.get_patient_from_bst(1001)
    print()
    hms.traverse_bst()
