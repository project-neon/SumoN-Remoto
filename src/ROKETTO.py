####    ###   #   #  #####  #####  #####   ###
#   #  #   #  #  #   #        #      #    #   #
####   #   #  ###    ####     #      #    #   #
#  #   #   #  #  #   #        #      #    #   #
#   #   ###   #   #  #####    #      #     ###

import random

inicio = 's'              ##//initial condition, 'r'=rear, 'f'=foward, 'e'=estrategy, 's'=select estrategy
left_speed = 0            ##//motor's variables
right_speed = 0           ##//motor's variables
speed = 40                ##//speed MAX set point
enemyPos = 1              ##//memory of enemy position, 0=left, 1=center, 2=right
last = 1                  ##//last enemy position memory
count = 1                 ##//counter
estrategy = 0             ##//selected estrategy


def control(front_right, front_left, back_right, back_left, distance_right, distance_left):

    global inicio, left_speed, right_speed, speed, enemyPos, last, count, estrategy
    
    if inicio == 's' : 
        estrategy = random.randint(1,1)
        inicio = 'r'       
    
    
#####  #####  #####  ####   #####  #####  #####  #####  #   #    ##
##     #        #    #   #  #   #    #    #      #       # #   ####
####   #####    #    ####   #####    #    ####   #  ##    #      ## 
##         #    #    #  #   #   #    #    #      #   #    #      ##
#####  #####    #    #   #  #   #    #    #####  #####    #    ##### 

    
    if estrategy == 1 :    
    
    
##//------- INITIAL CONDITION #1 ---------------
        
        ##//initial condition
        if inicio == 'r' :
            ##//go to te back
            left_speed = speed * -1
            right_speed = speed * -1
            inicio = 'e'
            return { 
                'leftSpeed': left_speed,
                'rightSpeed': right_speed
            }    
         
            
##//--------- CALCULATE ENEMY POSITION -------------
        if count > 8 :
        
        
            enemyPos = distance_left - distance_right;
    
   
            if enemyPos >= 10 :
                enemyPos = 2 ##//enemy to the right
            elif enemyPos <= -10 :
                enemyPos = 0 ##//enemy to the left
            else :
                if last == 2 :
                    enemyPos = 2 ##// last enemy position to the right
                elif last == 0 :
                    enemyPos = 0 ##// last enemy position to the left
                else :
                    enemyPos = 1 ##//enemy in the center or lost enemy
    
            last = enemyPos    ##//capture the last enemy position
        
        
        
##//---------------- VERIFICATIONS #1 ----------------  
    
            ##//if the back_sensor > 0.5, go to the 'foward'
            if back_left > 0.5 :
                left_speed = speed*1.0
                right_speed = speed*0.4
                inicio = 'f'
        
            ##// if the front_sensor > 0.0, go to 'estrategy'    
            elif front_right > 0 :
                ##//turn to the left
                left_speed = speed*-0.984
                right_speed = speed*0.984
                inicio = 'e'
                last = 1 ##//'last' changed
            elif front_left > 0 :
                ##//turn to the right
                right_speed = speed*-0.984
                left_speed = speed*0.984
                inicio = 'e'
                last = 1 ##//'last' changed

##//--------- MAKE DECISIONS #1 ------------------        
    
            ##//if the enemy position is '2', then the last position is 'right'     
            elif enemyPos == 2 :
                right_speed = speed*0.9
                left_speed = speed*1.0
        
            ##//if the enemy position is '0', then the last position is 'left'    
            elif enemyPos == 0 :
                left_speed = speed*0.9
                right_speed = speed*1.0

##//----------- ATTACK, MAYBE #1 ----------------- 
        
            ##//if the enemy is ahead
            elif enemyPos == 1 and distance_left < 300 :
                ##// go! go! go! more faster!!!!!
                left_speed = speed*1.0;
                right_speed = speed*1.0;
        
            ##//if 'inicio' = 'f', o to the foward    
            elif inicio == 'f' :
                ##//turn looking for enemy
                left_speed = speed*1.0
                right_speed = speed*-1.0
            
        count=1+count
        
        
##//OUTPUTS
    return { 
        'leftSpeed': left_speed,
        'rightSpeed': right_speed
    }