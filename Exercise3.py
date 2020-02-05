one = 1
two = 2
three = one + two
six = three * two
eightteen = 18
nine = eightteen / two

print (1 == nine % 2)

print (True and 2 == 4//2)

print (True or False)

import random

random_number = random.randint(0,20)
user_guess = int(input('Pick a number between 1 and 20?    '))

if user_guess == random_number:
    print ('You got it')
else:
    print ('Sorry better luck next time')
    print('The number was' + ' '  + str(random_number))