prices = [2.50, 3.50, 4.50]
total = 0 # For loop will error out if don't set total outside of loop
for price in prices:
    print('price is:', price)
    total = total + price

print('the total is:', total)
average = total / len(prices)
print('The average is:', average)
