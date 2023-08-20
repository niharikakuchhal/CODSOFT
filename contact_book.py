import os
import time
from colorama import Fore, Back, Style

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        print(Fore.GREEN + f"Contact '{name}' added." + Style.RESET_ALL)

    def view_contacts(self):
        if not self.contacts:
            print(Fore.YELLOW + "No contacts found." + Style.RESET_ALL)
        else:
            print(Fore.CYAN + "Contact List:")
            for name, info in self.contacts.items():
                print(f"Name: {name}, Phone: {info['phone']}")
            print(Style.RESET_ALL)

    def search_contact(self, keyword):
        matches = []
        for name, info in self.contacts.items():
            if keyword.lower() in name.lower() or keyword in info['phone']:
                matches.append((name, info))
        if not matches:
            print(Fore.RED+"No matching contacts found."+Style.RESET_ALL)
        else:
            print(Fore.BLUE+"Matching Contacts:"+Style.RESET_ALL)
            for name, info in matches:
                print(Fore.CYAN+f"Name: {name}, Phone: {info['phone']}"+Style.RESET_ALL)

    def update_contact(self, name, new_phone, new_email, new_address):
        if name in self.contacts:
            self.contacts[name]['phone'] = new_phone
            self.contacts[name]['email'] = new_email
            self.contacts[name]['address'] = new_address
            print(Fore.BLUE+f"Contact '{name}' updated."+Style.RESET_ALL)
        else:
            print(Fore.RED+f"Contact '{name}' not found."+Style.RESET_ALL)

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(Fore.BLUE+f"Contact '{name}' deleted."+Style.RESET_ALL)
        else:
            print(Fore.RED+f"Contact '{name}' not found."+Style.RESET_ALL)

def main():
    contact_book = ContactBook()

    while True:
        print("\n" + Back.BLUE + Fore.WHITE + " Contact Book Menu " + Style.RESET_ALL)
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        os.system('cls' if os.name == 'nt' else 'clear')

        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            keyword = input("Enter Name or Phone to search: ")
            contact_book.search_contact(keyword)
        elif choice == '4':
            name = input("Enter Name of contact to update: ")
            new_phone = input("Enter New Phone Number: ")
            new_email = input("Enter New Email: ")
            new_address = input("Enter New Address: ")
            contact_book.update_contact(name, new_phone, new_email, new_address)
        elif choice == '5':
            name = input("Enter Name of contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print(Fore.MAGENTA + "Exiting Contact Book." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice. Please select a valid option." + Style.RESET_ALL)
        
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
