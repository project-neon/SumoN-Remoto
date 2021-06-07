inicio = 0
left_speed = 0
right_speed = 0
speed = 45


def control(front_right, front_left, back_right, back_left, distance_right, distance_left):
    
    global inicio, left_speed, right_speed, speed
    
    
    if back_left > 0 :
        right_speed = speed*0.6
        left_speed = speed*0.8
        inicio = 1
    elif back_right > 0:
        left_speed = speed*0.6
        right_speed = speed*0.8
        inicio = 1
    elif inicio == 0:
        right_speed = -speed*0.8
        left_speed = -speed*0.6
    elif front_right > 0:
        left_speed = speed*-0.8
        right_speed = speed*-0.7
    elif front_left > 0:
        right_speed = speed*-0.8
        left_speed = speed*-0.7
    elif distance_left < 300:
        right_speed = speed*0.9
        left_speed = speed*0.9
    elif distance_right < 300:
        left_speed = speed*0.9
        right_speed = speed*0.9
    elif((-1)*(distance_right - distance_left))<=20:
        left_speed = speed*0.8
        right_speed = speed*-0.0
    
    return {
        'leftSpeed': left_speed,
        'rightSpeed': right_speed,
        'log': [
            { 'name': 'Front Left',  'value':   front_left,    'min': 0, 'max': 1 },
            { 'name': 'Front Right', 'value':   front_right,   'min': 0, 'max': 1 },
            { 'name': 'Distance Left', 'value': distance_left, 'min': 0, 'max': 300 }
        ]
    }