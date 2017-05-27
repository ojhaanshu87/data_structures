"""The Tower of Hanoi (also called the Tower of Brahma or Lucas' Tower,[1] and sometimes pluralised) 
is a mathematical game or puzzle. 
It consists of three rods, and a number of disks of different sizes which can slide onto any rod. 
The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest 
at the top, thus making a conical shape.
The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
  1. Only one disk can be moved at a time.
  2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another 
  stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
  3. No disk may be placed on top of a smaller disk."""



def move_disk(first_pole,to_pole,height):
    print("    "*(4-height), "moving disk", "~"*(height), "from",first_pole,"to",to_pole)

def move_tower(height,from_pole, to_pole, with_pole):
    if height >= 1:
        print( "    "*(3-height), "move_tower:", height, from_pole, to_pole )
        move_tower(height-1,from_pole,with_pole,to_pole)
        move_disk(from_pole,to_pole,height)
        move_tower(height-1,with_pole,to_pole,from_pole)
    #print(with_pole)

move_tower(3,"A","B","C")