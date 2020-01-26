# OMIS 30
# author: mdavis
# Distance Converter Solution

'''
Build a program that converts a user input between miles and kilometers (and kilometers to miles).  Use the following template.  
You must take inputs in the order listed below.  And your last line must be the print statement specified below.
# Ask the user for which scale they are going to start with?
# Check to make sure that the user inputted one of the acceptable values
# acceptable_user_scale_inputs = ['m','M','miles','Miles','km','KM','k','K','Kilometers','kilometers']
# If they did not, print out a statement telling them they did not do so and then quit out of the program.
# If they did, then continue with the rest of the program.
# Ask user for distance in the above scale
# Check to make sure that the user entered a valid distance. 
# acceptable_user_input = <float>
# Convert from M to KM, or KM to M
# Hint: is there a pattern you can use that means you don't have to write a lot of if/elif statements?
# Print out result
# print(<user_input> <'miles'/'kilometers'> is equivalent to <new distance rounded to 1 decimal places> in <'miles'/'kilometers'>)
# Hint: test this with google in both directions
'''


# Ask the user for which scale they are going to start with?
print('Are you starting with miles or kilometers?')
print('Acceptable inputs are: ')
acceptable_user_scale_inputs = ['m','M','miles','Miles','km','KM','k','K','Kilometers','kilometers']
print(acceptable_user_scale_inputs)
starting_scale = input()

# If they did not, print out a statement telling them they did not do so and then quit out of the program.
# If they did, then continue with the rest of the program.
if starting_scale in acceptable_user_scale_inputs:
    pass
else:
    print('Please try again next time with a true value')
    quit()

# Ask user for distance in the above scale
print('What is your starting distance in ' + starting_scale + '?')
print('Please enter it in a float format:')
starting_distance = input()

# Check to make sure that the user entered a valid distance.  
if starting_distance.strip().replace('.','').isdigit():
    pass
else:
    print('Please try again next time with a true numerical value (float).')
    quit()

# Or you can do it this way... Which is way easier and way more accurate
try:
    float(starting_distance)
except:
    print('Please try again next time with a true numerical value (float).')
    quit()


# Convert from M to KM, or KM to M
# Hint: is there a pattern you can use that means you don't have to write a lot of if/elif statements?
if starting_scale[0].upper() == 'M':
    old_scale = 'miles'
    new_distance = round( 1.60934 * float(starting_distance), 1)
    new_scale = 'kilometers'
elif starting_scale[0].upper() == 'K':
    old_scale = 'kilometers'
    new_distance = round( float(starting_distance) / 1.60934, 1)
    new_scale = 'miles'
else:
    print('ERROR')


# Print out result
print(starting_distance +  ' ' + old_scale + ' is equivalent to ' + str(new_distance) + ' in ' + new_scale)