# BMI calculator based on user input of height and weight
# Avoid division by zero and invalid input
try:
    weight = int(input('input your weight here(kg)'))
    height = float(input('input your height here(m)'))
    if weight <= 0 or height <= 0:
        print("your weight and height must be greater than 0")
    else:
        BMI = round(weight / height ** 2, 2)
        print("Your BMI is", BMI)
except ValueError:
    print("Error. Please enter a valid number for weight and height.")
    