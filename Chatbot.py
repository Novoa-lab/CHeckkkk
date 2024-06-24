import re
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

def parse_variables(problem_statement):
    found_vars = re.findall(r'(\w+) is (\d+)', problem_statement)
    variables_dict = {var: int(val) for var, val in found_vars}
    print("Extracted Variables:", variables_dict)
    return variables_dict

def calculate_answer(problem_statement, variables_dict):
    tokenized_statement = word_tokenize(problem_statement.lower())
    print("Tokenized Problem:", tokenized_statement)
    
    if 'twice' in tokenized_statement:
        if 'of' in tokenized_statement:
            target_variable = tokenized_statement[tokenized_statement.index('of') + 1]
        else:
            target_variable = tokenized_statement[-1].rstrip('?')
        print("Target Variable for 'twice':", target_variable)
        return 2 * variables_dict[target_variable]
    elif 'half' in tokenized_statement or 'one half' in tokenized_statement:
        if 'of' in tokenized_statement:
            target_variable = tokenized_statement[tokenized_statement.index('of') + 1]
        else:
            target_variable = tokenized_statement[-1].rstrip('?')
        print("Target Variable for 'half':", target_variable)
        return variables_dict[target_variable] / 2
    elif 'square' in tokenized_statement:
        target_variable = tokenized_statement[-1].rstrip('?')
        print("Target Variable for 'square':", target_variable)
        return variables_dict[target_variable] ** 2
    elif 'minus' in tokenized_statement or '-' in tokenized_statement or 'difference' in tokenized_statement:
        var1 = tokenized_statement[tokenized_statement.index('between') + 1] if 'difference' in tokenized_statement else tokenized_statement[tokenized_statement.index('minus') - 1]
        var2 = tokenized_statement[-1].rstrip('?')
        print("Variables for 'minus':", var1, var2)
        return variables_dict[var1] - variables_dict[var2]
    elif 'plus' in tokenized_statement or '+' in tokenized_statement or 'sum' in tokenized_statement:
        var1 = tokenized_statement[tokenized_statement.index('sum') + 1] if 'sum' in tokenized_statement else tokenized_statement[tokenized_statement.index('plus') - 1]
        var2 = tokenized_statement[-1].rstrip('?')
        print("Variables for 'plus':", var1, var2)
        return variables_dict[var1] + variables_dict[var2]
    elif 'times' in tokenized_statement or '*' in tokenized_statement or 'product' in tokenized_statement:
        var1 = tokenized_statement[tokenized_statement.index('product') + 1] if 'product' in tokenized_statement else tokenized_statement[tokenized_statement.index('times') - 1]
        var2 = tokenized_statement[-1].rstrip('?')
        print("Variables for 'times':", var1, var2)
        return variables_dict[var1] * variables_dict[var2]
    elif 'divided by' in tokenized_statement or '/' in tokenized_statement or 'per' in tokenized_statement:
        var1 = tokenized_statement[tokenized_statement.index('divided by') - 1] if 'divided by' in tokenized_statement else tokenized_statement[tokenized_statement.index('/') - 1]
        var2 = tokenized_statement[-1].rstrip('?')
        print("Variables for 'divided by':", var1, var2)
        return variables_dict[var1] / variables_dict[var2]
    elif '%' in tokenized_statement:
        if 'less than' in tokenized_statement:
            var1 = tokenized_statement[tokenized_statement.index('%') - 1]
            var2 = tokenized_statement[tokenized_statement.index('less than') + 2]
            print("Variables for '% less than':", var1, var2)
            return variables_dict[var2] - (variables_dict[var2] * int(var1) / 100)
        elif 'more than' in tokenized_statement:
            var1 = tokenized_statement[tokenized_statement.index('%') - 1]
            var2 = tokenized_statement[tokenized_statement.index('more than') + 2]
            print("Variables for '% more than':", var1, var2)
            return variables_dict[var2] + (variables_dict[var2] * int(var1) / 100)
        else:
            var1 = int(tokenized_statement[tokenized_statement.index('%') - 1])
            var2 = tokenized_statement[tokenized_statement.index('of') + 1]
            print("Variables for '%':", var1, var2)
            return (variables_dict[var2] / var1) * 100

    return "I can't solve this problem."

def math_chatbot(problem_statement):
    variables_dict = parse_variables(problem_statement)
    answer = calculate_answer(problem_statement, variables_dict)
    return answer

def main():
    print("Welcome to the MathBot. Please enter your question:")
    while True:
        problem_statement = input("You: ")
        if problem_statement.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        answer = math_chatbot(problem_statement)
        print(f"Chatbot: {answer}")

if __name__ == "__main__":
    main()

