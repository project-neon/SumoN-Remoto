####    ###   #   #  #####  #####  #####   ###
#   #  #   #  #  #   #        #      #    #   #
####   #   #  ###    ####     #      #    #   #
#  #   #   #  #  #   #        #      #    #   #
#   #   ###   #   #  #####    #      #     ###
import random

sInitial = 0        ##//initial distance // distância inicial 
sFinal = 0          ##//final distance // distância final  
tInitial = 0        ##//initial time // tempo inicial
tFinal = 0          ##//final time // tempo final
speedOp = 0         ##//opponent's speed in 'm/s' (meters per second) // velocidade do oponente em 'm/s' (metros por segundo)
timer = 0.0166667   ##//time in seconds -> (1/60=0,01667)* // tempo em segundos -> (1/60=0,01667)*
##// *OBS: The program runs 60 times per second. Therefore, each cycle is equivalent to 1/60 seconds. // O programa é executado 60 vezes por segundo. Logo, cada ciclo equivale á 1/60 segundos.

value = 0           ##//variable to calculate impact time // Variável para calcular o tempo de impacto


inicio = 'select'   ##//initial condition, 'start', 'neutral', 'start' // 'start' = condição inicial, 'neutral' = neutro, 'select' = selecionar estratégia
left_speed = 0      ##//motor's variables // variáveis dos motores
right_speed = 0     ##//motor's variables // variáveis dos motores
speed = 40          ##//speed MAX set point // valor máximo da velocidade
enemyPos = 1        ##//memory of enemy's position, 0=left, 1=center, 2=right // memoriza a posição do inimigo, 0=esquerda, 1=centro, 2=direita
last = 1            ##//last enemy's position // última posição do inimigo
count = 0           ##//counter // contador
strategy = 0        ##//selected strategy // estratégia selecionada
error = 0           ##//error for strategy #2 // variável de 'erro' utilizada na estratégia #2
action = 0          ##//action to complement strategy #2 // variável de 'ação' utilizada na estratégia  #2

def whatsTheSpeed (distance_left, distance_right):
    global sInitial, sFinal, tInitial, tFinal, speedOp, timer
   
    if distance_left > distance_right: ##//Choose which is the shortest distance // Escolhe qual é a menor distância
        sInitial = distance_right/100 ##//Transforms measure 'cm' into 'm' (meters) // Transforma a medida 'cm' em 'm' (metros)
    else:
        sInitial = distance_left/100 ##//Transforms measure 'cm' into 'm' (meters) // Transforma a medida 'cm' em 'm' (metros)
    tFinal = timer ##// Changes the value of variable 'tFinal' to the current time value // Muda o valor da variável 'tFinal' para o valor de tempo atual
    if sFinal == 0: ##// The first time, the value of 'sFinal' and 'sInitial' must be equal // Na primeira vez, o valor de 'sFinal' e 'sInitial' devem ser iguais
        sFinal = sInitial
    speedOp = (sFinal - sInitial)/(tFinal - tInitial) ##// Calculating the enemy's current speed // Cálculo da velocidade atual do inimigo
    ##// Updates the variables 'tInitial', 'sFinal' and 'timer' for the next calculation // Atualiza as variáveis 'tInitial', 'sFinal' e 'timer' para o próximo cálculo
    tInitial = tFinal
    sFinal = sInitial
    timer += 0.0166667 ##// Increment of 0.0166667 seconds to keep the variable in the 'seconds' unit // Incremento de 0.0166667 segundos para manter a variável na unidade dos 'segundos'
    return speedOp

def start(value3):
    global left_speed, right_speed
    if value3 == 1:
        ##//go to te back // vai para trás
        left_speed = speed * -1
        right_speed = speed * -1
    else:
        left_speed = speed * 1
        right_speed = speed * 0
    return left_speed, right_speed


