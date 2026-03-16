# countdown from a specific number
import time

def count_down(i):
    print(i)
    time.sleep(0.5) # quick interval between call stack
    if i <= 1: # basically the end (base case)
        print("Go")
    else:
        count_down(i - 1) # recursion

try:
    number = int(input("> "))
    if number < 1:
        print("Number must be greater than 0.")
    else:
        count_down(3)

except ValueError:
    print("Enter a number.")
