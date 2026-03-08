with open("common_passwords.txt") as f:
    common_passwords = [line.strip() for line in f]
# define your list of special characters
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']

# define a function called analyze_password that takes password as a parameter
def analyze_password(password):
    if password.lower() in common_passwords:
        print("This password is very common and should not be used.")
        return

    # use len() to check the length
    length = len(password)
    # check if it contains uppercase letters
    has_uppercase = any(c.isupper() for c in password)
    # check if it contains lowercase letters
    has_lowercase = any(c.islower() for c in password)
    # check if it contains numbers
    has_numbers = any(c.isdigit() for c in password)
    # check if it contains special characters
    has_special = any(c in special_characters for c in password)
    # use if/elif to rate it: weak, medium, strong, very strong
    if length < 8:
        rating = "weak"
    elif length >= 8 and length < 12:
        if has_uppercase and has_lowercase and has_numbers and has_special:
            rating = "strong"
        else:
            rating = "medium"
    else:
        if has_uppercase and has_lowercase and has_numbers and has_special:
            rating = "very strong"
        else:
            rating = "strong"

    # print the results using f-strings
    print(f"Password: {password}")
    print(f"Length: {length}")
    print(f"Has Uppercase: {has_uppercase}")
    print(f"Has Lowercase: {has_lowercase}")
    print(f"Has Numbers: {has_numbers}")
    print(f"Has Special Characters: {has_special}")
    print(f"Rating: {rating}")

# ask the user to input a password
user_password = input("Enter a password to analyze: ")
# call analyze_password with their input
analyze_password(user_password)