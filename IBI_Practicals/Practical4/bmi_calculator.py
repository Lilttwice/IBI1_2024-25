# BMI calculator based on user input of height and weight
# Avoid division by zero and invalid input

# 1. Prompt user for weight (kg) and height (m)
# 2. Validate inputs are positive numbers
# 3. Calculate BMI using formula: weight / (height^2)
# 4. Round BMI to 2 decimal places
# 5. Determine BMI category:
#    - Underweight: BMI < 18.5
#    - Normal: 18.5 <= BMI <= 24.9
#    - Overweight: 25 <= BMI <= 29.9
#    - Obese: BMI >= 30
# 6. Print result with BMI value and category

try:
    weight = float(input('Enter your weight (kg): '))
    height = float(input('Enter your height (m): '))
    
    if weight <= 0 or height <= 0:
        print("Error: Weight and height must be positive numbers.")
    else:
        bmi = round(weight / (height ** 2), 2)
        
        if bmi < 18.5:
            category = "underweight"
        elif 18.5 <= bmi <= 24.9:
            category = "normal weight"
        elif 25 <= bmi <= 29.9:
            category = "overweight"
        else:
            category = "obese"
            
        print(f"Your BMI is {bmi}. You are considered {category}.")
        
except ValueError:
    print("Error: Please enter valid numerical values for weight and height.")