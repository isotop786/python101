import pdb;

available_topping = ['mushrooms','olives','green peppers','pepperoni','pineapple',
                    'extra cheese']
req_topping = []                    

def input_req():
    choice = input('Choose your topping:')
    req_topping.append(choice)

def making_pizza():
    for r in req_topping:
        if r in available_topping:
            print(f"Adding {r} in your pizza")
        else:
            print(f"Sorry, we don't have {r}")


# req_topping = ['mushrooms','french fries','extra cheese']


print(f"Available toppings are :\n\t{available_topping}")

input_req()

print(len(req_topping))



if len(req_topping) <= 6:
    add = input("Do you want to add more topping? y/n: ")
    if add == 'y':
        print(add)
        input_req()

        print(req_topping)
    else:
        making_pizza()
else:
    print('Sorry, topping is full')    


making_pizza()

# for r in req_topping:
#     if r in available_topping:
#         print(f'Adding {r} in your pizza')
#     else:
#         print(f"Sorry, we don't have {r}.")   


print(req_topping)

print("\nFinished making your pizza :)")    
