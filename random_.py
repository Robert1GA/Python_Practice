# First, import random library
# Another lesson to import random, filename cannot be 'random.py'
import random

# random number between 0 and 1
random1 = random.random()
print(random1)

# random integer 1,2,3,4 or 5
randomint2 = random.randint(0,5)
print('1 to 5 integer:', randomint2)

# random number between 0 and 100
random2 = random.random() * 100
print('0 to 100 number:', random2)

# random from given values or strings
choice_list = ['Brewers', 'Packers', 'Badgers', 'Bucks']
print(random.choice(choice_list))

# shuffle a list
def shuffle_word(word):
    random.shuffle(word)
    return ' '.join(word)

print(choice_list)
print(shuffle_word(choice_list))
