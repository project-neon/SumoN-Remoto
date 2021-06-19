############ ------------ VERSION 09 ------------ ############

############ --------- START VARIABLES --------- ############
error = 0
sensorR = 0
sensorL = 0
inicio = 0
speedL = 0
speedR = 0
speed = 45
mem = 'r'        #variable used to 'mem'orize the position of the enemy 
                 # ---> 'm'=mid // 'r'=right // 'l'=left

############ --------- START OF THE PROGRAM --------- ############
def control(front_right, front_left, back_right, back_left, distance_right, distance_left):
 
    global error, sensorL, sensorR, inicio, speedL, speedR, speed, mem
    
    sensorR = distance_right
    sensorL = distance_left
    
    error = 0 - (distance_left-distance_right)
    
    speedR = speed * (error/300)
    speedL = speed * (error/300) * (-1)
        
    #checks the position of the enemy    
    if abs(error) <= 10 and (sensorR < 300 and sensorL < 300):
        mem='m'
    
    elif error > 0:
        mem='l'
        
    elif error < 0:
        mem='r'
        
    #search for the enemy    
    else:
        speedR = speed * -0.2
        speedL = speed * 0.9
        
    #rotates to the side where the enemy is
    if mem == 'l':
        speedR = speed * 0.8
        speedL = speed * 0.2
    
    elif mem == 'r':
        speedR = speed * 0.2
        speedL = speed * 0.8
    
    else: #mem = 'm'
        speedR = speed * 0.9
        speedL = speed * 0.9
        
    #checks if the robot has reached the edge by the 'front_sensor'    
    if front_left > 0.8 or front_right > 0.8:
        speedR = speed*-0.5
        speedL = speed*-0.9
        
    #goes back for 0.42 seconds, it happens only once
    if inicio < 25:
        speedR = speed * -0.9
        speedL = speed * -0.15
        inicio += 1
    
    #outputs
    return {
        'leftSpeed': speedL,
        'rightSpeed': speedR
    }