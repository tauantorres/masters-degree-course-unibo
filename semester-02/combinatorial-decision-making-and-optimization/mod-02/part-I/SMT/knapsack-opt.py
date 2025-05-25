from z3 import *

# Optimization version of 0-1 knapsack: select a number of items which total 
# weight is at most MAX_WEIGHT and total value is maximal.

# Input parameters. Can be defined in another file.
ITEMS = [
    (60, 10),   # Item 1: value=60, weight=10
    (100, 20),  # Item 2: value=100, weight=20
    (120, 30),  # Item 3: value=120, weight=30
    (90, 25),   # Item 4: value=90, weight=25
    (30, 5),    # Item 5: value=30, weight=5
    (80, 15)    # Item 6: value=80, weight=15
]
NUM_ITEMS = len(ITEMS)
MAX_WEIGHT = 50

# Model.
selected = Ints(' '.join(['x_' + str(i) for i in range(NUM_ITEMS)]))
s = Optimize()
tot_value = 0
tot_weight = 0
tot_value = 0
tot_weight = 0
for i in range(NUM_ITEMS):
  x_i = selected[i]
  s.add(x_i >= 0)
  s.add(x_i <= 1)
  tot_value  += x_i * ITEMS[i][0]
  tot_weight += x_i * ITEMS[i][1]
s.add(tot_weight <= MAX_WEIGHT)
z = s.maximize(tot_value)

print(f'The problem is {s.check()}')
print(f'Optimal solution (value {z.value()}):')
model = s.model()
for i in range(NUM_ITEMS):
  if model[selected[i]] == 1:
    print(f'\t{selected[i]} -- value: {ITEMS[i][0]} -- weight: {ITEMS[i][1]}')
    
