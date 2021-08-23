flag = 0 # 0 esquerda | 1 direita - para onde foi o inimigo
         # 0 left | 1 right, It help us to know where the enemy went

sInitial = 0        ##//initial distance // distância inicial 
sFinal = 0          ##//final distance // distância final  
tInitial = 0        ##//initial time // tempo inicial
tFinal = 1/30          ##//final time // tempo final
speedOp = 0         ##//opponent's speed in 'm/s' (meters per second) // velocidade do oponente em 'm/s' (metros por segundo)
timer = 1/60        ##//time in seconds -> (1/60)* // tempo em segundos -> (1/60)*
##// *OBS: The program runs 60 times per second. Therefore, each cycle is equivalent to 1/60 seconds. // O programa é executado 60 vezes por segundo. Logo, cada ciclo equivale á 1/60 segundos.

impactTime = 0      ##//variable to calculate impact time // Variável para calcular o tempo de impacto
   ##//initial condition, 'start', 'neutral' // 'start' = condição inicial, 'neutral' = neutro
left_speed = 0      ##//motor's variables // variáveis dos motores
right_speed = 0     ##//motor's variables // variáveis dos motores

counter = 0

MAX_SPEED = 40
NORMAL_SPEED = 35

erro = 0
I = 0
D = 0


def ctrl_proportional(distance_right, distance_left):
    
    global erro, flag, tFinal, timer, tInitial, I, D
    
    erro_prev = 0 
    
    tFinal = timer
    timer += 1/60
    
    erro = (distance_left - distance_right)

    if erro == 0:
        if distance_left == 300:
            if flag == 0:
                erro = 300
            else: 
                erro = -300

                
    I = I + 0.9*erro*(tFinal - timer)  
    
    D = 0.5*(erro - erro_prev)/(tFinal - timer) 

    #Problemas: I: Cravado no rastreio ; D ou I+D: ré louca ;_;

    left_speed = MAX_SPEED* (erro/300) + (MAX_SPEED*0.8)*I + (MAX_SPEED*0.9)*D
    right_speed = MAX_SPEED* -(erro/300) + (MAX_SPEED*0.8)*I + (MAX_SPEED*0.9)*D 


    erro_prev = erro
    
    return left_speed, right_speed,erro,flag

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
    
    
    global counter, flag,erro, MAX_SPEED, NORMAL_SPEED
    
    #Time counter function, might come in handy || descontinuada  
    #if counter >= 25: 
    #    counter += 1
    
    ###Initial retreat conditions block for maneuvering### // condição inicial de retirada ("ré")
    if (counter < 25): #time-frames for reaching edge // frames-de-tempo para alcançar a borda
        right_speed = -MAX_SPEED
        left_speed = -MAX_SPEED*0.8
        counter += 1
   
    elif back_left > 0: 
            right_speed = MAX_SPEED*0.5
            left_speed = MAX_SPEED*0.8
            
    elif back_right > 0:
            left_speed = MAX_SPEED*0.5
            right_speed = MAX_SPEED*0.8
            
    elif (counter < 27): #ajustão minmax na curva
            right_speed = -MAX_SPEED*0.7
            left_speed = MAX_SPEED
            counter += 1
            
    #alternative begin strategy, discontinued
    #elif inicio == 0:
       #     right_speed = -MAX_SPEED
        #    left_speed = -MAX_SPEED
    
    ###Current maneuver: retreat and reposition###
    
    # Everything is fine, so it will search for the enemy and attack it
    
    # // Está tudo seguro, o robô procurará o inimigo e atacará
    elif (not_in_danger(front_right, front_left, distance_right, distance_left)):
        
        #left_speed, right_speed = search_engine(distance_right, distance_left)
        left_speed,right_speed,erro,flag = ctrl_proportional(distance_right, distance_left)
        
    else:
    # The robot is in danger, so it got to go back with all speed (reverse) 
    # // O robô está em perigo, então irá recuar 

        left_speed, right_speed  = -MAX_SPEED, -MAX_SPEED
        
    return {
        'leftSpeed': left_speed,
        'rightSpeed': right_speed,
        'log': [ 
        
            { 'name': 'Timer',  'value':   counter,    'min': 0, 'max': 600 },
            { 'name': 'erro',  'value':   erro,    'min': -500, 'max': 500 }
          # { 'name': 'Front Right', 'value':   front_right,   'min': 0, 'max': 1 }
          # { 'name': 'Distance Left', 'value': distance_left, 'min': 0, 'max': 300 }
        
        ]
    }

"""

def whatsTheSpeed (distance_left, distance_right):
    global sInitial, sFinal, tInitial, tFinal, speedOp, timer, impactTime
   
    if distance_left > distance_right: ##//Choose which is the shortest distance // Escolhe qual é a menor distância
        sInitial = distance_right/100 ##//Transforms measure 'cm' into 'm' (meters) // Transforma a medida 'cm' em 'm' (metros)
    else:
        sInitial = distance_left/100 ##//Transforms measure 'cm' into 'm' (meters) // Transforma a medida 'cm' em 'm' (metros)
        
    tFinal = timer ##// Changes the value of variable 'tInitial' to the current time value // Muda o valor da variável 'tInitial' para o valor de tempo atual
 
    speedOp = (sFinal - sInitial)/(tFinal - tInitial) ##// Calculating the enemy's current speed // Cálculo da velocidade atual do inimigo
    
    impactTime = tFinal - tInitial
    
    ##// Updates the variables 'tInitial', 'sFinal' and 'timer' for the next calculation // Atualiza as variáveis 'tInitial', 'sFinal' e 'timer' para o próximo cálculo
    tInitial = tFinal
    sFinal = sInitial
    timer += 1/60 ##// Increment of 1/60 seconds to keep the variable in the 'seconds' unit // Incremento de 1/60 segundos para manter a variável na unidade dos 'segundos'
    
    return impactTime, speedOp


def enemyPosition(distance_left, distance_right):
    global flag, error
    
    error = distance_left - distance_right
    
    if error > 0:
        flag = 2  ##//enemy to the right // inimigo á direita
    elif error < 0:
        flag = 0  ##//enemy to the left // inimigo á esquerda
    elif flag == 2 and distance_left > 250:
            error = 300
    elif flag == 0 and distance_left > 250:
            error = -300
    else:
        flag = 1  ##//enemy in the center or lost enemy // inimigo no centro ou perdido
        error = 0
        
    return flag, error


def search_engine(distance_right, distance_left):

   
    #Function below: Will search for the opponent rotating, 
    #and after finding it, the robot will go straight 
    #função de procura rodando no próprio eixo, ataca a frente se há detecção
         
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
    """