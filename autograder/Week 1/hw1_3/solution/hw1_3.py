import math
def main():
    print("This program converts an integer from base 10 to base 3.")
    original_num = int(input("Enter an integer between 0 and 2000: "))
    num = original_num
    div = int(input(f"Enter the highest power of 3 that can divide into {original_num}: "))
    result = ""
    while div >= 1:
        # print(f"factor is {div}")
        # print(f"remainder is {num}")
        result += str(int(num//div))
        num %= div
        div /= 3
        # print(f"ongoing result is {result}")
        # print(f"===========================")
    print(f"The base 3 representation of {original_num} is: {result}")
main()