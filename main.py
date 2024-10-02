from calculator.calculator import Calculator

def main():
    try:
        a = input("Enter the first number: ")
        b = input("Enter the second number: ")
        operation = input("Enter the operation (add, subtract, multiply, divide): ")

        result = Calculator.calculate(float(a), float(b), operation)
        print(result)
    except ValueError:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
