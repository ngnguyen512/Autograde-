def transform_password(plaintext):
    # Define replacements
    replacements = {'a': '@', 'i': '1', 'o': '0', 'z': '2', 'e': '3'}
    
    # Capitalize the first letter and make the rest lowercase
    the_rest = plaintext[1:].lower()
    
    # Replace characters as per the rules
    for original, replacement in replacements.items():
        the_rest = the_rest.replace(original, replacement)
        the_rest = the_rest.replace(original.upper(), replacement)
    
    # Add !2 to the end of the password
    transformed_password = plaintext[0].upper() + the_rest + "!2"
  
    return transformed_password

# Example interaction with the user
def main():
    print("This program will help you choose a password!")
    user_password = input("Please enter the password you would like: ")
    suggested_password = transform_password(user_password)
    print(f"Here is your suggested password: {suggested_password}")
if __name__ == "__main__":
    main()
