# 3-4 

guests = ['john','smith','doe','joe','brad']

message = 'I want to invite you for dinner tonight'

def invite_guest():
    print('Inviting all guests name: ')
    for g in guests:
        print(f'Hello {g.title()}, {message}')

def print_guest():
    print('Printing all guest name: ')
    for g in guests:
        print(g.title())       

# guests.remove('joe')
notcomming = guests.pop(3)


invite_guest()
print('----------------------------------')
print(f'guest who could not make: {notcomming}')

# adding guest 
guests.insert(0,'Leonerd')

guests.insert(3,'Hafstader')

guests.append('Sheldon')



print_guest()
print('---------------Inviting for last time-------------------')
invite_guest()

print('\n\t UPDATE: I can only invite two people for dinner')


def shrinking_guest():
    poppedGuest = guests.pop()
    print(f'\nSorry {poppedGuest}, I can not invite you for dinner')

shrinking_guest()


