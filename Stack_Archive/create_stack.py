def create_stack():
    stack = []
    return stack

def is_empty( stack ):
    return len(stack) == 0
 
def push( stack, item ):
    stack.append( item )
 
def pop( stack ):
 
    if(is_empty( stack )):
        print("Stack Underflow ")
        exit(1)
 
    return stack.pop()
 
def prints(stack):
    for i in range(len(stack)-1, -1, -1):
        print(stack[i])
    print()

 