from Helper import *

# Program start

print("Welcome to the address book program")

users_input = "".lower()

while users_input != "q":
    print("Available options")
    print("1 - Login")
    print("2 - Sign up")
    print("3 - Enter a contact")
    print("4 - Display all contacts")
    print("5 - Find a contact")
    print("6 - Update a contact")
    print("7 - Delete a contact")
    print("q - quit program")
    users_input = input("Select option: ")

    if users_input == "1":
        email = input("Enter your email: ").lower()
        password = input("Enter your password: ")
        login(email, password)

    if users_input == "2":
        sign_up()

    elif users_input == "3":
        print("Enter your contact's information")

        first_name = input("First name = ").lower()
        last_name = input("Last name = ").lower()
        age = input("Age = ").lower()
        phone_number = input("Phone number = ").lower()
        address = input("Address = ").lower()

        contact = Person(first_name, last_name, age, phone_number, address)
        data = {"first_name": contact.first_name, "last_name": contact.last_name, "age": contact.age,
                "phone_number": contact.phone_number, "address": contact.address}
        create_contact(data)
        print("Thank you we have received your contacts information\n")

    elif users_input == "4":
        get_all_contacts()
        input("Contacts displayed. Hit enter to continue.")

    elif users_input == "5":
        contact_to_lookup = input("Enter the contact's first name to lookup\n").lower()
        find_contact(contact_to_lookup)

    elif users_input == "6":
        contact_to_update = input("Please enter contact's first name to update\n").lower()
        update_contact(contact_to_update)

    elif users_input == "7":
        contact_to_delete = input("Enter the contact's first name to delete\n").lower()
        delete_contact(contact_to_delete)

    elif users_input.lower() == "q":
        break

print("Thank you for using the address book")

# Program End
