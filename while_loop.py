# Simple
x = 1
while x !=3:
    print('x is', x)
    x = x + 1

# example of customer placing order
menu = {'chips':1, 'fries':2, 'drink':3, 'sandwich':4}
orders = []
order = input("What would you like? (Press Q to quit)")

while order.upper() != 'Q':
    # Find the order and add to list if exists
    found = menu.get(order)
    if found:
        orders.append(order)
    else:
        print("That item does not exist")
    # See if the customer wants anything else
    order = input("Anything else? (Press Q to quit)")

print('you ordered:', orders)
