import random
import string

def gen_password(length):
    # All letters, numbers, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password of given length
    password ="".join(random.choices(characters, k=length))
    return password

# Getting input from the user
user = int(input("Enter the length of the password: "))
print("The generated password is:", gen_password(user))
