def is_valid(left, right):
    if left == '(' and right == ')' or left == '[' and right == ']' or left == '{' and right == '}':
        return True  
    return False
  
def is_proper_nested(expression):
    stack = [] 
    for symbol in expression:
        if symbol == '[' or symbol == '{' or symbol == '(':
            stack.append(symbol)
        else:
            if len(stack) == 0:
                return False
            last = stack.pop()
            if not is_valid(last, symbol):
                return False
      
    if len(stack) != 0:
        return False          
    return True

