# # alien_0 = {'color':'green', 'points':[2,5,6]}

# # alien_0['color'] = 'Yellow'

# # alien_0['positoin'] = 'right'

# # print(alien_0)

# # modifying values in dictionary
# alien_0 = {
#     'x_position':0,
#     'y_position':25,
#     'speed':'medium',
#     'color': 'green'
# }

# print(f"Original position: {alien_0['x_position']}")

# # Moving the object to right
# # Determining lenght based on object speed 
# if alien_0['speed'] == 'slow':
#     x_inc = 1
# elif alien_0['speed'] == 'medium':
#     x_inc = 2
# else:
#     x_inc = 3 

# alien_0['x_position'] = alien_0['x_position'] + x_inc


# print(f"\nNew Position is : {alien_0['x_position']}")

# # deleting key, value pair 
# print(f"alien_0 before delete\n {alien_0}")
# del alien_0['color']



# print(f"alien_0 after delete\n {alien_0}")


##################### storing similar objects #####################

# fav_languate = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil':'python'
# }

# print(fav_languate)

# peolang ={}
# name=input("Hi, your name ? or q to quit")
# lang = input(f"{name}, your language or q to quit")

# while name != 'q' and lang !='q':
#     name = input("Hi, what your name ?: ")
#     peolang[name] = name
#     lang = input("And, your language?: ")
#     peolang[name] = lang


# print(peolang)


# Voting system 

candidate = ['Python','Javascript']
p = ''
v = ''

voter = {"name":"","language":""}
vote = {"language"}

def voting(p,v,c,voter,vote):
    print(f'Our candidates are: \n {c}')
    p = input("Your voter id? : ")
    v = input("Your vote for ?\nPython=P, Javascript=J : ")
    voter["name"] = p
    voter["lanuage"] = v
   

# voting(p,v,candidate,voter,vote)
# voting(p,v,candidate,voter,vote)
# voting(p,v,candidate,voter,vote)
# voting(p,v,candidate,voter,vote)

while p !='q' or v !='q':
    print(f"Our candidates are {candidate}")
    p = input('Your voter id please: ')
    voter["name"] =p
    v = input(f"{candidate[0]}=A and {candidate[1]}=B \nYour Vote for:")
    voter["language"] =v


print(f"voter: {voter}\n\nvote:{vote}")
























