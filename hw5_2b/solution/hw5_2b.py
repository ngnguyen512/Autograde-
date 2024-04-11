from math import gcd

def compute_gcd_list(numbers):
    if len(numbers) == 2:
        return gcd(numbers[0], numbers[1])
    return gcd(numbers[0], compute_gcd_list(numbers[1:]))

def are_pairwise_relatively_prime(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if gcd(numbers[i], numbers[j]) != 1:
                return False
    return True

def main():
    print("This program determines the GCD of a collection of integers.")
    numbers = []
    while True:
        number_str = input("Please enter an integer (<Enter> to quit): ")
        if number_str == "":
            break
        numbers.append(int(number_str))
    
    if numbers:
        numbers_gcd = compute_gcd_list(numbers)
        print(f"The GCD of {tuple(numbers)} is: {numbers_gcd}")
        
        if are_pairwise_relatively_prime(numbers):
            print(f"{tuple(numbers)} are pairwise relatively prime.")
        else:
            print(f"{tuple(numbers)} are not pairwise relatively prime.")
    else:
        print("No numbers entered.")

if __name__ == "__main__":
    main()
