current_users = ['john','smith','jose','jane','mark','eugene']

new_users = ['Yake','kabir','rafi','john','rippon','mark']

for nu in new_users:
    if nu in current_users:
        print(f"{nu.upper()}, this username has been taken")
    else:
        print(f"{nu}, this username is available") 
   

numbers = list(range(1,10))

for n in numbers:
    if n == 1:
        print(f"{n}st")
    elif n == 2:
        print(f"{n}nd")
    elif n == 3:
        print(f"{n}rd")
    else:
        print(f"{n}th")        

