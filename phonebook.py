__author__ = 'Ryan Perkins'
phonebook = {}

#The intro asks the user who he is looking for and then directs the user to the next function.
def intro():
    search = raw_input('Who are you looking for?')
    return check_dict(search)


#This function checks to see if the person requested is in the phonebook and if he is then it prints the contact information and returns back to the intro.
#If the person is not in the phone book it then directs the user to the replay function.
def check_dict(search):
    if search in phonebook:
        print phonebook[search]
        intro()
    else:
        replay()

        #return data_entry()


#This function asks the user for the contact information to save it in the dictionary and then goes back to the intro.
def data_entry():
    name = raw_input('Enter the name.')
    address = raw_input('Enter the address.')
    number = raw_input('Enter the phone number.')
    phonebook[name] = {'name': name, 'address': address, 'number': number}
    intro()


#This function is used when the contact is not found in the phonebook.
# It then asks if the user wants to enter the contact information.
def replay():
    ask_user = raw_input("Individual not found.  Would you like to add contact information?\n type 'y' for yes or 'n' for no.").lower()
    if ask_user == 'y':
        return data_entry()
    else:
        print "Thanks for using the phonebook."


def main():
    intro()





if __name__ == '__main__':
    intro()