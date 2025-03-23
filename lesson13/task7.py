import re


def format_phone_number(phone):
    cleaned = re.sub(r'\D', '', phone)
    if len(cleaned) == 10:
        return f"({cleaned[:3]}) {cleaned[3:6]}-{cleaned[6:]}"
    else:
        return "Invalid phone number format. Please enter a 10-digit number."


def main():
    phone = input("Enter a phone number: ")
    formatted = format_phone_number(phone)
    print("Formatted phone number:", formatted)


if __name__ == "__main__":
    main()
