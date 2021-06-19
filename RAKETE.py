############ ------------ VERSION 06 ------------ ############

############ --------- START VARIABLES --------- ############
inicio = 0
left_speed = 0
right_speed = 0
speed = 45

############ --------- START OF THE PROGRAM --------- ############
def control(front_right, front_left, back_right, back_left, distance_right, distance_left):
 
    global inicio, left_speed, right_speed, speed
    
    #initial condition, the robot goes forward   
    if inicio == 0 and (distance_left == 300 and distance_right == 300):
        right_speed = speed*0.9
        left_speed = speed*0.6
        inicio = 1
        
    #checks if the robot has reached the edge by the 'front_sensor'    
    elif front_right > 0:
        left_speed = speed*0.8
        right_speed = speed*-0.9
        inicio = 1
    elif front_left > 0:
        left_speed = speed*0.7
        right_speed = speed*-0.9
        inicio = 1
        
    #rotates to the side where the enemy is
    elif distance_left < 300:
        right_speed = speed*0.9
        left_speed = speed*0.4
    elif distance_right < 300:
        right_speed = speed*0.4
        left_speed = speed*0.9
        
    #search for the enemy    
    elif(abs(distance_right - distance_left))<=20:
        left_speed = speed*0.9
        right_speed = speed*0.7
    
    #outputs
    return {
        'leftSpeed': left_speed,
        'rightSpeed': right_speed
    }