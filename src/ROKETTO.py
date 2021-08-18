####    ###   #   #  #####  #####  #####   ###            ▄    ▄▄▄▄▄▄▄    ▄
#   #  #   #  #  #   #        #      #    #   #          ▀▀▄ ▄█████████▄ ▄▀▀
####   #   #  ###    ####     #      #    #   #              ██ ▀███▀ ██
#  #   #   #  #  #   #        #      #    #   #            ▄ ▀████▀████▀ ▄
#   #   ###   #   #  #####    #      #     ###           ▀█    ██▀█▀██    █▀
import random

strategy = random.randint(1,3)       ##//selected strategy // estratégia selecionada

sInitial = 0        ##//initial distance // distância inicial 
sFinal = 0          ##//final distance // distância final  
tInitial = 0        ##//initial time // tempo inicial
tFinal = 0          ##//final time // tempo final
speedOp = 0         ##//opponent's speed in 'm/s' (meters per second) // velocidade do oponente em 'm/s' (metros por segundo)
timer = 1/60        ##//time in seconds -> (1/60)* // tempo em segundos -> (1/60)*
##// *OBS: The program runs 60 times per second. Therefore, each cycle is equivalent to 1/60 seconds. // O programa é executado 60 vezes por segundo. Logo, cada ciclo equivale á 1/60 segundos.

impactTime = 0      ##//variable to calculate impact time // Variável para calcular o tempo de impacto

inicio = 'start'    ##//initial condition, 'start', 'neutral' // 'start' = condição inicial, 'neutral' = neutro
left_speed = 0      ##//motor's variables // variáveis dos motores
right_speed = 0     ##//motor's variables // variáveis dos motores
speed = 40          ##//speed MAX set point // valor máximo da velocidade
flag = 1            ##//last enemy's position // última posição do inimigo
count = 0           ##//counter // contador 
error = 0           ##//error for strategy #2 // variável de 'erro' utilizada na estratégia #2
action = 0          ##//action to complement strategy #2 // variável de 'ação' utilizada na estratégia  #2

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
    
    return impactTime

def start(varX):   
    global left_speed, right_speed, flag
    
    left_speed = (-2) * speed * varX + speed
    right_speed = (-1) * speed * varX
    flag = 2 - varX
    
    return left_speed, right_speed, flag

def sensors(front_left, front_right, back_left, back_right):
    global left_speed, right_speed, flag
   
    ##//if the back_sensor > 0.5, go to the foward // se o sensor traseiro da esquerda for > 0.5 vai pra frente
    if back_left > 0.5:
        left_speed = speed * 1.0
        right_speed = speed * 0.4
    ##//if the front_sensor > 0, rotate the robot // se o algum sensor dianteiro for > 0, então rotaciona o robô
    elif front_right > 0:
        ##//turn to the left // gira para a esquerda
        left_speed = speed * -0.984
        right_speed = speed * 0.984
        flag = 0
    elif front_left > 0:
        ##//turn to the right // gira para a direita
        left_speed = speed * 0.984
        right_speed = speed * -0.984
        flag = 2
 
    return left_speed, right_speed     
       
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

def moviment(distance_left, distance_right, value1):
    global left_speed, right_speed, flag, error
    
    flag, error = enemyPosition(distance_left, distance_right)
    
    if value1 == 1:
        ##//if the enemy's position is '2', then the last position is 'right' // se o inimigo estiver á direita, vai para a direita levemente
        if flag == 2:
            right_speed = speed * 0.9
            left_speed = speed * 1.0
        ##//if the enemy's position is '0', then the last position is 'left' // se o inimigo estiver á esquerda, vai para a esquerda levemente
        elif flag == 0:
            left_speed = speed * 0.9
            right_speed = speed * 1.0
        ##//if the enemy is ahead, go to the foward // se o inimigo estiver á frente, vai pra frente
        elif flag == 1 and distance_left < 300:
            left_speed = speed * 1.0
            right_speed = speed * 1.0
    else:
        right_speed = (speed*0.5) * -(error/300) + (speed*0.2)
        left_speed = (speed*0.5) * (error/300) + (speed*0.2)       

    return left_speed, right_speed

