import re

def get_integer_input(prompt):
    while True:
        try:
            userInput = int(input(prompt))
            return userInput
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")

def get_float_input(prompt):
    while True:
        try:
            userInput = float(input(prompt))
            return userInput
        except ValueError:
            print("Error: Invalid input. Please enter a valid floating-point number.")

def get_age():
    while True:
        userAge = get_integer_input("Please enter your age: ")
        if 1 <= userAge <= 120:
            return userAge
        else:
            print("Error: Please enter a valid age between 1 and 120.")

def get_non_empty_string(prompt):
    while True:
        userInput = input(prompt).strip()
        if userInput:
            return userInput
        else:
            print("Error: Input cannot be empty. Please enter a non-empty string.")

def get_email_address():
    while True:
        emailAddress = input("Please enter your email address: ")
        if re.match(r'^[a-zA-Z0-9_+&*-]+(?:\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,7}$', emailAddress):
            return emailAddress
        else:
            print("Error: Invalid email address format. Please enter a valid email address.")

def main():
    age = get_age()
    print("You entered age:", age)
    email = get_email_address()
    print("You entered email:", email)

if __name__ == "__main__":
    main()