def sensors(front_left, front_right, back_left, back_right, value4):
    global left_speed, right_speed
    if value4 == 1 :
        ##//if the back_sensor > 0.5, go to the foward // se o sensor traseiro da esquerda for > 0.5 vai pra frente
        if back_left > 0.5:
            left_speed = speed * 1.0
            right_speed = speed * 0.4
        ##//if the front_sensor > 0, rotate the robot // se o algum sensor dianteiro for > 0, então rotaciona o robô
        elif front_right > 0:
            ##//turn to the left // gira para a esquerda
            left_speed = speed * -0.984
            right_speed = speed * 0.984
        elif front_left > 0:
            ##//turn to the right // gira para a direita
            left_speed = speed * 0.984
            right_speed = speed * -0.984
    else:
        ##//check the back's sensors // verifica os sensores traseiros
        if back_left > 0.9 or back_right > 0.9:
            right_speed = speed * 1.0
            left_speed = speed * 1.0   
        ##//check the front_left sensor // verifica o sensor dianteiro da esquerda
        if front_left > 0.9 or front_right > 0.9 :
            right_speed = speed * -1.0
            left_speed = speed * -1.0 
    return left_speed, right_speed     
       

def enemyPosition(distance_left, distance_right, value2):
    global enemyPos, last, error
    enemyPos = distance_left - distance_right
    error = enemyPos
    if value2 == 1:
        if enemyPos >= 10:
            enemyPos = 2  ##//enemy to the right // inimigo á direita
        elif enemyPos <= -10:
            enemyPos = 0  ##//enemy to the left // inimigo á esquerda
        else:
            if last == 2:
                enemyPos = 2  ##//last enemy's position to the right // última posição do inimigo á direita
            elif last == 0:
                enemyPos = 0  ##//last enemy's position to the left // última posição do inimigo á esquerda
            else:
                enemyPos = 1  ##//enemy in the center or lost enemy // inimigo no centro ou perdido
        last = enemyPos  ##//capture the last enemy's position // memoriza a última posição do inimigo
        return enemyPos,0
    else:
        if error > 0:
            enemyPos = 2  ##//enemy to the right // inimigo á direita
        elif error < 0:
            enemyPos = 0  ##//enemy to the left // inimigo á esquerda
        else:
            enemyPos = 1  ##//enemy in the center or lost enemy // inimigo no centro ou perdido

        if enemyPos == 1 and distance_left == 300:
            if last == 2 :
                enemyPos = 2 ##//last enemy's position to the right // última posição do inimigo á direita
                error = 300 
            elif last == 0:
                enemyPos = 0 ##//last enemy's position to the left // última posição do inimigo á esquerda
                error = -300 
        last = enemyPos  ##//capture the last enemy's position // memoriza a última posição do inimigo
        return enemyPos, error


def moviment(distance_left, distance_right, value1):
    global enemyPos, left_speed, right_speed, error
    enemyPos, error = enemyPosition(distance_left, distance_right, value1)
    if value1 == 1:
        ##//if the enemy's position is '2', then the last position is 'right' // se o inimigo estiver á direita, vai para a direita levemente
        if enemyPos == 2:
            right_speed = speed * 0.9
            left_speed = speed * 1.0
        ##//if the enemy's position is '0', then the last position is 'left' // se o inimigo estiver á esquerda, vai para a esquerda levemente
        elif enemyPos == 0:
            left_speed = speed * 0.9
            right_speed = speed * 1.0
        ##//if the enemy is ahead, go to the foward // se o inimigo estiver á frente, vai pra frente
        elif enemyPos == 1 and distance_left < 300:
            left_speed = speed * 1.0
            right_speed = speed * 1.0
    else:
        ##//if the enemy's position is '2', then the last position is 'right' // se o inimigo estiver á direita, gira para a direita proporcionalmente ao 'erro' calculado  
        if enemyPos == 2 :
            right_speed = speed * -(error/300)
            left_speed = speed * (error/300)       
        ##//if the enemy's position is '0', then the last position is 'left' // se o inimigo estiver á esquerda, gira para a esquerda proporcionalmente ao 'erro' calculado  
        elif enemyPos == 0 :
            left_speed = speed*(error/300)
            right_speed = speed*-(error/300)      
    return left_speed, right_speed


