####    ###   #   #  #####  #####  #####   ###
#   #  #   #  #  #   #        #      #    #   #
####   #   #  ###    ####     #      #    #   #
#  #   #   #  #  #   #        #      #    #   #
#   #   ###   #   #  #####    #      #     ###
import random

inicio = 's'              ##//initial condition, 'r'=rear, 'f'=foward, 'e'= strategy, 's'=select strategy
left_speed = 0            ##//motor's variables
right_speed = 0           ##//motor's variables
speed = 40                ##//speed MAX set point
enemyPos = 1              ##//memory of enemy's position, 0=left, 1=center, 2=right
last = 1                  ##//last enemy's position memory
count = 1                 ##//counter
strategy = 0              ##//selected strategy
error = 0                 ##//error for strategy #2
action = 0                ##//action to complement strategy #2

def control(front_right, front_left, back_right, back_left, distance_right, distance_left):

    global inicio, left_speed, right_speed, speed, enemyPos, last, count, strategy, error, action
    
    if inicio == 's' : 
        strategy = random.randint(1,3)
        inicio = 'r'       
    
    
#####  #####  ####   #####  #####  #####  #####  #   #    ##
#        #    #   #  #   #    #    #      #       # #   ####
#####    #    ####   #####    #    ####   #  ##    #      ## 
    #    #    #  #   #   #    #    #      #   #    #      ##
#####    #    #   #  #   #    #    #####  #####    #    ##### 

    
    if strategy == 1 :    
    
    
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
         
            
##//--------- CALCULATE ENEMY'S POSITION -------------
        if count > 8 :
        
        
            enemyPos = distance_left - distance_right;
    
   
            if enemyPos >= 10 :
                enemyPos = 2 ##//enemy to the right
            elif enemyPos <= -10 :
                enemyPos = 0 ##//enemy to the left
            else :
                if last == 2 :
                    enemyPos = 2 ##// last enemy's position to the right
                elif last == 0 :
                    enemyPos = 0 ##// last enemy's position to the left
                else :
                    enemyPos = 1 ##//enemy in the center or lost enemy
    
            last = enemyPos    ##//capture the last enemy's position
        
        
        
##//---------------- VERIFICATIONS #1 ----------------  
    
            ##//if the back_sensor > 0.5, go to the 'foward'
            if back_left > 0.5 :
                left_speed = speed*1.0
                right_speed = speed*0.4
                inicio = 'f'
        
            ##// if the front_sensor > 0.0, go to 'strategy'    
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
    
            ##//if the enemy's position is '2', then the last position is 'right'     
            elif enemyPos == 2 :
                right_speed = speed*0.9
                left_speed = speed*1.0
        
            ##//if the enemy's position is '0', then the last position is 'left'    
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
            
        count += 1

        
#####  #####  ####   #####  #####  #####  #####  #   #  #####
#        #    #   #  #   #    #    #      #       # #      ##
#####    #    ####   #####    #    ####   #  ##    #    ##### 
    #    #    #  #   #   #    #    #      #   #    #    ## 
#####    #    #   #  #   #    #    #####  #####    #    ##### 


    elif strategy == 2 :


##//--------- CALCULATE ENEMY'S POSITION -------------
   
        error = distance_left - distance_right;
    
   
        if error > 0 :
            enemyPos = 2 ##//enemy to the right
        elif error < 0 :
            enemyPos = 0 ##//enemy to the left
        else:
            enemyPos = 1 ##//enemy in the center or lost enemy
            
    
       
        
            
##//--------- MAKE DECISIONS PART 1#2 ------------------        
 
        if enemyPos == 1 and distance_left == 300:
            if last == 2 :
                enemyPos = 2 ##// last enemy's position to the right
                error = 300 
            elif last == 0:
                enemyPos = 0 ##// last enemy's position to the left
                error = -300 
            else :
                ##//search for the enemy
                right_speed = speed * 0.0
                left_speed = speed * 1.0
        
        
        last = enemyPos    ##//capture the last enemy's position     
        
        
        ##//Check the back's sensors
        if (back_right > 0.9 or back_left > 0.9) and action != 'ok':
            right_speed = speed * 1.0
            left_speed = speed * 1.0
        ##//Check the front_left sensor
        if front_left > 0.9 and action != 'ok' :
            right_speed = speed * -1.0
            left_speed = speed * -1.0
            action = 'ok'
        ##//Check the front_right sensor
        elif front_right > 0.9 and action != 'ok' :
            right_speed = speed * -1.0
            left_speed = speed * -1.0
            action = 'ok'

##//--------- EVASIVE MANEUVER ------------------            
       
        ##//Evasive maneuver!!
        elif action == 'ok' :
            if count == 0 :
                if distance_left <= distance_right :
                    inicio = 'turnR'
                else:
                    inicio = 'turnL'
            
            if inicio == 'turnR' :
                if count < 27 :
                    right_speed = speed * -0.3
                    left_speed = speed * -1.0
                elif count < 63 :
                    right_speed = speed * 1.0
                    left_speed = speed * -1.0  
                else :
                    inicio = 'keepTurn'
            
            elif inicio == 'turnL' :
                if count < 27 :
                    right_speed = speed * -1.0
                    left_speed = speed * -0.3
                elif count < 63 :
                    right_speed = speed * -1.0
                    left_speed = speed * 1.0
                else :
                    inicio = 'keepTurn'
                    
            elif inicio == 'keepTurn' :
                if error < 10 and error > -10 : 
                    action = 'attack'
                else: 
                    left_speed = speed*(error/300)
                    right_speed = speed*-(error/300)
            
            count += 1
        

##//--------- MAKE DECISIONS PART 2 #2 ------------------
        
        ##//ROKETTO!! Evasive maneuver!! ref: POKÉMON
        elif distance_left < 50 and action == 0:
            action = 'ok'
            count = 0
        
        ##//counterattack (PODE MUDAR DE ESTRATÉGIA NO MEIO DA LUTA OU EXECUTAR UMA FUNÇÃO PRÓPRIA DA ESTRATÉGIA 2)   
        elif action == 'attack' : 
            if enemyPos == 2:
                right_speed = speed * 0.8
                left_speed = speed * 1.0
            elif enemyPos == 0:
                right_speed = speed * 1.0
                left_speed = speed * 0.8
                            
        ##//if the enemy's position is '2', then the last position is 'right'     
        elif enemyPos == 2 :
            right_speed = speed * -(error/300)
            left_speed = speed * (error/300)
        
        ##//if the enemy's position is '0', then the last position is 'left'    
        elif enemyPos == 0 :
            left_speed = speed*(error/300)
            right_speed = speed*-(error/300)            

            
#####  #####  ####   #####  #####  #####  #####  #   #  #####
#        #    #   #  #   #    #    #      #       # #      ##
#####    #    ####   #####    #    ####   #  ##    #    ##### 
    #    #    #  #   #   #    #    #      #   #    #       ## 
#####    #    #   #  #   #    #    #####  #####    #    ##### 
            
    elif strategy == 3 :
        right_speed = speed * 0.3
        left_speed = speed * 0.9
        count = count + 1
        if count >= 80:
            strategy = random.randint(1,2)
            if strategy == 1:
                inicio = 'e'
                count = 10
            else :
                action == 'attack'
        
##//OUTPUTS
    return { 
        'leftSpeed': left_speed,
        'rightSpeed': right_speed
    }
