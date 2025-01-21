from datetime import datetime
import json

# JSON file name to store history
HISTORY_FILE = "history.json"

# Load history on startup
def load_history():
    """Loads history from a JSON file, or returns an empty list if the file doesn't exist."""
    try:
        with open(HISTORY_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)  # Load JSON data
    except FileNotFoundError:
        return []  # If the file doesn't exist, return an empty list
    except json.JSONDecodeError:
        print("Error: The history file is corrupted. The history will be reset.")
        return []  # If the file is corrupted, return an empty list

# Save history to a JSON file
def save_history():
    """Saves the history to a JSON file."""
    with open(HISTORY_FILE, 'w', encoding='utf-8') as file:
        json.dump(history, file, indent=4, ensure_ascii=False)  # Save with indentation for readability

# Add an entry to the history
def add_to_history(entry):
    """Adds an operation to the history with date and time."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Current date and time
    history.append(f"{timestamp} - {entry}")  # Add the formatted entry to the history list
    save_history()  # Automatically save after each modification

# Display the history
def show_history():
    """Displays the history of operations."""
    if not history:
        print("No calculations have been performed yet.")
    else:
        print("Calculation history:")
        for entry in history:
            print(entry)

# Prompt for a valid number
def get_number(prompt):
    """Prompts the user for a valid number."""
    while True:
        try:
            return float(input(prompt))  # Convert to a floating-point number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Prompt for a valid operator
def get_operator():
    """Prompts the user for a valid operator."""
    valid_operators = ['+', '-', '*', '/']
    while True:
        operator = input("Enter an operator (+, -, *, /): ").strip()
        if operator in valid_operators:
            return operator
        else:
            print("Invalid operator. Please choose from +, -, *, /.")

# Perform a calculation
def calculate(a, b, operator):
    """Performs the specified operation on two numbers."""
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "Error: Division by zero."
        return a / b

# Prompt for a 'yes' or 'no' response
def get_yes_no_input(prompt):
    """Prompts for a 'yes' or 'no' response and validates it."""
    while True:
        response = input(prompt).strip().lower()
        if response in ['yes', 'no']:
            return response  # Return the valid response
        print("Error: Please respond with 'yes' or 'no'.")

# Main program
def main():
    global history  # Declare history as global so it can be modified everywhere
    history = load_history()  # Load history from the JSON file
    print("Welcome to the Python calculator!")

    current_result = None  # Variable to store the previous result
    keep_running = True

    while keep_running:
        # Ask if the user wants to use the previous result
        if current_result is not None:
            use_previous = get_yes_no_input("Would you like to use the previous result? (yes/no): ")
            if use_previous == 'yes':
                num1 = current_result
                print(f"Using previous result: {current_result}")
            else:
                num1 = get_number("Enter the first number: ")
        else:
            num1 = get_number("Enter the first number: ")

        # Get the rest of the input
        operator = get_operator()
        num2 = get_number("Enter the second number: ")

        # Compute the result
        result = calculate(num1, num2, operator)

        # Display the result
        print(f"Result: {num1} {operator} {num2} = {result}")

        # Add to history with date and time
        add_to_history(f"{num1} {operator} {num2} = {result}")

        # Store the result for the next operation if it's a valid number
        if isinstance(result, (int, float)):
            current_result = result
        else:
            current_result = None

        # Offer to view the history
        view_hist = get_yes_no_input("Would you like to view the calculator history? (yes/no): ")
        if view_hist == 'yes':
            show_history()

        # Ask if the user wants to continue
        again = get_yes_no_input("Would you like to perform another calculation? (yes/no): ")
        if again == 'no':
            print("Thank you for using the calculator. Goodbye!")
            keep_running = False
        else:
            print("Alright, let's continue!")

if __name__ == "__main__":
    main()
