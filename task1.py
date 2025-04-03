#Assienment 1 
#Takes two numbers as input from the user.
# Step 1: Get two numbers from the use
try:
    num1 = int(input("Enter first number: "))  # Convert input to int
    num2 = int(input("Enter second number: "))  # Convert input to int

    # Step 2: Perform calculations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2

    # Handle division carefully (avoid division by zero)
    if num2 != 0:
        division = num1 // num2  # Integer division
    else:
        division = "Undefined (cannot divide by zero)"

    # Step 3: Display results
    print("\nResults:")
    print(f"addition: {addition}")
    print(f"subtraction: {subtraction}")
    print(f"multiplication: {multiplication}")
    print(f"division: {division}")

except ValueError:
    print("Error: Please enter valid numbers!")