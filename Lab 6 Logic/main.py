from logic import *
from utils import *

clauses = []
clauses.append(expr("(American(x) & Weapon(y) & Sells(x, y, z) & Hostile(z)) ==> Criminal(x)"))
clauses.append(expr("Owns(nono, T1)"))
clauses.append(expr("Missile(T1)"))
clauses.append(expr("(Missile(x) & Owns(nono, x)) ==> Sells(Robert, x, nono)"))
clauses.append(expr("Missile(x) ==> Weapon(x)"))
clauses.append(expr("Enemy(nono, America)  ==> Hostile(x) "))
clauses.append(expr("Enemy(nono, America)"))
clauses.append(expr("American(Robert)"))


# Create a first-order logic knowledge base (KB) with clauses
KB = FolKB(clauses)

# Add rules and facts with tell



# Get information from the knowledge base with ask
hostile = KB.ask(expr('Hostile(x)'))
criminal = KB.ask(expr('Criminal(x)'))

# Print answers
print('Hostile?')
print(hostile)
print('\nCriminal?')
print(criminal)
print()
