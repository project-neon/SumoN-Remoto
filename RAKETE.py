############ ------------ VERSION 07 ------------ ############

############ --------- START VARIABLES --------- ############
count = 30        #initial time counter (real time --> 'count'/60)
left_speed = 0
right_speed = 0
speed = 45

############ --------- START OF THE PROGRAM --------- ############
def control(front_right, front_left, back_right, back_left, distance_right, distance_left):
 
    global count, left_speed, right_speed, speed
    
    #initial condition, the robot goes back for 0,5 seconds   
    if count > 0 and (distance_left-distance_right) == 0:
        right_speed = speed*-0.7
        left_speed = speed*-0.8
        count -= 1
        
    #checks if the robot has reached the edge by the 'back_sensor'    
    elif back_left > 0:
        left_speed = speed*0.8
        right_speed = speed*0.5
    elif back_right > 0:
        left_speed = speed*0.5
        right_speed = speed*0.8
    
    #checks if the robot has reached the edge by the 'front_sensor'    
    elif front_right > 0:
        left_speed = speed*-0.8
        right_speed = speed*0.8
    elif front_left > 0:
        left_speed = speed*0.8
        right_speed = speed*-0.8
        
    #rotates to the side where the enemy is
    elif distance_left < 300:
        right_speed = speed*0.9
        left_speed = speed*0.7
    elif distance_right < 300:
        right_speed = speed*0.7
        left_speed = speed*0.9
        
    #search for the enemy    
    elif(abs(distance_right - distance_left))<=1:
        left_speed = speed*0.6
        right_speed = speed*-0.3
    
    #outputs
    return {
        'leftSpeed': left_speed,
        'rightSpeed': right_speed
    }
