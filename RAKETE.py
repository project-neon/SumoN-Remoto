############ ------------ VERSION 10 ------------ ############

############ --------- START VARIABLES --------- ############
inicio = 0
left_speed = 0
right_speed = 0
speed = 45

############ --------- START OF THE PROGRAM --------- ############
def control(front_right, front_left, back_right, back_left, distance_right, distance_left):
 
    global inicio, left_speed, right_speed, speed
    
    #checks if the robot has reached the edge by the 'back_sensor'
    if back_left > 0 :
        right_speed = speed*0.6
        left_speed = speed*0.8
        inicio = 1
    elif back_right > 0:
        left_speed = speed*0.6
        right_speed = speed*0.8
        inicio = 1
    
    #initial condition, the robot goes back
    elif inicio == 0:
        right_speed = -speed*0.8
        left_speed = -speed*0.6
        
    #checks if the robot has reached the edge by the 'front_sensor'
    elif front_right > 0:
        left_speed = speed*-0.8
        right_speed = speed*-0.7
    elif front_left > 0:
        right_speed = speed*-0.8
        left_speed = speed*-0.7
    
    #rotates to the side where the enemy is
    elif distance_left < 300:
        right_speed = speed*0.9
        left_speed = speed*0.9
    elif distance_right < 300:
        left_speed = speed*0.9
        right_speed = speed*0.9
    elif((-1)*(distance_right - distance_left))<=20:
        left_speed = speed*0.8
        right_speed = speed*-0.0    
    
    #outputs
    return {
        'leftSpeed': left_speed,
        'rightSpeed': right_speed
    }