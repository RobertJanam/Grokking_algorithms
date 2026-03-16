# returns the factorial of a number

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)

try:
    number = int(input("> "))
    if number < 1:
        print("Number must be greater than 0.")
    else:
        print(f"fact: {fact(number)}")

except ValueError:
    print("Enter a number.")
