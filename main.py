"""
Main script for generating random passwords
"""
import password_generator

length_input = password_generator.get_valid_password_length
generate_password = password_generator.generate_password

if __name__ == "__main__":
    print("Your generated password is: ", generate_password(length_input))
