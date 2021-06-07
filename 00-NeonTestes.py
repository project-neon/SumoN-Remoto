flag = 1 # 0 left | 1 right, It help us to know where the enemy went

counter = 0
inicio = 0

MAX_SPEED = 40
NORMAL_SPEED = 35

#Will search for the opponent rotating, and after finding it, 
#it will go straight


def searchEngine(distance_right, distance_left):
    global flag, MAX_SPEED, NORMAL_SPEED
    
    if distance_right < 300 and distance_left == 300:
        # Opponent to the right => Turn right
        left_speed  =  40
        right_speed =  35
        flag = 1
    elif distance_right == 300 and distance_left < 300:
        # Opponent to the left => Turn left
        left_speed  =  40
        right_speed =  35
        flag = 0
    elif distance_right < 300 and distance_left < 300:
        # Opponent in front => Go
        left_speed  = 40
        right_speed = 40
    else:# Lost the opponent
        if flag == 0: #Last time seen was to the left
            left_speed  = 0
            right_speed = 35
        else: #Last time seen was to the right
            left_speed  = 35
            right_speed = 0
    return left_speed, right_speed

# Will see if the sensor of the robot is above the white line (borders)
# Will return True or False
def not_in_danger(front_right, front_left):
    return (front_right == 0 and front_left == 0)

# Main function that will loop 60 times in a second
def control(front_right, front_left, back_right, back_left, distance_right, distance_left):
    
    global counter, inicio, flag, MAX_SPEED, NORMAL_SPEED
        
    if counter >= 0: #Time counter function, might come in handy
        counter += 1
    
    #Initial retreat conditions block for maneuvering
    if back_left > 0: 
            right_speed = MAX_SPEED*0.5
            left_speed = MAX_SPEED*0.8
            inicio = 1
            
    elif back_right > 0:
            left_speed = MAX_SPEED*0.5
            right_speed = MAX_SPEED*0.8
            inicio = 1
            
    elif inicio == 0:
            right_speed = -MAX_SPEED
            left_speed = -MAX_SPEED
    # Current maneuver: retreat and reposition            
    
    # Everything is fine, so it will search for the enemy and attack it
    elif (not_in_danger(front_right, front_left)):
        left_speed, right_speed = searchEngine(distance_right, distance_left)
    else:
    # The robot is in danger, so it got to go back with all speed (reverse)    

        left_speed, right_speed  = -MAX_SPEED, -MAX_SPEED
        
    return {
        'leftSpeed': left_speed,
        'rightSpeed': right_speed,
        'log': [ 
        
            { 'name': 'Timer',  'value':   counter,    'min': 0, 'max': 600 }
          # { 'name': 'Front Right', 'value':   front_right,   'min': 0, 'max': 1 }
          # { 'name': 'Distance Left', 'value': distance_left, 'min': 0, 'max': 300 }
        
        ]
    }