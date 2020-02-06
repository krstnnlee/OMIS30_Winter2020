# ##################
# author: midavis
# date: 2019-11-04
#
# OMIS 30
# Generate Random Password Homework Solution
# #####################################

#### Requirements ####
# Generate a random password of length n.
# n should be defined by the user, by taking an input.
# Your input should be able to handle invalid inputs (i.e. use try/except and while loops)
# The password must contain at least one uppercase english alphabet letter.
# The password must contain at least one lowercase engish alphabet letter.
# The password must contain at least one numeral [0-9].
# There cannot be any discernable pattern from the passwords your program creates.
# Use the random library and loops, but not the string or any other libraries.
# Your last line should be print(<yourpassword>)

#### Strategy #####
## Ask the user for the length n
## Check to make sure that they entered a valid number - minimum is 3
## Make lists of valid characters
## Use loops and random to choose values from those lists until we hit length n
## Check to make sure that the requirements are met

#### Start of Code #####
import random

## Ask the user for the length n
## Check to make sure that they entered a valid number
entered_positive_number = False
while entered_positive_number == False:
    try:
        print('How many characters do you want in your new password?: ')
        n = int( input() )
        if n >= 3:
            entered_positive_number = True
            print('\n')
        else:
            print("Please make sure you enter a positive integer greater than 2!")
    except Exception as e:
        print('Please enter a positive integer.')

## Make lists of valid characters
lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase = [x.upper() for x in lowercase]
# uppercase = list()
# for x in lowercase:
#     uppercase.append( x.upper() )
numbers = ['0','1','2','3','4','5','6','7','8','9']

## Use loops and random to choose values from those lists until we hit length n
## Check to make sure that the requirements are met

# Because of the minimum requirements, we know we need at least 3 characters, and one from each group
# We can generate one random element from each of those three categories.
# Then for the rest of the 'n' elements, we generate random elements from any of the values.
# Then we combine the first 3 things, plus the ones from the for loop, to get to the full list of things
# Then randomly distribute the characters around.
# Convert the list to a string

one_lower = random.choice(lowercase)
one_upper = random.choice(uppercase)
one_number= random.choice(numbers)
all_chars = lowercase + uppercase + numbers
list_of_chars = [one_lower, one_upper, one_number]

for i in range(0,n-3,1):
    list_of_chars.append( random.choice(all_chars) )

# Then randomly distribute the characters around.
random.shuffle(list_of_chars)

# Convert the list to a string
my_password = ''.join(list_of_chars)

print(my_password)