contacts = {}

while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone
        print("Contact Added Successfully!")

    elif choice == 2:
        if len(contacts) == 0:
            print("No contacts available.")
        else:
            print("\n----- Contact List -----")
            for name, phone in contacts.items():
                print(name, ":", phone)

    elif choice == 3:
        name = input("Enter name to search: ")

        if name in contacts:
            print("Phone Number:", contacts[name])
        else:
            print("Contact not found.")

    elif choice == 4:
        name = input("Enter name to delete: ")

        if name in contacts:
            contacts.pop(name)
            print("Contact Deleted.")
        else:
            print("Contact not found.")

    elif choice == 5:
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice.")