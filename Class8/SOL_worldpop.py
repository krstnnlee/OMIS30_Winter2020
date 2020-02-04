# OMIS 30
# author: mdavis
# World Population Solution

'''
Find the largest [country, continent, and population] in each continent.  (Don't just return the country - return the whole sub-list). 
Use the provided (shuffled) list on GitHub.  I added the original CSV and the code I used to shuffle the list.  But you don't need either of those.  You're looking for 'world_pop_list.py'.
There are many methods of solving this. 
Your solution must use for loops though (just for the sake of this assignment). 
You cannot use 'sort' functions.
Your code should be agnostic to the number of countries or continents there are.  i.e. if we added another country, or another continent, you should not need to change your code.
'''

# We'll go over this, but this just saves me copying and pasting the big list of lists in here.
from world_pop_list import world_pop_list

'''
Method 1 - just do Africa first, and then Asia, and see what the differences are...
'''
all_biggest_countries = list()

# Africa
africa_bucket = list()

# Add country to the Africa bucket
for country_list in world_pop_list:
    if country_list[1] == 'Africa':
        africa_bucket.append(country_list)

# Check for the biggest in the Africa bucket
max_population = 0
biggest_country = None
for country_list in africa_bucket:
    if country_list[2] > max_population:
        biggest_country = country_list
        max_population = country_list[2]
all_biggest_countries.append(biggest_country)

# Asia
asia_bucket = list()

# Add country to the Asia bucket
for country_list in world_pop_list:
    if country_list[1] == 'Asia':
        asia_bucket.append(country_list)

# Check for the biggest in the Asia bucket
max_population = 0
biggest_country = None
for country_list in asia_bucket:
    if country_list[2] > max_population:
        biggest_country = country_list
        max_population = country_list[2]
all_biggest_countries.append(biggest_country)

# And keep going for each continent
# ...
print(all_biggest_countries)


'''
Method 2 - Notice the pattern above... Replace everywhere you see Africa or Asia with a variable. But here you have to do a loop

all_biggest_countries = list()

# Continent_x
continent_bucket = list()

# Add country to the continent_bucket
for country_list in world_pop_list:
    if country_list[1] == continent:
        continent_bucket.append(country_list)

# Check for the biggest in the continent_bucket
max_population = 0
biggest_country = None
for country_list in continent_bucket:
    if country_list[2] > max_population:
        biggest_country = country_list
        max_population = country_list[2]
all_biggest_countries.append(biggest_country)

# So the loop is:
for continent in all_continents:
    # do the above

# but what is all_continents?
all_continents = set()
for country_list in world_pop_list:
    all_continents.add(country_list[1])
'''
all_biggest_countries = list()

all_continents = set()
for country_list in world_pop_list:
    all_continents.add(country_list[1])

for continent in all_continents:
    continent_bucket = list()

    # Add country to the continent_bucket
    for country_list in world_pop_list:
        if country_list[1] == continent:
            continent_bucket.append(country_list)

    # Check for the biggest in the continent_bucket
    max_population = 0
    biggest_country = None
    for country_list in continent_bucket:
        if country_list[2] > max_population:
            biggest_country = country_list
            max_population = country_list[2]
    all_biggest_countries.append(biggest_country)

print(all_biggest_countries)



'''
Method 3 - the 'elegant'/hard to understand way but way less code
''' 
## Brute force method
# First line simple version
all_continents = set()
for country_list in world_pop_list:
    all_continents.add(country_list[1])

# First line fancy version
continents = set( [country_list[1] for country_list in world_pop_list] )

# for every continent, create a blank dictionary row with continent as the key
# and [None, None, 0] as the value
continent_dict = dict.fromkeys(continents, [None, None, 0] )
# Asia: [None, None, 0]
# Africa: [None, None, 0]
# ...

for country_list in world_pop_list:
    # print('outer loop')
    # print(country_list)
    for key, value in continent_dict.items():
        # print('inner loop')
        # print(key)
        # print(value)
        if country_list[1] == key and country_list[2] > value[2]:
            continent_dict[key] = country_list
            # print(country_list)

print(continent_dict.values())