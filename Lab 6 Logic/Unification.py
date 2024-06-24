from logic import unify
from utils import expr

print(unify(expr('x'), 3))

print(unify(expr('A(x)'), expr('A(B)')))

print(unify(expr('Cat(x) & Dog(Dobby)'), expr('Cat(Bella) & Dog(y)')))


