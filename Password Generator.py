import secrets
import string

def generate_password(length):
    # Define the character set for the password
    alphabet = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

# Get user input for password length
try:
    desired_length = int(input("Enter the desired password length: "))
    if desired_length <= 0:
        print("Please enter a positive integer for the password length.")
    else:
        generated_password = generate_password(desired_length)
        print("Generated Password:", generated_password)
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
