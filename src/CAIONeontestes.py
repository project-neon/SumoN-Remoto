flag = 1 # 0 esquerda | 1 direita - para onde foi o inimigo
         # 0 left | 1 right, It help us to know where the enemy went


counter = 0
inicio = 0

MAX_SPEED = 40
NORMAL_SPEED = 35


def search_engine(distance_right, distance_left):

    """
    Function below: Will search for the opponent rotating, 
    and after finding it, the robot will go straight 
    função de procura rodando no próprio eixo, ataca a frente se há detecção
    """
    
    global flag, MAX_SPEED, NORMAL_SPEED
    
    if distance_right < 300 and distance_left == 300:
        # Opponent to the right => Turn right
        left_speed  =  MAX_SPEED*0.9
        right_speed =  NORMAL_SPEED*0.9
        flag = 1
    elif distance_right == 300 and distance_left < 300:
        # Opponent to the left => Turn left
        left_speed  =  NORMAL_SPEED*0.8
        right_speed =  MAX_SPEED*0.8
        flag = 0
        
    elif distance_right < 300 and distance_left < 300:
        # Opponent in front => Go
        left_speed  = MAX_SPEED*100
        right_speed = MAX_SPEED*100
        
    else:# Lost the opponent
        if flag == 0: #Last time seen was to the left
            left_speed  = NORMAL_SPEED*0.4
            right_speed = NORMAL_SPEED
        else: #Last time seen was to the right
            left_speed  = NORMAL_SPEED
            right_speed = NORMAL_SPEED*0.4
    return left_speed, right_speed



def not_in_danger(front_right, front_left, back_right, back_left):

    """"
    # Will see if the sensor of the robot is above the white line (borders
    // checa se está na linha branca
    # Will return True or False // retorna verdadeiro ou falso
    """
    
    if(front_right < 0.8 and front_left < 0.8): #check if it's safe // checar se está seguro
        
        return (True) 



def control(front_right, front_left, back_right, back_left, distance_right, distance_left):
    
    """
    # Main function that will loop 60 times in a second
    // função principal rodará 60 frames por segundo  
    """
    
    
    global counter, inicio, flag, MAX_SPEED, NORMAL_SPEED
    
    #Time counter function, might come in handy || descontinuada  
    #if counter >= 25: 
    #    counter += 1
    
    ###Initial retreat conditions block for maneuvering### // condição inicial de retirada ("ré")
    if (counter < 25): #time-frames for reaching edge // frames-de-tempo para alcançar a borda
        right_speed = -MAX_SPEED
        left_speed = -MAX_SPEED
        counter += 1
   
    elif back_left > 0: 
            right_speed = MAX_SPEED*0.5
            left_speed = MAX_SPEED*0.8
            inicio = 1
            
    elif back_right > 0:
            left_speed = MAX_SPEED*0.5
            right_speed = MAX_SPEED*0.8
            inicio = 1
            
    #alternative begin strategy, discontinued
    #elif inicio == 0:
       #     right_speed = -MAX_SPEED
        #    left_speed = -MAX_SPEED
    
    ###Current maneuver: retreat and reposition###
    
    # Everything is fine, so it will search for the enemy and attack it
    # // Está tudo seguro, o robô procurará o inimigo e atacará
    elif (not_in_danger(front_right, front_left, distance_right, distance_left)):
        left_speed, right_speed = search_engine(distance_right, distance_left)
    else:
    # The robot is in danger, so it got to go back with all speed (reverse) 
    # // O robô está em perigo, então irá recuar 

        left_speed, right_speed  = -MAX_SPEED, -MAX_SPEED
        
    return {
        'leftSpeed': left_speed,
        'rightSpeed': right_speed,
        'log': [ 
        
            { 'name': 'Timer',  'value':   counter,    'min': 0, 'max': 600 }
          # { 'name': 'Front Right', 'value':   front_right,   'min': 0, 'max': 1 }
          # { 'name': 'Distance Left', 'value': distance_left, 'min': 0, 'max': 300 }
        
        ]
    }