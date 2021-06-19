############ ------------ VERSION 05 ------------ ############

############ --------- START VARIABLES --------- ############
inicio = 0
left_speed = 0
right_speed = 0
speed = 45

############ --------- START OF THE PROGRAM --------- ############
def control(front_right, front_left, back_right, back_left, distance_right, distance_left):
    
    global inicio, left_speed, right_speed, speed
    
    #checks if the robot has reached the edge by the 'back_sensor'
    if back_left > 0 or back_right > 0:
        right_speed = speed*1.0
        left_speed = speed*1.0
        inicio = 1
        
    #initial condition, the robot goes back    
    elif inicio == 0 and (distance_left == 300 and distance_right == 300):
        right_speed = speed*-0.9
        left_speed = speed*-0.6
        
    #checks if the robot has reached the edge by the 'front_sensor'    
    elif front_right > 0 or front_left > 0:
        left_speed = speed*0.9
        right_speed = speed*-0.9
        inicio = 1
        
    #Go forward when you spot the enemy
    elif (distance_left < 300 and distance_right < 300) and (distance_left-distance_right) < 10:
        right_speed = speed*0.9
        left_speed = speed*0.9
    elif distance_left < 300 or distance_right < 300:
        right_speed = speed*0.8
        left_speed = speed*0.8
        
    #search for the enemy    
    elif(abs(distance_right - distance_left))<=20:
        left_speed = speed*0.6
        right_speed = speed*-0.5
    
    #outputs
    return {
        'leftSpeed': left_speed,
        'rightSpeed': right_speed
    }
