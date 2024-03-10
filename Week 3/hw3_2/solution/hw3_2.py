def calculate_name_value(name):
    return sum((ord(char.lower()) - 96) for char in name if char.isalpha())

def main():
    print("This program calculates the numeric value of a name.")
    user_name = input("Please enter your name: ")
    name_value = calculate_name_value(user_name)
    print(f"The numeric value of your name is: {name_value}")

if __name__ == "__main__":
    main()
