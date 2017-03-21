# The following will crash a program:
#   my_file = open('name.txt', 'r')
# This will give a FileNotFoundError and the program will crash.

# We can use Try, Except to recover from errors.
try:
    file = open('sales.txt', 'r')
    print(file.read())
except:
    print('File does not exist')
# program will continue...


# Types of exceptions
    # FileNotFoundError
    # IndexError
    # KeyError
    # NameError
    # ValueError

price = input('Enter the price: ')
try:
    price = float(price)
    print('Price = ' + price)
except ValueError:  # <-- this looks for the specific type of error
    print('Not a number!')

# Also...
price = input('Enter the price: ')
try:
    price = float(price)
    print('Price = ' + price)
except ValueError as err:  # <-- creates a variable to hold the error
    print(err) # <-- prints the error
