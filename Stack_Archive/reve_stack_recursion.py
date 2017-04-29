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

def inserrt_at_bottom(stack, item):
    if is_empty(stack):
        push(stack, item)
    else:
        temp = pop(stack)
        inserrt_at_bottom(stack, item)
        push(stack, temp)
 
def reverse(stack):
    if not is_empty(stack):
        temp = pop(stack)
        reverse(stack)
        inserrt_at_bottom(stack, temp)

# stack = create_stack()
# push( stack, str(4) )
# push( stack, str(3) )
# push( stack, str(2) )
# push( stack, str(1) )
# print("Original Stack ")
# prints(stack)
 
# reverse(stack)
 
# print("Reversed Stack ")
# prints(stack)