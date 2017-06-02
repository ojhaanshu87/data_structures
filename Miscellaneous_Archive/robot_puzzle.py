'''  
Find the distance of robot after some moves from origin point.

SAMPLE INPUT :
UP 5
DOWN 3
LEFT 3
RIGHT 2

SAMPLE OUTPUT :
2
'''


import math

def robot_move(input_text_file):

    start_x = 0
    start_y = 0
    #next two line is origin point of robot
    current_x = start_x
    current_y = start_y
    
    #read the text file
    with open(input_text_file) as file:
        movements = file.readlines()
        #iterate over file at each line
        for movement in movements:
            movement = movement.strip('\n').split(' ')
            direction, steps = movement[0], movement[1]

            if direction == 'UP':
                current_y += int(steps)
            elif direction == 'DOWN':
                current_y -= int(steps)
            elif direction == 'RIGHT':
                current_x += int(steps)
            elif direction == 'LEFT':
                current_x -= int(steps)

        file.close()
    #calculate distance
    distance = math.sqrt(current_x*current_x + current_y*current_y)
    return(int(distance))