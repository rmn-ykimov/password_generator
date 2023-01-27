import random

def generate_password(length):
    # Create a string of possible characters for the password
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*_"
    # Initialize an empty string to store the password
    password = ""
    # Use a for loop to add a random character from the characters string to the password string the specified number of times
    for i in range(length):
        password += random.choice(characters)
    return password

length = int(input("Enter the desired password length: "))
print("Your generated password is: ", generate_password(length))
