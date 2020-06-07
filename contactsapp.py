import csv

while True:
    f = open("contacts1.csv")
    csv_f = csv.reader(f)
    command = 0
    try:
        command = int(input('''
*********************
Phi's Address Book App
*****HOME SCREEN*****
1 = Search contacts
2 = View all contacts
3 = Add new contact
9 = EXIT: 
> '''))
    except ValueError:
        print("invalid response")
    else:
        if command == 9:
            print("Goodbye")
            break
        elif command == 3:
            print("Adding new contact")
            in_first = input("What is the first name? ")
            in_last = input("What is the last name? ")
            in_email = input("What is the email address? ")
            in_all = [in_first.capitalize(), in_last.capitalize(), in_email]
            f = open("contacts1.csv", "a", newline="")
            writer = csv.writer(f)
            writer.writerow(in_all)
            print(f'{in_first} has been added to contacts!')
            #need to close csv to get it to save. gets reopened in parent while loop
            f.close()

        elif command == 2:
            print("Showing all Contacts")
            for row in csv_f:
                print(row)
        elif command == 1:
            try:
                search_options = int(input("""
*********************
Search contact options 
1 = First Name
2 = Last Name
3 = Email
9 = Return to home screen
> """))
                # contact count used for all options (first, last & email)
                contact_found = 0

                if search_options == 1:
                    print("Searching by First Name")
                    search_contact = input("Enter First Name: ")
                    for row in csv_f:
                        if search_contact.capitalize() == row[0]:
                            print(row)
                            contact_found += 1
                    if contact_found == 0:
                        print("No Contacts found!")
                    elif contact_found > 0:
                        print(f'Contacts found: {contact_found}')

                elif search_options == 2:
                    print("Searching by Last Name")
                    search_contact = input("Enter Last Name: ")
                    for row in csv_f:
                        if search_contact.capitalize() == row[1]:
                            print(row)
                            contact_found += 1
                    if contact_found == 0:
                        print("No Contacts found!")
                    elif contact_found > 0:
                        print(f'Contacts found: {contact_found}')

                elif search_options == 3:
                    print("Searching by Email")
                    search_contact = input("Enter Email: ")
                    for row in csv_f:
                        if search_contact.lower() == row[2]:
                            print(row)
                            contact_found += 1
                    if contact_found == 0:
                        print("No Contacts found!")
                    elif contact_found > 0:
                        print(f'Contacts found: {contact_found}')

                elif search_options == 9:
                    print("Returning to home")
                else:
                    print("Invalid response")
            except ValueError:
                print("Invalid response")

        else:
            print("Response not recognised, please try again")
