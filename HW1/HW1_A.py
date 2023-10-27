#List of all states
from itertools import permutations
import random
all_states = list(permutations([0,1,2,3,4,5,6,7,8]))
print(f'Total no. of states: {len(all_states)}')
print(random.sample(all_states,10))