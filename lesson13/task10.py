import re


def extract_dates(text):
    pattern = r'\b\d{2}-\d{2}-\d{4}\b'
    dates = re.findall(pattern, text)
    return dates


def main():
    text = input("Enter a text containing dates (DD-MM-YYYY format): ")
    dates = extract_dates(text)

    if dates:
        print("Extracted dates:", dates)
    else:
        print("No dates found in the text.")


if __name__ == "__main__":
    main()
