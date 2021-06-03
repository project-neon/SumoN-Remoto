MAX_SPEED = 40
NORMAL_SPEED = 35

def searchEngine(distance_right, distance_left):
    if distance_right < 300 and distance_left == 300:
        # Opponent to the right => Turn right
        left_speed  =  40
        right_speed =  35
    elif distance_right == 300 and distance_left < 300:
        # Opponent to the left => Turn left
        left_speed  =  35
        right_speed =  40
    elif distance_right < 300 and distance_left < 300:
        # Opponent in front => Don't turn
        left_speed  = 40
        right_speed = 40
    elif distance_right == 300 and distance_left == 300:
        # Opponent lost => Search to the right
        left_speed  =  40
        right_speed = -40
    return left_speed, right_speed

def not_in_danger(front_right, front_left):
    return (front_right == 0 and front_left == 0)


def control(front_right, front_left, back_right, back_left, distance_right, distance_left):
    global MAX_SPEED, NORMAL_SPEED
    
    if (not_in_danger(front_right, front_left)):
        left_speed, right_speed = searchEngine(distance_right, distance_left)
    else:
        left_speed = -MAX_SPEED
        right_speed = -MAX_SPEED
        
    return {
        'leftSpeed': left_speed,
        'rightSpeed': right_speed,
        'log': [  ]
    }