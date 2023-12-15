from calculator_logo import logo

def choose_operation() -> str:
    is_input_correct = False
    while not is_input_correct:
        operation = input("+\n-\n*\n/\nPick an operation: ")
        
        if operation not in "+-/*":
            print("Pick valid operation!")
            continue
        is_input_correct = True
    return operation

def check_number_input(message_to_display: str) -> float:
    is_correct = False
    while not is_correct:
        try:
            input_number = float(input(message_to_display))
            is_correct = True
        except ValueError:
            print("It wasn't an number!")
    return input_number

def check_input(previous_answer: int) -> str:
    is_correct = False
    while not is_correct:
        input_next_operation = input(f"Type 'y' to continue calculating with {previous_answer}, type 'n' to start a new calculation, \nor type 'q' to quit calculator: ").lower()
        if input_next_operation in 'ynq':
            return input_next_operation

def calc_answer(first_number: int, operation: str, second_number: int) -> int:
    output = 0
    if operation == '+':
        output = first_number + second_number
    elif operation == '-':
        output = first_number - second_number
    elif operation == '*':
        output = first_number * second_number
    else:
        output = first_number / second_number
    return output

def calculator() -> str:
    first_number = check_number_input("What's the first number?: ")
    is_next_operation = True
    while is_next_operation:
        operation = choose_operation()
        second_number = check_number_input("What's the second number?: ")
        answer = calc_answer(first_number, operation, second_number)
        print(f"{first_number} {operation} {second_number} = {answer}")
        input_next_operation = check_input(answer)
        if input_next_operation == 'y':
            first_number = answer
        else:
            return input_next_operation

if __name__ == "__main__":
    print(logo)
    is_next = True
    while is_next:
        new_calculation = calculator()
        if new_calculation == 'q':
            break
        else:
            continue

    print("Bye!")