def evasiveManeuver(distance_left, distance_right, value5):
    global inicio, error, left_speed, right_speed, action, enemyPos
    enemyPos, error = enemyPosition(distance_left,distance_right, 2)
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
        elif value5 < 65:
            right_speed = speed * 1.0
            left_speed = speed * -1.0
        else:
            inicio = 'keepTurn'  ##//search the enemy after the maneuver // Procura pelo inimio após a manobra
    ##EVASIVE MANEUVER TO THE LEFT // manobra evasiva para a esquerda
    elif inicio == 'turnL':
        if value5 < 35:
            right_speed = speed * -1.0
            left_speed = speed * -0.3
        elif value5 < 60:
            right_speed = speed * -1.0
            left_speed = speed * 1.0
        else:
            inicio = 'keepTurn'  ##//search the enemy after the maneuver // Procura pelo inimio após a manobra
    elif inicio == 'keepTurn':
        if error < 10 and error > -10:
            action = 'attack'  ##//attack if the enemy is in front // ataca se o inimigo estiver na frente
        else:
            ##//search the enemy // Procura o inimigo
            left_speed = speed * (error / 300)
            right_speed = speed * -(error / 300)
    value5 += 1
    return left_speed, right_speed, action, value5


def control(front_right, front_left, back_right, back_left, distance_right, distance_left):

    global inicio, left_speed, right_speed, speed, enemyPos, last, count, strategy, error, action
    global speedOp, value
    
    if inicio == 'select':  ##//randomly select strategy // escole a estratégia aleatoriamente
        strategy = random.randint(1, 3)
        inicio = 'start'

    if strategy == 1:
        if inicio == 'start':
            left_speed, right_speed = start(1)
            inicio = 'neutral'
            return {'leftSpeed': left_speed, 'rightSpeed': right_speed}
        if count > 7:
            if back_left > 0 or front_left > 0 or front_right > 0:
                left_speed, right_speed = sensors(front_left, front_right, back_left, back_right, 1)
                inicio = 'neutral'
                last = 1
            else:
                left_speed, right_speed = moviment(distance_left, distance_right,1)
        count += 1

    elif strategy == 2:
        
     
        
        enemyPos, error = enemyPosition (distance_left, distance_right, 2)
        if inicio == 'start' :
            left_speed, right_speed = start(2)
            inicio = 'neutral'
        elif (back_right > 0.9 or back_left > 0.9 or front_left > 0.9 or front_right > 0.9) and action != 'ok': ##//check the sensors // verifica os sensores
            left_speed, right_speed = sensors(front_left, front_right, back_left, back_right, 2)
            action = 'ok'
        elif action == 'ok':
            left_speed, right_speed, action, count = evasiveManeuver(distance_left, distance_right, count)

        
        ##//function to perform evasive maneuver based on enemy speed // função para executar a manobra evasiva com base na velocidade do inimigo 
        elif distance_left < 60: ##// minimum distance to start checking // distância mínima para o início da verificação
            speedOp = whatsTheSpeed(distance_left, distance_right) ##// calculating the enemy's current speed // calcula a velocidade atual do inimigo
            if speedOp > 0: 
                ##//calculates the impact time // calcula o tempo para o impacto
                if distance_left < distance_right: ##//selects the side with the shortest distance // seleciona o lado com a menor distância
                    value = (distance_left/100) / speedOp 
                else:
                    value = (distance_right/100) / speedOp
                if value <= 0.2 and action == 0: ##// Performs evasive maneuver if impact time is less than 0.2 seconds // Executa a manobra evasiva se o tempo de impacto for menor do que 0,2 segundos
                    action = 'ok'
                    count = 0
            



        elif action == 'attack': ##//counterattack // contra-ataque após a manobra
            if enemyPos == 2:  ##//enemy on the right // inimigo à direita
                right_speed = speed * 0.8
                left_speed = speed * 1.0
            elif enemyPos == 0:  ##//enemy on the left // inimigo à esquerda
                right_speed = speed * 1.0
                left_speed = speed * 0.8
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
                count = 0
##//OUTPUTS
    return {'leftSpeed': left_speed, 'rightSpeed': right_speed}
