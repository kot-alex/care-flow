class Patient:
    def __init__(self, patient_id, name, age, condition):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.condition = condition

    # Less than comparison based on patient_id
    def __lt__(self, other):
        if isinstance(other, Patient):
            return self.patient_id < other.patient_id
        return False

    # Greater than comparison based on patient_id
    def __gt__(self, other):
        if isinstance(other, Patient):
            return self.patient_id > other.patient_id
        return False

    # Equal comparison based on patient_id
    def __eq__(self, other):
        if isinstance(other, Patient):
            return self.patient_id == other.patient_id
        return False

    def __repr__(self):
        return f"Patient({self.patient_id}, {self.name}, {self.age}, {self.condition})"
