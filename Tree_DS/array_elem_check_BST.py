# 1) Create an empty stack.
# 2) Initialize root as INT_MIN.
# 3) Do following for every element pre[i]
#      a) If pre[i] is smaller than current root, return false.
#      b) Keep removing elements from stack while pre[i] is greater
#         then stack top. Make the last removed item as new root (to
#         be compared next).
#         At this point, pre[i] is greater than the removed root
#         (That is why if we see a smaller element in step a), we 
#         return false)
#      c) push pre[i] to stack (All elements in stack are in decreasing
#         order)  

INT_MIN = -2**32
 
def can_rep_bst(preorder_traversal):
    # Create an empty stack
    s = []
    # Initialize current root as minimum possible value
    root = INT_MIN
    # Traverse given array
    for elem in preorder_traversal: 
        #NOTE:value is equal to pre[i] according to the 
        #given algo   
     
        # If we find a node who is on the right side
        # and smaller than root, return False
        if elem < root :
            return False
     
        # If value(pre[i]) is in right subtree of stack top, 
        # Keep removing items smaller than value
        # and make the last removed items as new root
        while(len(s) > 0 and s[-1] < elem) :
            root = s.pop()
         
        # At this point either stack is empty or value
        # is smaller than root, push value
        s.append(elem)
 
    return True
 
# Driver Program
preorder_traversal1 = [40 , 30 , 35 , 80 , 100]
print "true" if can_rep_bst(preorder_traversal1) == True else "false"
preorder_traversal2 = [40 , 30 , 35 , 20 ,  80 , 100]
print "true" if can_rep_bst(preorder_traversal2) == True else "false"