# This code is for displaying and managing employee details for NextRobotics

def print_employee_details(details):
    print("\n--- Employee Details ---")
    if not details:
        print("No details found.")
    else:
        for key, value in details.items():
            print(f"{key}: {value}")
    print("------------------------\n")

# Collect initial employee details
employees = {
    "Name": input("Enter your Full name: ").title(),
    "Age": int(input("Enter your Age: ")),
    "Gender": input("Enter your Gender: ").title(),
    "email": input("Enter your email: "),
    "Phone Num": int(input("Enter your Phone Number: ")),
    "Address": input("Enter your Address: ").title(),
    "Qualification": input("Qualification: ").title()
}

print("\n-------------------------------------------")
print("Welcome to NextRobotics Application Portal")
print("-------------------------------------------")

# Display initial details and ask for confirmation
print_employee_details(employees)
confirmation = input("Are these details correct? (yes/no): ").lower()

if confirmation in ('yes', 'y'):
    print("\nThank you for confirming your details. Your information has been saved.")
else:
    print("\nPlease update your details as needed.")
    while True:
        print("\nFor any changes, please select an option:")
        print("1. Add a new detail")
        print("2. Update an existing detail")
        print("3. Remove a detail")
        print("4. Finish and Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            new_key = input("Enter the new detail name (e.g., Department): ")
            new_value = input(f"Enter the value for '{new_key}': ")
            employees[new_key] = new_value
            print(f"Added new detail: '{new_key}'.")
            print_employee_details(employees)

        elif choice == '2':
            update_key = input("Enter the name of the detail to update: ")
            if update_key in employees:
                new_value = input(f"Enter the new value for '{update_key}': ")
                employees[update_key] = new_value
                print(f"Updated '{update_key}' to '{new_value}'.")
                print_employee_details(employees)
            else:
                print(f"Error: '{update_key}' not found. Please choose from the existing details.")
        
        elif choice == '3':
            remove_key = input("Enter the name of the detail to remove: ")
            if remove_key in employees:
                del employees[remove_key]
                print(f"Removed '{remove_key}'.")
                print_employee_details(employees)
            else:
                print(f"Error: '{remove_key}' not found. No changes were made.")
        
        elif choice == '4':
            print("\nFinal details have been updated and saved.")
            print_employee_details(employees)
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
