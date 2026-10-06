class Patient:
    def __init__(self, patient_id, name, age, illness):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.illness = illness

    def display_info(self):
        print(f"ID: {self.patient_id} | Name: {self.name} | Age: {self.age} | Illness: {self.illness}")


class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []  # a list that stores Patient objects

    def admit_patient(self, patient):
        self.patients.append(patient)
        print(f"{patient.name} has been admitted to {self.name}.")

    def discharge_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                self.patients.remove(patient)
                print(f"{patient.name} has been discharged.")
                return
        print("Patient not found.")

    def show_patients(self):
        print(f"\nPatients in {self.name}:")
        if len(self.patients) == 0:
            print("No patients yet.")
        for patient in self.patients:
            patient.display_info()

    def total_patients(self):
        return len(self.patients)


# ---- Try it out ----
hospital = Hospital("Connaught Hospital")

p1 = Patient(1, "Kadiatu", 25, "Malaria")
p2 = Patient(2, "John", 40, "Typhoid")
p3 = Patient(3, "Bintu", 18, "Fever")

hospital.admit_patient(p1)
hospital.admit_patient(p2)
hospital.admit_patient(p3)

hospital.show_patients()
print("Total patients:", hospital.total_patients())

hospital.discharge_patient(2)
hospital.show_patients()
print("Total patients:", hospital.total_patients())