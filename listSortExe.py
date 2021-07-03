# 1. storing location23e 
places = ['dhaka','chandpur','sylhet','cyberjaya','kualalumpur','kajang']

# 2. Printing list in original order
print(f'Printing list in original order: \n\t {places}')

# 3. rearrageing the list temporarily
print(f'Printing list in alphabetical order: \n\t {sorted(places)}')

# 4. Original list display
print(f'Printing original list \n\t {places}')

# 5. Display list in reverse ahphabetical order
temp = sorted(places)
print(f'Printing list in reverse alphabetical order \n\t {sorted(places, reverse=True)}')

# 6. Printing original list 
print(f'printing original list again: \n\t{places}')

# 7. Reversing the list 
places.reverse()
print(f'Printing reverse list : \n\t {places}')

# 8. Sorting alphibeticallay 
places.sort()
print(f'Printing permanently sorted list \n\t {places}')

# 9. Reversing sorted list 
places.reverse()
print(f'Prining reverse sorted list \n\t {places}')
