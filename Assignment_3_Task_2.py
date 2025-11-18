import math
# Takes in input from the user as a float.
num = float(input("Enter a number: "))

# Square Root of the number.
if num >= 0:
    square_root = math.sqrt(num)
else:
    square_root = "Undefined for negative numbers"

# Natural Log of the number.
if num > 0:
    natural_log = math.log(num)
else:
    natural_log = "Undefined for zero or negative numbers"

# Sine (in radians) of the number.
sine_value = math.sin(num)

print(f"Square root : {square_root}")
print(f"Natural logarithm : {natural_log}")
print(f"Sine (in radians): {sine_value}")