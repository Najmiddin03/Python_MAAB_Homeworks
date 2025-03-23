import re


def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>_]', password))

    strength = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria])

    if strength == 1:
        return "Weak"
    elif strength == 2:
        return "Medium"
    elif strength == 3:
        return "Strong"
    elif strength == 4:
        return "Very Strong"


def main():
    password = input("Enter a password: ")
    strength = check_password_strength(password)
    print("Password Strength:", strength)


if __name__ == "__main__":
    main()
