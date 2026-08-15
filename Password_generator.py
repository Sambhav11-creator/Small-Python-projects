import secrets
import string
x=int(input("Enter the length of the password: "))
def generate_password(length=x):
    characters = string.ascii_letters + string.digits + string.punctuation
    # string.ascii_letters is used for to get letters from A-Z ,a-z
    # string.digits is used to get numbers from 0-9
    # string.punctuation is used to get symbols
    password = "".join(secrets.choice(characters) for i in range(length))
    return password

print(generate_password())
