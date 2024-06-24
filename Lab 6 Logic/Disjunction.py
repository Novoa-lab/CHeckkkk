from logic import FolKB, expr

clauses = []
clauses.append(expr("Likes(John, Pizza)"))  # Individual atomic formula
clauses.append(expr("Likes(Mary, Pizza)"))  # Individual atomic formula

# Create a first-order logic knowledge base (KB) with clauses
KB = FolKB(clauses)

# Query the knowledge base
result = KB.ask(expr('Likes(John, x)'))

# Print the result
print('What does John like?')
print(result)

