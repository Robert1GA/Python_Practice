# Initialize a dictionary
food = {'fruit': 'apricot', 'veggie': 'artichoke', 'meat': 'deer', 'water': 'swamp water'}
print(food)

# To add key value to the dictionary
food['sweets'] = 'twizzlers'

# To remove key-value from dictionary
del food['water']

# To get a key-value pair that might not be there (without error)
# If no key-value with this method, will return None
# Because trying to access a key-value that doesn't exist would cause
# an error and program to crash
result = food.get('grain')
if result:
    print(result)
else:
    print('key does not exist:', result)

print(food)
# To print the value of a key -
print(food['meat'])
