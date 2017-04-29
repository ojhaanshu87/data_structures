# Enter your code here. Read input from STDIN. Print output to STDOUT
from ast import literal_eval

input_string = raw_input()

invalid_input_exception = False

if input_string.startswith(" ") or input_string.endswith(" "):
    invalid_input_exception = True

tokens = input_string.split(" ")

pairs = []
for token in tokens:
    try:
        tup = ast.literal_eval(token)
        
        if not (tup[0].isupper() and len(tup[0]) == 1 and tup[1].isupper() and len(tup[1]) == 1):
            raise Exception()
        
        pairs.append(tup)
    except:
        invalid_input_exception = True
        break
# E1 handle till        

#E2 start here
seen = []
duplicate = False
for pair in pairs:
    if pair in seen:
        duplicate = True
        break
        
    seen.append(pair)
#E2 end here

#E3 Strart here
parent_map = {}

more_than_two_children = False
for pair in pairs:
    if pair[0] in parent_map:
        parent_map[pair[0]].append(pair[1])
        
        if len(parent_map[pair[0]]) > 2:
            more_than_two_children = True
            break
    else:
        parent_map[pair[0]] = []
#E3 end here       

#E4 Start here

parent_map = {}
cycle = False

for pair in pairs:
    parent_map[pair[0]] = pair[1]
    
start = pairs[0][0]
temp_start = pairs[0][0]
while temp_start in parent_map:
    now = parent_map[start]
    
    if now == start:
        cycle = True
        break
        
    temp_start = now
#E4 End here

#E5 Start Here
child_map = {}
multiple_roots = False

for pair in pairs:
    if pair[1] in child_map:
        child_map[pair[1]].append(pair[0])
        
        if len(child_map[pair[1]]) > 1:
            multiple_roots = True
            break
            
    else:
        child_map[pair[1]] = []
        
#E5 end here
    
if invalid_input_exception:
    print "E1"
elif duplicate:
    print "E2"
elif more_than_two_children:
    print "E3"
elif cycle:
    print "E4"
elif multiple_roots:
    print "E5"
 

class Tree:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.key = val
        
        
    