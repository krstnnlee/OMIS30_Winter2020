# OMIS 30
# author: mdavis
# last modified: 2020-01-30

import pandas as pd
import random
import pprint

world_pop = pd.read_csv('/Users/mdavis/dev/OMIS30/Class8/world_pop.csv')
world_pop_list = []
for row in world_pop.values:
    world_pop_list.append(list(row))

random.shuffle(world_pop_list)
pprint.pprint(world_pop_list)