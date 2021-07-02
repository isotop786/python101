# A List is a collection which is ordered and changeable. Allows duplicate members.
# bicycles = ['terk','redline','specialized']

# print(bicycles)

# print(f'bicycle at index[1] is: {bicycles[1]}')

# print(bicycles[1].title())

# print(f'the last element of list is: {bicycles[-1].title()}')


# List Modifying 

motorcycles = ['honda','yamaha','suzuki']
# motorcycles = []


def print_moto():
    print('Printing all motorcycles: ')
    for x in  motorcycles:
        print(x.title())

# modify element
# motorcycles[0] = 'ducati'

# adding new element in the list

# motorcycles.append('ducati motor')
# motorcycles.append('honda')
# motorcycles.append('suzuki')
# motorcycles.append('yamaha')

# motorcycles.insert(0,'ducati')
# print(f'list before del {print_moto()}')
# removing element 
# del motorcycles[1]
# popped_moto = motorcycles.pop()


print_moto()

motorcycles.remove('suzuki')

print_moto()

# print(f'pooped motorcycle: {popped_moto}')