def evasiveManeuver(distance_left, distance_right, value5):
    global inicio, left_speed, right_speed, action
    
    if value5 == 0:
        if distance_left <= distance_right:  ##//decide which way to dodge // decide para qual lado vai ser a manobra evasiva
            inicio = 'turnR'  ##//evasive maneuver to the right // manobra evasiva para a direita
        else:
            inicio = 'turnL'  ##//evasive maneuver to the left // manobra evasiva para a esquerda
    
    ##EVASIVE MANEUVER TO THE RIGHT // manobra evasiva para a direita
    if inicio == 'turnR':
        if value5 < 30:
            right_speed = speed * -0.4
            left_speed = speed * -1.0
        elif value5 < 70:
            right_speed = speed * 1.0
            left_speed = speed * -1.0
        else:
            action = 'attack'  
            
    ##EVASIVE MANEUVER TO THE LEFT // manobra evasiva para a esquerda
    elif inicio == 'turnL':
        if value5 < 35:
            right_speed = speed * -1.0
            left_speed = speed * -0.3
        elif value5 < 60:
            right_speed = speed * -1.0
            left_speed = speed * 1.0
        else:
            action = 'attack'
    
    value5 += 1
    
    return left_speed, right_speed, action, value5

def control(front_right, front_left, back_right, back_left, distance_right, distance_left):

    global strategy, impactTime, inicio, left_speed, right_speed, speed, flag, count, error, action

    if strategy == 1:
        if inicio == 'start':
            left_speed, right_speed, flag = start(1)
            inicio = 'neutral'
            return {'leftSpeed': left_speed, 'rightSpeed': right_speed}
        if count > 7:
            if back_left > 0 or front_left > 0 or front_right > 0:
                left_speed, right_speed = sensors(front_left, front_right, back_left, back_right)
                inicio = 'neutral'
                flag = 1 
            else:
                left_speed, right_speed = moviment(distance_left, distance_right,1)
        count += 1

    elif strategy == 2: 
        
        flag, error = enemyPosition (distance_left, distance_right)
        
        if inicio == 'start' :
            left_speed, right_speed, flag = start(0)
            inicio = 'neutral'
        elif (back_right > 0.9 or back_left > 0.9 or front_left > 0.9 or front_right > 0.9) and action != 'ok': ##//check the sensors // verifica os sensores
            left_speed, right_speed = sensors(front_left, front_right, back_left, back_right)
            action = 'ok'
        elif action == 'ok':
            left_speed, right_speed, action, count = evasiveManeuver(distance_left, distance_right, count)

            ##//function to perform evasive maneuver based on enemy speed // função para executar a manobra evasiva com base na velocidade do inimigo 
        elif distance_left < 50: ##// minimum distance to start checking // distância mínima para o início da verificação
            impactTime = whatsTheSpeed(distance_left, distance_right)
            if impactTime < 0.1 and action == 0: ##// Performs evasive maneuver if impact time is less than 0.2 seconds // Executa a manobra evasiva se o tempo de impacto for menor do que 0,2 segundos
                    action = 'ok'
        
        elif action == 'attack': ##//counterattack // contra-ataque após a manobra
            right_speed = speed*0.4 * -(error/300) + (speed * 0.5)
            left_speed = speed*0.4 * (error/300) + (speed * 0.5)
            if error > -10 and error < 10:
                right_speed = speed
                left_speed = speed 
        else:
            left_speed, right_speed = moviment(distance_left, distance_right, 2)

    elif strategy == 3 :
        right_speed = speed * 0.5
        left_speed = speed * 0.9
        count = count + 1
        if count >= 70: ##//change strategy after '1,1667' seconds (count/60) // muda de estratégia após 1,1667 segundos. 
            strategy = random.randint(1,2)
            if strategy == 1:
                inicio = 'neutral'
                count = 10
            else :
                action = 'attack'
##//OUTPUTS
    return {'leftSpeed': left_speed, 'rightSpeed': right_speed}
