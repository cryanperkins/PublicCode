name = raw_input('Enter the name.')
address = raw_input('Enter the address.')
number = raw_input('Enter the phone number.')
phonebook  = {}

phonebook[address] = address
phonebook[number] = number
phonebook[name] =  (name, address, number)
search = raw_input('Who are you looking for?')
print(phonebook[search])

