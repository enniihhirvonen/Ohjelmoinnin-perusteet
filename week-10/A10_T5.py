"""
########################################################
# Task A10_T5
# Developer Enni Hirvonen
# Date 2025-12-05
########################################################

"""

def recursive_factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * recursive_factorial(num-1)

def main():
    print("Program starting.")

    num = int(input("Insert factorial: "))

    # steps for multiplication string
    steps = "*".join(str(i) for i in range(1, num + 1))

    result = recursive_factorial(num)
    print(f"Factorial {num}!")
    print(f"{steps} = {result}")

    print("Program ending.")

if __name__ == "__main__":
    main()