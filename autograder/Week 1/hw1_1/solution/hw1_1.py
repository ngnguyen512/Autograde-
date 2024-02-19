import math
def main():
    print("This program calculates the geometric mean of a set of numbers.")
    n = int(input("How many numbers are you providing? "))
    ans = 1
    for i in range(n):
        a = float(input("Enter number: "))
        ans *= a
    ans = math.pow(ans, 1/n)
    print("Geometric mean =", round(ans, 3))

