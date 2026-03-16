# returns the factorial of a number
import time
def fact(x, is_first_call=True):
    if x != 1:
        print(f"current number: {x}")
        cn.append(x)

    time.sleep(0.5)
    if x == 1:
        cn.append(x)
        return 1
    else:
        if ctl and len(ctl) > 0:
            for i in ctl:
                current_total = i
        else:
            current_total = x * (x - 1)
        if is_first_call:
            print(f"{x} * {x - 1}")
            time.sleep(0.5)
            print(f"= {current_total}")
        else:
            print(f"{current_total} * {x - 1}")
            time.sleep(0.5)
            current_total *= (x - 1)
            print(f"= {current_total}")

        ctl.append(current_total)
        time.sleep(0.5)
        return x * fact(x - 1, is_first_call=False)

if __name__ == "__main__":
    ctl = []
    cn = []
    try:
        number = int(input("> "))
        if number < 1:
            print("Number must be greater than 0.")
        elif number > 500:
            print("That's too much.")
        else:
            print(f"\nfact: {fact(number)}")
            for i in cn:
                if i != 1:
                    print(f"{i} * ", end='')
                else:
                    print(f"{i}")

    except ValueError:
        print("Enter a number.")
