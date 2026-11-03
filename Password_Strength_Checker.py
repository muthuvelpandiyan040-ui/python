
# Password Strength Checker

password = input("Enter your password: ")

# Check password conditions
length = len(password) >= 8
digit = any(char.isdigit() for char in password)
uppercase = any(char.isupper() for char in password)
lowercase = any(char.islower() for char in password)
special = any(not char.isalnum() for char in password)

# Check all conditions
if length and digit and uppercase and lowercase and special:
    print("Strong Password")
else:
    print("Weak Password")
    print("Missing conditions:")

    if not length:
        print("- Password must contain at least 8 characters.")

    if not digit:
        print("- Password must contain at least one digit.")

    if not uppercase:
        print("- Password must contain at least one uppercase letter.")

    if not lowercase:
        print("- Password must contain at least one lowercase letter.")

    if not special:
        print("- Password must contain at least one special character.")
