import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# You can specify the length of the password as an argument to the function.
# If no length is specified, it will default to 12 characters.
password = generate_password()

print("Generated Password:", password)



