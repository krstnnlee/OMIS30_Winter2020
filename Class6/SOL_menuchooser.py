# OMIS 30
# author: mdavis
# Menu Chooser Solution

'''
Pretend your friend works at a fancy tech company where they get free gourmet lunches each day.  They are allowed to invite you to their cafe 1x this week, so they're going to ask you what day you want to join them.  Once you decide which day, you need to figure out which meal you're going to go to.  To decide, you'll want to see the main courses for each meal, and then choose the meal based of which has your favorite main course.
Your goal is to start with a menu (given below), and prompt the user for inputs, and then tell the user which meal (breakfast, lunch, or dinner) that they chose.  One requirement though, is the user (chooser) can only select the meal by selecting the main course.  (You can't do something like tell the user breakfast is eggs, lunch is sandwich, dinner is turkey, and then ask the user to say 'dinner'.  They'd have to say 'turkey', and then you would go back on the code side to figure out that turkey belongs to dinner.)
This is your first real problem-solving exercise.  Think it through, and write an outline before writing any code.
Create a script named 'menuchooser.py'.  Create it via VS Code.  Do not include anything with your name or identifying information in it.  Submit it via Camino.
You need to prompt the user twice (and only twice).  Make sure you do so in this order:
    Selecting day of week
    Selecting the main course
Your last line of code should be 
print('You chose ' + <DayOfWeek> + ' ' + <Meal> + ' for your free meal!')

Hints:
There should be five days in the menu.  Print them to the user, and ask the user to select one of the days.
There should be three mains for each day.  Print them to the user, and ask the user to select one of the mains.
Capitalization matters!  Be careful with user inputs - they might not always capitalize things as you want them to.
You'll have to get creative - you may have to switch variables into other variable types, create lists out of parts of other lists, tuples, dictionaries, etc..  You don't need any if statements or loops.  
You should be able to check your own code by selecting 'Friday' at your first prompt, 'Waffle' at your second prompt, and getting back ('You chose Friday Breakfast for your free meal!')
'''

menu = {
'Monday':
{'Breakfast': {'Drink': 'Water', 'Appetizer': 'Hash Browns', 'Main': 'Eggs', 'Dessert': 'Cupcake'},
'Lunch': {'Drink': 'Soda', 'Appetizer': 'Crisps', 'Main': 'Burger', 'Dessert': 'Pie'},
'Dinner': {'Drink': 'Milk', 'Appetizer': 'Fries', 'Main': 'Steak', 'Dessert': 'Cookies'}},

'Tuesday':
{'Breakfast': {'Drink': 'Horchata', 'Appetizer': 'Chips', 'Main': 'Burrito', 'Dessert': 'Caramel'},
'Lunch': {'Drink': 'Orange Soda', 'Appetizer': 'Takis', 'Main': 'Quesadilla', 'Dessert': 'Flan'},
'Dinner': {'Drink': 'Milk', 'Appetizer': 'Street Taco', 'Main': 'Super Burrito', 'Dessert': 'Cinnamon Twists'}},

'Wednesday':
{'Breakfast': {'Drink': 'Orange Juice', 'Appetizer': 'Tater Tots', 'Main': 'Pancakes', 'Dessert': 'Frosted Donut'},
'Lunch': {'Drink': 'Water', 'Appetizer': 'Mushroom Bundle', 'Main': 'Pad Thai', 'Dessert': 'Pineapple Fruit Cake'},
'Dinner': {'Drink': 'Beer', 'Appetizer': 'Spring Rolls', 'Main': 'Yellow Curry', 'Dessert': 'Rice Roll'}},

'Thursday':
{'Breakfast': {'Drink': 'Apple Juice', 'Appetizer': 'Mini Pizza Rolls', 'Main': 'Spaghetti', 'Dessert': 'Cannoli'},
'Lunch': {'Drink': 'Water', 'Appetizer': 'Mozzarella Sticks', 'Main': 'Penne Pasta', 'Dessert': 'Cake'},
'Dinner': {'Drink': 'Wine', 'Appetizer': 'Cheese Charcuterie', 'Main': 'Lasagna', 'Dessert': 'Croissant'} },

'Friday':
{'Breakfast': {'Drink': 'Coffee', 'Appetizer': 'Cereal', 'Main': 'Waffle', 'Dessert': 'Syrup Pancakes'},
'Lunch': {'Drink': 'Kale Juice', 'Appetizer': 'Mashed Potatoes', 'Main': 'Turkey', 'Dessert': 'Carrot Cake'},
'Dinner': {'Drink': 'Milk', 'Appetizer': 'Eggplant Bites', 'Main': 'Deep Dish Pizza', 'Dessert': 'Pizookie'}}
}


# figure out which day
    # print the list of options of days
        # find the keys in the dictionary
        # print them
print( list( menu.keys() ) )
    # ask the user which day
        # print a question to the user
print( 'Which day would like to come in?' )
    # get their answer
        # use the input function
DayOfWeek = input()

# figure out the main courses for that day and list them
    # 'search' === use the key to get the value because you're using dictionaries
    # search the dictionary for that day
    # search the day dictionary for each of the three meals
    # search each of the meal dictionaries for the mains
    # print each of the mains out
print('\n')
print( menu[DayOfWeek]['Breakfast']['Main'] )
print( menu[DayOfWeek]['Lunch']['Main'] )
print( menu[DayOfWeek]['Dinner']['Main'] )

# figure out the favorite
    # ask the user for which main?
print( 'Which main would you like?' )
    # use the input function to get their answer
Main = input()

# match the favorite to the courses ***

### Solution 1 ###
# Create a dictionary of values
temp_dict = dict()
temp_dict[ menu[DayOfWeek]['Breakfast']['Main'] ] = 'Breakfast'
temp_dict[ menu[DayOfWeek]['Lunch']['Main'] ] = 'Lunch'
temp_dict[ menu[DayOfWeek]['Dinner']['Main'] ] = 'Dinner'
Meal = temp_dict[Main] 

### Solution 2 ###
# Create a list of the values and use a simple index
name_of_meals = [ 'Breakfast', 'Lunch', 'Dinner' ]
name_of_meals = list( menu[DayOfWeek].keys() )
list_of_meals = [ menu[DayOfWeek]['Breakfast']['Main'], menu[DayOfWeek]['Lunch']['Main'], menu[DayOfWeek]['Dinner']['Main'] ]
meal_index = list_of_meals.index(Main)
Meal = name_of_meals[meal_index]

### Solution 3 ###
# Go fancy and do solution 2 in one giant step
Meal = list( menu[DayOfWeek].keys() )[ [ menu[DayOfWeek]['Breakfast']['Main'], menu[DayOfWeek]['Lunch']['Main'], menu[DayOfWeek]['Dinner']['Main'] ].index(Main) ]

#### Solution 4 ###
# using if statements - which was not allowed initially
if Main == menu[DayOfWeek]['Breakfast']['Main']:
    Meal = 'Breakfast'
elif Main == menu[DayOfWeek]['Lunch']['Main']:
    Meal = 'Lunch'
elif Main == menu[DayOfWeek]['Dinner']['Main']:
    Meal = 'Dinner'


# print it out
print('\n')
print('You chose ' + DayOfWeek + ' ' + Meal + ' for your free meal!')