import json

# Read the JSON file
with open('student.json', 'r') as file:
    data = json.load(file)


def print_keys_values(data, indent=0):
    if isinstance(data, dict):
        for key, value in data.items():
            print("  " * indent + f"{key}:")
            print_keys_values(value, indent + 3)
    elif isinstance(data, list):
        for item in data:
            print_keys_values(item, indent)
    else:
        # Print the value with indentation
        print("  " * indent + f"{data}")


# Print keys and values from the JSON data
print_keys_values(data)
