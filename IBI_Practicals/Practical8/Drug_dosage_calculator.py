# Drug Dosage Calculator
# This program calculates the dosage of a drug based on the weight and age of a person. 
def dosage_calculator(weight, dosage_per_kg):
    if 10 <= weight <= 200:
        dosage = weight * dosage_per_kg
        return dosage
    else:
        return None

def volume_calculator(dosage, drug_type):
    if drug_type == "1":
        volume = dosage / 120 * 5
    elif drug_type == "2":
        volume = dosage / 250 * 5  # 修正计算公式
    else:
        return None
    
    return volume

# example
example_dosage = dosage_calculator(70, 25)
example_volume = volume_calculator(example_dosage, "1")
print(f"Example calculation: The dosage of a 120mg/5ml drug for a 70kg adult is{example_dosage}mg, the volumne is{example_volume}ml")

# input
try:
    weight = float(input("Enter your weight in kg: "))
    age = int(input("Enter your age in years: "))
    drug_type = input("Enter the type of drug (120mg/5ml & 250mg/5ml) using 1 or 2: ")
    
    # validate age
    if age <= 0:
        print("Invalid age. Please enter a positive age.")
    else:
        # dosage via age
        dosage_per_kg = 15 if age < 18 else 25
        
        # calculate dosage via weight
        dosage = dosage_calculator(weight, dosage_per_kg)
        if dosage is None:
            print("Invalid weight. Please enter a weight between 10 and 200 kg.")
        else:
            volume = volume_calculator(dosage, drug_type)
            if volume is None:
                print("Invalid drug type. Please enter '1' or '2'.")
            else:
                print(f"The dosage for a {weight} kg person of age {age} is {dosage:.2f} mg, which is equivalent to {volume:.2f} ml of the drug.")
except ValueError:
    print("Invalid input. Please enter valid numbers.")