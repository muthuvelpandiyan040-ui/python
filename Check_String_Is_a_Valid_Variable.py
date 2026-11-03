
import keyword

# Get input from user
name = input("Enter a variable name: ")

# Check whether the name is valid
if name.isidentifier() and not keyword.iskeyword(name):
    print(name, "is a valid variable name.")
else:
    print(name, "is NOT a valid variable name.")
