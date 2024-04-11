def gcd(a, b):
    """Compute the Greatest Common Divisor of a and b."""
    while b:
        a, b = b, a % b
    return abs(a)

def main():
    # Introduction message
    print("This program determines the GCD of two integers.")

    # Asking for user input
    num1 = int(input("Please enter an integer: "))
    num2 = int(input("Please enter another integer: "))
    
    
    # Calculating the GCD
    gcd_result = gcd(num1, num2)

    # Displaying the result
    print(f"The GCD of ({num1}, {num2})  {gcd_result}")

    # Checking if the numbers are relatively prime
    if gcd_result == 1:
        print(f"({num1}, {num2}) are relatively prime.")
    else:
        print(f"({num1}, {num2}) are not relatively prime.")

if __name__ == "__main__":
    main()
