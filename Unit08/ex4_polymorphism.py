class Contacts:
    def __init__(self):
        # Initialize the view to 'list' to show the list view first
        self.view = 'list'
        self.contact_list = []
        self.choice = None
        self.index = None

    def display(self):
        # Infinite loop to handle different views until 'quit' is selected
        while True:
            if self.view == 'list':
                # Show the list of contacts
                self.show_list()
            elif self.view == 'info':
                # Show detailed information about a contact
                self.show_info()
            elif self.view == 'add':
                # Add a new contact
                print()
                self.add_contact()
            elif self.view == 'quit':
                # Exit the loop and end the display method
                print('\nClosing the contact list...\n')
                break

    def show_list(self):
        # Print a blank line for legibility
        print()
        if len(self.contact_list) == 0:
            # If contact list is empty, present the user with options to add a contact or quit
            self.choice = input('(A)dd a new contact \n(Q)uit \n> ').lower()
        else:
            # If contact list is not empty, list all contacts with index numbers
            for index, contact in enumerate(self.contact_list):
                print(f"{index + 1}) {contact.first_name} {contact.last_name}")
            # Present the user with options to select a contact, add a new contact, or quit
            self.choice = input('\n(#) Select a name \n(A)dd a new contact\n(Q)uit \n> ').lower()
        # Handle the user's choice
        self.handle_choice()

    def handle_choice(self):
        # Handle user choice: 'q' to quit, 'a' to add a contact, 'c' to go to the contact list, or a number to select a contact
        if self.choice == 'q':
            self.view = 'quit'
        elif self.choice == 'a' and self.view == 'list':
            self.view = 'add'
        elif self.choice.isnumeric() and self.view == 'list':
            index = int(self.choice) - 1
            if 0 <= index < len(self.contact_list):
                self.index = index
                self.view = 'info'
        elif self.choice == 'c' and self.view == 'info':
            self.view = 'list'
        elif self.choice == 'n' and self.view == 'info':
            self.index = self.index + 1 if self.index + 1 < len(self.contact_list) else 0
        elif self.choice == 'p' and self.view == 'info':
            self.index = self.index - 1 if self.index - 1 >= 0 else len(self.contact_list) - 1

    def show_info(self):
        # Display detailed information about the selected contact
        self.contact_list[self.index].display_info()
        # Present the user with options to return to the list view, go to the next contact, go to the previous contact, or quit
        self.choice = input('\n(C)ontact List \n(P)revious contact \n(N)ext contact \n(Q)uit \n> ').lower()
        self.handle_choice()

    def __add__(self, new_contact):
        # Overload the + operator to add a new contact to the contact list
        self.contact_list.append(new_contact)

    def add_contact(self):
        # Add a new contact by creating an Information object and adding it to the contact list
        self + Information()
        # Revert back to the list view after adding a contact
        self.view = 'list'

# The Information class used to store contact details
class Information:
    def __init__(self):
        self.first_name = input('Enter their first name: ')
        self.last_name = input('Enter their last name: ')
        self.personal_phone = input('Enter their personal phone number: ')
        self.personal_email = input('Enter their personal email address: ')
        self.work_phone = input('Enter their work phone number: ')
        self.work_email = input('Enter their work email address: ')
        self.title = input('Enter their work title: ')

    def display_info(self):
        # Print the contact information with context
        print(f'\n{self.first_name} {self.last_name}')
        print(f'Personal phone number: {self.personal_phone}')
        print(f'Personal email address: {self.personal_email}')
        print(f'Work title: {self.title}')
        print(f'Work phone number: {self.work_phone}')
        print(f'Work email address: {self.work_email}')

# Testing the code
contacts = Contacts()
contacts.display()