############ ------------ VERSION 08 ------------ ############

############ --------- START VARIABLES --------- ############
inicio = 0
left_speed = 0
right_speed = 0
speed = 45
error = 0

############ --------- START OF THE PROGRAM --------- ############
def control(front_right, front_left, back_right, back_left, distance_right, distance_left):
 
    global count, left_speed, right_speed, speed, error
    
    error = 0 - (distance_left-distance_right)
        
    #checks if the robot has reached the edge by the 'front_sensor'    
    if front_right > 0.8 or front_left > 0.8:
        left_speed = speed*0.9
        right_speed = speed*-0.9
        
    #rotates to the side where the enemy is
    elif abs(error) <= 10 and distance_left < 300:
        right_speed = speed*1.0
        left_speed = speed*1.0
        
    elif error > 0:
        right_speed = 0.9*speed*(error/300)
        left_speed = 0.45*speed*(error/300)
        
    elif error < 0:
        error = abs(error)
        right_speed = 0.45*speed*(error/300)
        left_speed = 0.9*speed*(error/300)
        
    elif distance_left < 300 or distance_right < 300:
        right_speed = speed*0.8
        left_speed = speed*0.8
        
    #search for the enemy    
    elif(abs(error))<=20:
        left_speed = speed*0.7
        right_speed = speed*-0.1
    
    #outputs
    return {
        'leftSpeed': left_speed,
        'rightSpeed': right_speed
    }
