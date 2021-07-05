# making list of more than five users
users = ['john','doe','joe','admin','smith','perterson','brad','sadler']

for u in users:
    if u == 'admin':
        print(f"\n\tHello {u.upper()} Welcome back, would you like to see a status report\n\n")
    else:
        print(f"Hello {u.title()}, thank you for logging in")    