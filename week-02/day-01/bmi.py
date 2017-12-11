mass_in_kg = 81.2
height_in_m = 1.78

#Print the Body mass index (BMI) based on these values

def calculate_bmi():
    sum_bmi = mass_in_kg / height_in_m ** 2
    return sum_bmi


print(calculate_bmi())
