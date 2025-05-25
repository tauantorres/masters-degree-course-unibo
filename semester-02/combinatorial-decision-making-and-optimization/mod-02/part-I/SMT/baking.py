from z3 import *

# Baking cakes.

# Input parameters. Can be defined in another file.
FLOUR_QTY = 4000
FLOUR_B = 250
FLOUR_C = 200
BANANA_QTY = 6
BANANA_B = 2
BANANA_C = 0
SUGAR_QTY = 2000
SUGAR_B = 75
SUGAR_C = 150
BUTTER_QTY = 500
BUTTER_B = 100
BUTTER_C = 150
COCOA_QTY = 500
COCOA_B = 0
COCOA_C = 75
PROFIT_B = 400
PROFIT_C = 450

# Model.
#B, C = Ints('#BananaCakes #ChocoCakes')
B, C = Reals('#BananaCakes #ChocoCakes')
s = Optimize()
s.add(B >= 0)
s.add(C >= 0)
s.add(FLOUR_B * B + FLOUR_C * C <= FLOUR_QTY)
s.add(SUGAR_B * B + SUGAR_C * C <= SUGAR_QTY)
s.add(BANANA_B * B + BANANA_C * C <= BANANA_QTY)
s.add(BUTTER_B * B + BUTTER_C * C <= BUTTER_QTY)
s.add(COCOA_B * B + COCOA_C * C <= COCOA_QTY)
z = s.maximize(PROFIT_B*B + PROFIT_C*C)

print(f'The problem is {s.check()}')
print(f'Optimal solution (value {z.value()}$):')
model = s.model()
print(f'#Banana cakes {model[B]}')
print(f'#Chocolate cakes {model[C]}')
    
