#Aim: Write a menu-driven Python program to perform substring checking, character counting, substring replacement, #and conversion to capital letters.
while True:

    print("\n===== STRING OPERATIONS MENU =====")
    print("1. Check Substring")
    print("2. Count Occurrences of Character")
    print("3. Replace a Substring")
    print("4. Convert to Capital Letters")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        # Check substring
        text = input("Enter the main string: ")
        sub = input("Enter substring to search: ")

        if sub in text:
            print("Substring found!")
        else:
            print("Substring not found!")

    elif choice == '2':
        # Count character occurrences
        text = input("Enter a string: ")
        char = input("Enter character to count: ")

        count = text.count(char)

        print("Number of occurrences:", count)

    elif choice == '3':
        # Replace substring
        text = input("Enter a string: ")
        old = input("Enter substring to replace: ")
        new = input("Enter new substring: ")

        result = text.replace(old, new)

        print("Updated string:", result)

    elif choice == '4':
        # Convert to capital letters
        text = input("Enter a string: ")

        print("Capital letters:", text.upper())

    elif choice == '5':
        print("Exiting the program...")
        break

    else:
        print("Invalid choice! Please try again.")
