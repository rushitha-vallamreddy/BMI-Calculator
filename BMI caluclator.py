def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        if weight <= 0 or height <= 0:
            print("Please enter positive values for both weight and height.")
            return
        
        bmi = calculate_bmi(weight, height)
        category = categorize_bmi(bmi)
        
        print(f"Your BMI is: {bmi}")
        print(f"Category: {category}")
    except ValueError:
        print("Invalid input! Please enter numerical values for both weight and height.")

if __name__ == "__main__":
    main()
