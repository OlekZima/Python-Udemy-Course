def main():
    height = float(input("Type your height in meters like `1.75` or `2.00`: "))
    
    weight = int(input("Type your weight in kilograms like `80` or `65`: "))
    
    bmi_index = round(weight / height ** 2, 2)

    output_string = f"Your BMI index is {bmi_index}, "

    if bmi_index < 18.5:
        output_string += "you are underweight."
    elif 18.5 <= bmi_index < 25:
        output_string += "you have a normal weight."
    elif 25 <= bmi_index < 30:
        output_string += "you are slightly overweight."
    elif 30 <= bmi_index < 35:
        output_string += "you are obese."
    else:
        output_string += "you are clinically obese."

    print(output_string)

if __name__ == "__main__":
    main()