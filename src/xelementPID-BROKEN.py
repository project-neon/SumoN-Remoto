flag = 1 # 0 left | 1 right, It help us to know where the enemy went

counter = 0
inicio = 0

MAX_SPEED = 38
NORMAL_SPEED = 34

error = 0 

I_erro = 0
D_erro = 0
speed_setpoint = 0
Kp = 0.1
Ki = 0.001
Kd = 0.001

tempo = 0

tempo_prev = 0

ajuste = 0

def proportionalIntegralController(Kp, Ki, Kd, ajustemax=0, ajustenrml=0):
    # initialize stored data
    global MAX_SPEED, NORMAL_SPEED
    e1_prev = 0
    e2_prev = 0
    tempo_prev = -10
    I1 = 0
    I2 = 0
    
    # initial control
    MAX_SPEED = MAX_SPEED + ajustemax
    NORMAL_SPEED = NORMAL_SPEED + ajustenrml    
    
    for i in range(0,20):        ##while True:
        # yield ajuste, wait for new t, PV, SP

        tempo, left_speed, right_speed, MAX_SPEED, NORMAL_SPEED = yield ajustemax, ajustenrml
        
        # PID calculations
        e1 = NORMAL_SPEED - abs(left_speed - right_speed)
        e2 = MAX_SPEED - abs(left_speed - right_speed)
        
        P1 = Kp*e1
        P2 = Kp*e2
        
        I1 = I1 + Ki*e1*(tempo - tempo_prev)
        I2 = I2 + Ki*e2*(tempo - tempo_prev)
        
        D1 = Kd*(e1 - e1_prev)/(tempo - tempo_prev)
        D2 = Kd*(e2 - e2_prev)/(tempo - tempo_prev)
        
        ajustemax = ajuste + P1 + I1 + D1
        ajustenrml = ajuste + P2 + P2 + D2
        
        # update stored data for next iteration
        e1_prev = e1
        e2_prev = e2 
        tempo_prev = tempo


#Function below: Will search for the opponent rotating, 
#and after finding it, the robot will go straight 
## // função de procura rodando no próprio eixo, ataca a frente se há detecção

def searchEngine(distance_right, distance_left):
    global flag, MAX_SPEED, NORMAL_SPEED, error, ajustemax, ajustenrml
    
    if distance_right < 300 and distance_left == 300:
        # Opponent to the right => Turn right
        left_speed  =  (MAX_SPEED+ajustemax)
        right_speed =  (NORMAL_SPEED+ajustenrml) 
        flag = 1
    elif distance_right == 300 and distance_left < 300:
        # Opponent to the left => Turn left
        left_speed  =  (NORMAL_SPEED+ajustenrml)
        right_speed =  (MAX_SPEED+ajustemax)
        flag = 0
        
    elif distance_right < 300 and distance_left < 300:
        # Opponent in front => Go
        left_speed  = MAX_SPEED*100
        right_speed = MAX_SPEED*100
        
    else:# Lost the opponent
        if flag == 0: #Last time seen was to the left
            left_speed  = (NORMAL_SPEED+ajustenrml)
            right_speed = (MAX_SPEED+ajustemax)
        else: #Last time seen was to the right
            left_speed  = (MAX_SPEED+ajustemax)
            right_speed = (NORMAL_SPEED+ajustenrml)
    return left_speed, right_speed


# Will see if the sensor of the robot is above the white line (borders) // checa se está na linha branca
# Will return True or False // retorna verdadeiro ou falso
def not_in_danger(front_right, front_left, back_right, back_left):

    if(front_right < 0.8 and front_left < 0.8): #check if it's safe // checar se está seguro
        
        return (True) 


# Main function that will loop 60 times in a second // função principal rodará 60 frames por segundo
def control(front_right, front_left, back_right, back_left, distance_right, distance_left):
    
    global counter, inicio, flag, MAX_SPEED, NORMAL_SPEED, tempo, ajustemax, ajustenrml
    
     #Time counter function, might come in handy || descontinuada  
   # if counter >= 25: 
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
        left_speed, right_speed = searchEngine(distance_right, distance_left)
    else:
    # The robot is in danger, so it got to go back with all speed (reverse) 
    # // O robô está em perigo, então irá recuar 

        left_speed, right_speed  = -MAX_SPEED, -MAX_SPEED

    tempo += tempo
        
    return {
        'leftSpeed': left_speed,
        'rightSpeed': right_speed,
        'log': [ 
        
            { 'name': 'Timer',  'value':   counter,    'min': 0, 'max': 600 }
          # { 'name': 'Front Right', 'value':   front_right,   'min': 0, 'max': 1 }
          # { 'name': 'Distance Left', 'value': distance_left, 'min': 0, 'max': 300 }
        
        ]
    }