# Patient Record Management System
class Patient:
    def __init__(self, name: str, age: int, latest_admission: str, medical_history: str):
        self.name = name
        self.age = age
        self.latest_admission = latest_admission
        self.medical_history = medical_history
    
    def print_patient(self) -> None:
        print(f"Name: {self.name} Age: {self.age} Latest date of admission: {self.latest_admission} Medical history: {self.medical_history}")

# input name
name = input("What's the patient's name: ")

# input age， with validation
while True:
    age_input = input("What's the patient's age: ")
    if age_input.strip():  # check if input is not empty
        # try to convert input to integer
        try:
            age = int(age_input)  # transfer input to integer
            break  # valid input, exit loop
        except ValueError:
            print("Invalid input. Please enter an integer for age.")  # prompt invalid input（noninteger）
    else:
        print("Age cannot be empty. Try again.")  # prompt empty input

latest_admission = input("What's the latest date for the patient to admit: ")
medical_history = input("What's the patient's medical history: ")

patient = Patient(name, age, latest_admission, medical_history)
patient.print_patient()

#Enter patient name: Alice
#Enter patient age (integer): 35
#Enter latest admission date (e.g., 2025-05-28): 2025-05-20
#Enter medical history: Allergic rhinitis
#Name: Alice, Age: 35, Last Admission: 2025-05-20, History: Allergic rhinitis
