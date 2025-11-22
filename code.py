def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"
while True:
    print("1. Calculate BMI")
    print("2. Exit")
    choice = input("Enter choice: ")
  
    if choice == "1":
        weight = float(input("Enter your weight (in kg): "))
        height = float(input("Enter your height (in meters): "))

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
      
        print(f"\nYour BMI is: {bmi:.2f}")
        print("Category:", category)
        print()
    
    elif choice == "2":
        print("Goodbye.")
        break
  
    else:
        print("Invalid option.\n")
