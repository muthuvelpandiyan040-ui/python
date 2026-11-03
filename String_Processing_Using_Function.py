#Define a function process_string() to convert a string into uppercase and lowercase, find its length, reverse it, #and check whether it is a palindrome.
def process_string():

    # Accept string from user
    text = input("Enter a string: ")

    # Convert to uppercase
    print("Uppercase:", text.upper())

    # Convert to lowercase
    print("Lowercase:", text.lower())

    # Find length
    print("Length of string:", len(text))

    # Reverse string using slicing
    reverse = text[::-1]
    print("Reversed string:", reverse)

    # Check palindrome
    if text.lower() == reverse.lower():
        print("The given string is a Palindrome.")
    else:
        print("The given string is NOT a Palindrome.")


# Call the function
process_string()
