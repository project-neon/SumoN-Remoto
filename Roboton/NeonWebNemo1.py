flag = 0 # 0 left | 1 right

MAX_SPEED = 40
NORMAL_SPEED = 35

def not_in_danger(front_right, front_left):
    return not (front_right > 0 or front_left > 0)


def control(front_right, front_left, back_right, back_left, distance_right, distance_left):
    global flag, MAX_SPEED, NORMAL_SPEED
    left_speed  = 0
    right_speed = 0
    
    if (not_in_danger(front_right, front_left)):
        if ( (distance_right < 300) or (distance_left < 300) ):
            left_speed = MAX_SPEED
            right_speed = MAX_SPEED
        elif ( (distance_right < 300) ):
            right_speed = NORMAL_SPEED
            flag = 1
        elif ( (distance_left < 300) ):
            left_speed = NORMAL_SPEED
            flag = 1
        else:
            left_speed = NORMAL_SPEED if flag == 0 else 0
            right_speed = NORMAL_SPEED if flag == 1 else 0
    else:
        left_speed = -MAX_SPEED
        right_speed = -MAX_SPEED
        
    return {
        'leftSpeed': left_speed,
        'rightSpeed': right_speed,
        'log': [
            { 'name': 'Front Left',  'value':   front_left,    'min': 0, 'max': 1 },
            { 'name': 'Front Right', 'value':   front_right,   'min': 0, 'max': 1 },
            { 'name': 'Distance Left', 'value': distance_left, 'min': 0, 'max': 300 },
            { 'name': 'Distance Right', 'value': distance_right, 'min': 0, 'max': 300 },
        ]
    }