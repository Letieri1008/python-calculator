def get_number(prompt: str) -> float:

    """Get valid number input from user."""
    
    while True:
        try:
            return float(input(prompt)
                         )
        except ValueError:
            print("Error: Please enter a valid number!")

def calculate(num1: float, num2: float, operation: str) -> float:
    """Perform the requested arithmetic operation."""
    operations = {
        '1': lambda x, y: x + y,
        '2': lambda x, y: x - y,
        '3': lambda x, y: x * y,
        '4': lambda x, y: x / y if y != 0 else None
    }
    return operations[operation](num1, num2)

def calculator():

    """Main calculator function."""

    menu = """
=== Available Operations ===
1: Addition (+)
2: Subtraction (-)
3: Multiplication (*)
4: Division (/)
0: Exit
"""
    print(menu)
    
    while True:
        operation = input("\nEnter operation number (0-4): ").strip()
        
        if operation == '0':
            print("Shutting down calculator...")
            break
            
        if operation not in {'1', '2', '3', '4'}:
            print("Invalid option! Please choose 0-4.")
            continue
            
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        
        result = calculate(num1, num2, operation)
        
        if operation == '4' and num2 == 0:
            print("Error: Division by zero!")
        else:
            symbol= {'1': '+', '2': '-', '3': '*', '4': '/'}[operation]
            print(f"\nResult: {num1} {symbol} {num2} = {result}")

if __name__ == "__main__":
    calculator()
