class InputValidationError(Exception):
    pass

def validate_input(user_input):
    if not isinstance(user_input, str):
        raise InputValidationError("Input must be a string")
    if len(user_input) == 0:
        raise InputValidationError("Input cannot be empty")
    if any(char.isdigit() for char in user_input):
        raise InputValidationError("Input cannot contain numbers")
    return True

def main_processing_loop():
    while True:
        user_input = input("Enter a command (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        try:
            validate_input(user_input)
            # Process the valid input here (placeholder for actual functionality)
            print(f"Processing input: {user_input}")
        except InputValidationError as e:
            print(f"Invalid input: {e}")

if __name__ == '__main__':
    main_processing_loop()