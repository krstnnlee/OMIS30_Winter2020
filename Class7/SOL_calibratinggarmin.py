# OMIS 30
# author: mdavis
# Calibrating Garmin Solution

'''
You just got a brand new Garmin watch - it has a GPS mode which tracks how far you move.  You have an old one though, which can output the distance in kilometers and miles.  But the new one only records in miles.  Due to some consumer reports, you don't know if the new one is accurate, so you decide to test the two watches side by side on your next run.
You'll get the distance and distance scale from the old watch.  You'll also get the distance from the new watch, and know that it's in miles.
Write a script that determines whether or not the new watch is close enough in accuracy to the old watch.
You should be taking 4 inputs (in this order):
The old watch's recorded distance
The old watch's recorded distance scale - using the same accepted inputs as the last assignment
The new watch's recorded distance
The acceptable threshold for 'close enough', in miles
Your last line should then be printing a boolean which says if the delta is under the acceptable threshold.
print(<True/False>)
Use While loops and Try/Except to make sure that inputs 1, 3, and 4 are numerical.  And that input 2 is using the same accepted inputs as the last assignment.
Hint: make sure you accept both whole and not-whole numbers.
Hint: make sure you take your inputs in that order please!
'''

#### Strategy #####
# go for a run
# record the data from the watches - i.e. put the first 3 inputs into the computer
# do the conversions between distances
# ask the user what the acceptable threshold is
# then calculate whether or not the distances are within the threshold
# print the result

## record the data from the watches - i.e. put the first 3 inputs into the computer
# old watch's recorded distance
# old watch's distance scale
# new watch's recorded distance (in miles)
# new watch's distance scale (automatically miles)

# old watch's recorded distance
entered_positive_number = False
while entered_positive_number == False:
    try:
        print('How far did you run according to the old watch?')
        print('Enter your numerical distance: ')
        old_watch_distance = float( input() )
        if old_watch_distance > 0:
            entered_positive_number = True
            print('\n')
        else:
            print("Whoa! You ran negative distance!?!?! You're amazing. But try again.")
    except Exception as e:
        print('Please enter a numerical response.')

# old watch's distance scale
acceptable_user_scale_inputs = ['m','M','miles','Miles','km','KM','k','K','Kilometers','kilometers']
entered_valid_scale = False
while entered_valid_scale == False:
    try:
        print('What were the units of measurement on the old watch? Use one of these:')
        print(acceptable_user_scale_inputs)
        old_watch_scale = input()
        if old_watch_scale in acceptable_user_scale_inputs:
            entered_valid_scale = True
            print('\n')
        else:
            print("Please use one of the acceptable inputs.")
    except Exception as e:
        print('Please enter a valid response.')

# new watch's recorded distance
entered_positive_number = False
while entered_positive_number == False:
    try:
        print('How far did you run according to the new watch?')
        print('Enter your numerical distance - in miles!: ')
        new_watch_distance = float( input() )
        if new_watch_distance > 0:
            entered_positive_number = True
            print('\n')
        else:
            print("Whoa! You ran negative distance!?!?! You're amazing. But try again.")
    except Exception as e:
        print('Please enter a numerical response.')

# new watch's distance scale (automatically miles)
new_watch_scale = 'miles'


## do the conversions between distances
# copy from previous homework (assuming you got it correct) - but don't round and you can delete a bunch of stuff!
if old_watch_scale[0].upper() == 'M':
    old_watch_distance_converted = old_watch_distance
elif old_watch_scale[0].upper() == 'K':
    old_watch_distance_converted = float(old_watch_distance) / 1.60934
else:
    print('ERROR')


## ask the user what the acceptable threshold is
entered_positive_number = False
while entered_positive_number == False:
    try:
        print('What is the acceptable discrepancy between the two watches?')
        print('Enter your numerical threshold, in miles: ')
        threshold = float( input() )
        if threshold > 0:
            entered_positive_number = True
            print('\n')
        else:
            print("Has to be positive.  We'll take care of the of the +/- for you.")
    except Exception as e:
        print('Please enter a numerical response.')


## then calculate whether or not the distances are within the threshold
if old_watch_distance_converted - threshold <= new_watch_distance <= old_watch_distance_converted + threshold:
    within_threshold = True
else:
    within_threshold = False

## print the result
print(within_threshold)