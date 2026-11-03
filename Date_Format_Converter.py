
from datetime import datetime

try:
    # Accept date from user
    date_input = input("Enter date (dd-mm-yyyy): ")

    # Convert date into required format
    date_object = datetime.strptime(date_input, "%d-%m-%Y")

    # Display converted date
    result = date_object.strftime("%B %d, %Y")

    print("Converted Date:", result)

except ValueError:
    print("Invalid date! Please enter a valid date in dd-mm-yyyy format.")
