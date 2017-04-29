def create_stack():
	stack =[]
	return stack

def is_empty (stack):
	return len(stack) ==0

def push (stack, elem):
	stack.append(elem)
	
def pop(stack):
    if (is_empty(stack)):
    	exit (1)
    return stack.pop()

def next_greater_elem(arr):
    stack = create_stack()
    element = 0
    next = 0
    push(stack, arr[0])
    for i in range(1, len(arr), 1):
        next = arr[i]
 
        if is_empty(stack) == False:
            element = pop(stack)
            while element < next :
                print(str(element)+ " -- " + str(next))
                if is_empty(stack) == True :
                    break
                element = pop(stack)
            if  element > next:
                push(stack, element)
        push(stack, next)
    while is_empty(stack) == False:
            element = pop(stack)
            next = -1
            print(str(element) + " -- " + str(next))
