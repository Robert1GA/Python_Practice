prices = [2.50, 3.50, 4.50]
total = 0 # For loop will error out if don't set total outside of loop
for price in prices:
    print('price is:', price)
    total = total + price

print('the total is:', total)
average = total / len(prices)
print('The average is:', average)

# Looping through a range of numbers with a step value
for i in range(2000, 2020, 4):
    print('Presidential year:', i)

# Looping through a string
word = 'Welcome!'
for letter in word:
    print(letter)

# Looping to add to a dictionary
# This will loops through all menu items and ..
# .. assign a price to each into the menu_prices dictinary
menu = ['cola', 'chips', 'sandwich', 'burger']
menu_prices = {}
price = .50
for item in menu:
    menu_prices[item] = price
    price = price + 1
print(menu_prices)

# Print out the above using a loops
for name, price in menu_prices.items():
    # using sep = '' removes the space separator (of each comma)
    # formatting the price to two decimal places - f for float
    print(name, ': $', format(price, '.2f'), sep='')
