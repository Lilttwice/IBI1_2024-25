class patients:
    def __init__(self, patient_name, age, date_of_latest_admission, medical_history):
        self.patient_name = patient_name
        self.age = age
        self.date_of_latest_admission = date_of_latest_admission
        self.medical_history = medical_history

    def print_details(self):
        print(f"Patient Name: {self.patient_name}, Age: {self.age}, Date of Latest Admission: {self.date_of_latest_admission}, Medical History: {self.medical_history}")

# 类使用示例
patient1 = patients("John Doe", 30, "2025-01-01", "Some medical history details")
patient1.print_details()