num = int(input("Enter a number to calculate it's factorial: "))
def factorial(num):
    if num < 0:
        print("Number can't be negative. Try again!")
        return None
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)
print(f"The factorial of the entered number is: {factorial(num)}")