import re
import requests

# Function to validate email format
def is_valid_email(email):
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(re.match(email_pattern, email))

# Function to validate a database entry
def is_valid_entry(entry):
    # Split the entry into fields
    fields = entry.strip().split(',')

    # Check the number of fields
    if len(fields) < 2:
        return False

    # Check id and username for alphanumeric characters
    if not fields[0].isalnum() or not fields[1].isalnum():
        return False

    # Check email format
    if not is_valid_email(fields[2]):
        return False

    # Check if age is a number (if present)
    if fields[3] and not fields[3].isdigit():
        return False

    return True

# Function to extract the first letter of the username for each invalid entry
def extract_hidden_message(entries):
    invalid_usernames = [entry.split(',')[1][0] for entry in entries if not is_valid_entry(entry)]
    return ''.join(invalid_usernames)

# Load database entries from the URL
url = "https://codember.dev/data/database_attacked.txt"
response = requests.get(url)
entries = response.text.strip().split('\n')

# Extract the hidden message
hidden_message = extract_hidden_message(entries)

# Print the hidden message
print("Hidden Message:", hidden_message)
