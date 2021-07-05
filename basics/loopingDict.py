# user_0 = {
#     'username':'elf',
#     'first':'enrico',
#     'last':'fermi'
# }

# for k,v in user_0.items():
#     print(f"{k} --- {v}")


# language = {
#     "python":{
#         "count":0
#     },
#     "javascript":0
# }

# language["python"]

vote = {
    "python":0,
    "javascript":0
}
v = ''
# vote["python"] = 1

# v = input('language? :')
# if v =="python":
#     vote["python"] = vote["python"]+1
# else:
#     vote["javascript"] = vote["javascript"] + 1
print('Voting\nPython=py\tJavascript=js')
while v !="q":
    v = input('language? :')
    if v == "py":
        vote["python"] = vote["python"] + 1
    elif v =='js':
        vote["javascript"] = vote["javascript"] +1    
    elif v=='q':
        print("Thanks for your vote\n\tQuiting the application")    
    else:
        print('Invalid\nTry agaain')


# print(vote)
print('\n\n\n========= Voting Result =============\n')
print(f'Python is {vote["python"]} \t Javascript is: {vote["javascript"]}')

if vote["python"] > vote["javascript"]:
    print("\nWinner is Python")
else:
    print('\nWinner is Javascript')    

