print("Program starting.")

name = input("What is your name: ")

first_number = float(input("Enter a floating point number: "))
second_number = float(input("Enter second floating point number: "))


product = round(first_number * second_number, 2)

print(f"{name} you gave numbers {first_number} and {second_number}")
print(f"Multiplying first and second number will result in product {product}")
print("Program ending.")
