def calculate_paracetamol_volume(weight, strength):
    # define the valid strengths of paracetamol in the unit of mg per 5 ml
    valid_strengths = [120, 250]
    if weight < 10 or weight > 100:
        raise ValueError("Weight should be between 10 and 100 kg")
    if strength not in valid_strengths:
        raise ValueError("Invalid paracetamol strength. Valid strengths are 120 mg/5 ml or 250 mg/5 ml")
    required_dose = weight * 15
    if strength == 120:
        volume = (required_dose / 120) * 5
    else:
        volume = (required_dose / 250) * 5
    return volume

# try an example
try:
    volume = calculate_paracetamol_volume(30, 120)
    print(f"The required volume of paracetamol is {volume} ml")
except ValueError as e:
    print(e)