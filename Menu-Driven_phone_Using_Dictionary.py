
# Menu-Driven Phonebook Application using Dictionary

phonebook = {}

while True:
    print("\n===== PHONEBOOK MENU =====")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add a new contact
    if choice == '1':
        name = input("Enter name: ")
        number = input("Enter phone number: ")

        phonebook[number] = name
        print("Contact added successfully!")

    # Update an existing contact
    elif choice == '2':
        number = input("Enter phone number to update: ")

        if number in phonebook:
            name = input("Enter new name: ")
            phonebook[number] = name
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    # Search for a contact
    elif choice == '3':
        number = input("Enter phone number to search: ")

        if number in phonebook:
            print("Name:", phonebook[number])
            print("Phone Number:", number)
        else:
            print("Contact not found!")

    # Delete a contact
    elif choice == '4':
        number = input("Enter phone number to delete: ")

        if number in phonebook:
            del phonebook[number]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    # Display all contacts
    elif choice == '5':
        if phonebook:
            print("\nPhonebook Entries:")
            for number, name in phonebook.items():
                print("Name:", name, "| Phone:", number)
        else:
            print("Phonebook is empty!")

    # Exit the application
    elif choice == '6':
        print("Exiting Phonebook Application...")
        break

    else:
        print("Invalid choice! Please try again.")
