def main():
    height = float(input("Type your height in meters like `1.75` or `2.00`: "))
    
    weight = int(input("Type your weight in kilograms like `80` or `65`: "))
    
    bmi_index = int(weight / height ** 2)
    
    print(f"Your BMI index is {bmi_index}")

if __name__ == "__main__":
    main()