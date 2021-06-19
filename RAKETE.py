############ ------------ VERSION 11 ------------ ############

############ ---------- START VARIABLES --------- ############
inicio = 'r'        #initial condition, 'r'=rear, 'f'=forward, 'e'=estrategy
left_speed = 0
right_speed = 0
speed = 45
enemyPos = 1        #enemy position, '0'=left, '1'=center, '2'=right
last = 1            #last enemy position

############ --------- START OF THE PROGRAM --------- ############
def control(front_right, front_left, back_right, back_left, distance_right, distance_left):
 
    global inicio, left_speed, right_speed, speed, enemyPos, last
    
##########################################    
#   DISCOVER THE POSITION OF THE ENEMY   #
##########################################

    enemyPos = distance_left - distance_right
    
    if enemyPos >= 10:
        enemyPos = 2        #enemy is in the righ
        
    elif enemyPos <= -10:
        enemyPos = 0        #enemy is in the left

    else:
        if last == 2:
            enemyPos = 2    #last enemy position to the right
        elif last == 0:
            enemyPos = 0    #last enemy position to the left
        else:
            enemyPos = 1    #enemy is in the center or lost enemy

    last = enemyPos         #capture the last enemy position
    
##########################################    
#             VERIFICATIONS              #
##########################################

    #checks if the robot has reached the edge by the 'back_sensor'
    if back_left > 0.5:
        right_speed = speed*0.7
        left_speed = speed*0.9
        inicio = 'f';    
        
    #checks if the robot has reached the edge by the 'front_sensor'
    elif front_right > 0.5:
        right_speed = speed*0.875
        left_speed = speed*-0.875
        inicio = 'e'
        last = 1
    elif front_left > 0.5:
        right_speed = speed*-0.875
        left_speed = speed*0.875
        inicio = 'e'
        last = 1

##########################################    
#             MAKE DECISIONS             #
##########################################
    
    #rotates to the side where the enemy is
    elif enemyPos == 2:
        right_speed = speed*0.9
        left_speed = speed*0.9
        
    elif enemyPos == 0:
        right_speed = speed*0.85
        left_speed = speed*0.9    
        
#########################################   
#           INITIAL CONDITION           #
#########################################
    
    #goes back
    elif inicio == 'r':
        left_speed = speed * -0.9
        right_speed = speed * -0.9
    
    #goes forward, turns looking for the enemy
    elif inicio == 'f':
        left_speed = speed * 0.9
        right_speed = speed * -0.9
    
###########################################   
#                 OUTPUTS                 #
###########################################

    return {
        'leftSpeed': left_speed,
        'rightSpeed': right_speed
    }
