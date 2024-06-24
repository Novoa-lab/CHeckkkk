from logic import *
from utils import expr, symbols

# Define the clauses
clauses = [
    expr('American(x) & Sells(x, y) & Hostile(y) ==> Criminal(x)'),  # Rule 1
    expr('Missile(x) & Owns(Nono, x) ==> Sells(Robert, x, Nono)'),  # Rule 2
    expr('Missile(x) ==> Weapon(x)'),  # Rule 3
    expr('EnemyOfAmerica(Nono) ==> Hostile(Nono)'),  # Rule 4
    expr('Owns(Nono, T1)'),  # Fact 1
    expr('Missile(T1)'),  # Fact 2
    expr('EnemyOfAmerica(Nono)'),  # Fact 3
    expr('American(Robert)'),  # Fact 4
]

# Initialize the knowledge base
KB = FolKB(clauses)

# Query the knowledge base
hostile = fol_bc_ask(KB, expr("Hostile(x)"))
criminal = fol_bc_ask(KB, expr("Criminal(x)"))

# Print the results
print('Who is hostile?')
print(list(hostile), '\n')

print('Who is a criminal?')
print(list(criminal))