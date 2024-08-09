import random
import string

# List of characters to use in the password
letters = string.ascii_lowercase
symbols = ["?", ":", ",", "|"]

# Combine letters and symbols
all_characters = letters + ''.join(symbols)

# Function to generate a random password
def generate_password(length=10):
    return ''.join(random.choice(all_characters) for _ in range(length))

# Generate and print a random password
password = generate_password()
print("Your password is: " + password)
