####    ###   #   #  #####  #####  #####   ###
#   #  #   #  #  #   #        #      #    #   #
####   #   #  ###    ####     #      #    #   #
#  #   #   #  #  #   #        #      #    #   #
#   #   ###   #   #  #####    #      #     ###
import random

inicio = 's'              ##//initial condition, 'r'=rear, 'f'=foward, 'e'= neutral, 's'=select strategy  // condição inicial, 'r'=trás, 'f'=frente, 'e'=neutro, 's'=selecionar estratégia
left_speed = 0            ##//motor's variables // variáveis dos motores
right_speed = 0           ##//motor's variables // variáveis dos motores
speed = 40                ##//speed MAX set point // valor máximo da velocidade
enemyPos = 1              ##//memory of enemy's position, 0=left, 1=center, 2=right  // memoriza a posição do inimigo, 0=esquerda, 1=centro, 2=direita
last = 1                  ##//last enemy's position // última posição do inimigo
count = 1                 ##//counter  // contador
strategy = 0              ##//selected strategy // estratégia selecionada
error = 0                 ##//error for strategy #2  // variável de 'erro' utilizada na estratégia #2
action = 0                ##//action to complement strategy #2  // variável de 'ação' utilizada na estratégia  #2

def control(front_right, front_left, back_right, back_left, distance_right, distance_left):

    global inicio, left_speed, right_speed, speed, enemyPos, last, count, strategy, error, action
    
    ##//randomly select strategy  // escole a estratégia aleatoriamente
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
        
        ##//initial condition  // condição inicial
        if inicio == 'r' :
            ##//go to te back  // vai para trás
            left_speed = speed * -1
            right_speed = speed * -1
            inicio = 'e'
            return { 
                'leftSpeed': left_speed,
                'rightSpeed': right_speed
            }    
         
            
##//--------- CALCULATE ENEMY'S POSITION -------------
        if count > 8 :
        
        
            enemyPos = distance_left - distance_right
    
   
            if enemyPos >= 10 :
                enemyPos = 2 ##//enemy to the right // inimigo á direita
            elif enemyPos <= -10 :
                enemyPos = 0 ##//enemy to the left // inimigo á esquerda
            else :
                if last == 2 :
                    enemyPos = 2 ##// last enemy's position to the right  // última posição do inimigo á direita
                elif last == 0 :
                    enemyPos = 0 ##// last enemy's position to the left  // última posição do inimigo á esquerda
                else :
                    enemyPos = 1 ##//enemy in the center or lost enemy  // inimigo no centro ou perdido
    
            last = enemyPos    ##//capture the last enemy's position // memoriza a última posição do inimigo
        
        
        
##//---------------- VERIFICATIONS #1 ----------------  
    
            ##//if the back_sensor > 0.5, go to the 'foward'  // se o sensor traseiro da esquerda for > 0.5, então muda 'inicio' para 'f', vai pra frente
            if back_left > 0.5 :
                left_speed = speed*1.0
                right_speed = speed*0.4
                inicio = 'f'
        
            ##// if the front_sensor > 0.0, go to 'neutral'  // se o algum sensor dianteiro for > 0, então rotaciona o robô. Muda 'inicio' para 'e', neutro    
            elif front_right > 0 :
                ##//turn to the left  // gira para a esquerda
                left_speed = speed*-0.984
                right_speed = speed*0.984
                inicio = 'e'
                last = 1 ##//'last' changed  // valor de 'last' alterado
            elif front_left > 0 :
                ##//turn to the right // gira para a direita
                right_speed = speed*-0.984
                left_speed = speed*0.984
                inicio = 'e'
                last = 1 ##//'last' changed // valor de 'last' alterado

##//--------- MAKE DECISIONS #1 ------------------        
    
            ##//if the enemy's position is '2', then the last position is 'right'   // se o inimigo estiver á direita, vai para a direita levemente  
            elif enemyPos == 2 :
                right_speed = speed*0.9
                left_speed = speed*1.0
        
            ##//if the enemy's position is '0', then the last position is 'left'   // se o inimigo estiver á esquerda, vai para a esquerda levemente     
            elif enemyPos == 0 :
                left_speed = speed*0.9
                right_speed = speed*1.0

##//----------- ATTACK, MAYBE #1 ----------------- 
        
            ##//if the enemy is ahead  // se o inimigo estiver á frente
            elif enemyPos == 1 and distance_left < 300 :
                ##// go! go! go! more faster!!!!!  /// avança o mais rápido que conseguir
                left_speed = speed*1.0;
                right_speed = speed*1.0;
        
            ##//if 'inicio' = 'f', go to the foward  // se 'inicio' for 'f', o robô gira no próprio eixo     
            elif inicio == 'f' :
                ##//turn looking for enemy // ira para procurar o inimigo
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
            enemyPos = 2 ##//enemy to the right // inimigo á direita
        elif error < 0 :
            enemyPos = 0 ##//enemy to the left // inimigo á esquerda
        else:
            enemyPos = 1 ##//enemy in the center or lost enemy  // inimigo no centro ou perdido
                       
##//--------- MAKE DECISIONS PART 1#2 ------------------        
 
        if enemyPos == 1 and distance_left == 300:
            if last == 2 :
                enemyPos = 2 ##// last enemy's position to the right   // última posição do inimigo á direita
                error = 300 
            elif last == 0:
                enemyPos = 0 ##// last enemy's position to the left   // última posição do inimigo á esquerda
                error = -300 
            else :
                ##//search for the enemy // gira procurando o inimigo
                right_speed = speed * 0.0
                left_speed = speed * 1.0
               
        last = enemyPos    ##//capture the last enemy's position   // memoriza a última posição do inimigo  
              
        ##//Check the back's sensors // Verifica os sensores traseiros
        if (back_right > 0.9 or back_left > 0.9) and action != 'ok':
            right_speed = speed * 1.0
            left_speed = speed * 1.0
            
        ##//Check the front_left sensor // Verifica o sensor dianteiro da esquerda
        if front_left > 0.9 and action != 'ok' :
            right_speed = speed * -1.0
            left_speed = speed * -1.0
            action = 'ok'
            
        ##//Check the front_right sensor  // Verifica o sensor dianteiro da esquerda
        elif front_right > 0.9 and action != 'ok' :
            right_speed = speed * -1.0
            left_speed = speed * -1.0
            action = 'ok'

##//--------- EVASIVE MANEUVER ------------------            
       
        ##//Evasive maneuver!!  // Manobra evasiva
        elif action == 'ok' :
            if count == 0 :
                if distance_left <= distance_right : ##//decide which way to dodge  /// decide para qual lado vai ser a manobra evasiva
                    inicio = 'turnR' ##//evasive maneuver to the right /// manobra evasiva para a direita
                else:
                    inicio = 'turnL' ##//evasive maneuver to the left /// manobra evasiva para a esquerda
                   
            ##EVASIVE MANEUVER TO THE RIGHT  // manobra evasiva para a direita
            if inicio == 'turnR' :
                if count < 27 :
                    right_speed = speed * -0.3
                    left_speed = speed * -1.0
                elif count < 65 :
                    right_speed = speed * 1.0
                    left_speed = speed * -1.0  
                else :
                    inicio = 'keepTurn'  ##//search the enemy after the maneuver // Procura pelo inimio após a manobra
            
             ##EVASIVE MANEUVER TO THE LEFT  // manobra evasiva para a esquerda
            elif inicio == 'turnL' :
                if count < 27 :
                    right_speed = speed * -1.0
                    left_speed = speed * -0.3
                elif count < 65 :
                    right_speed = speed * -1.0
                    left_speed = speed * 1.0
                else :
                    inicio = 'keepTurn'  ##//search the enemy after the maneuver // Procura pelo inimio após a manobra
                    
            elif inicio == 'keepTurn' :
                if error < 10 and error > -10 : 
                    action = 'attack' ##//attack if the enemy is in front /// ataca se o inimigo estiver na frente
                else: 
                    ##//search the enemy // Procura o inimigo
                    left_speed = speed*(error/300)
                    right_speed = speed*-(error/300)
            
            count += 1
        

##//--------- MAKE DECISIONS PART 2 #2 ------------------
        
        ##//ROKETTO!! Evasive maneuver!! ref: POKÉMON
        elif distance_left < 50 and action == 0:
            action = 'ok'
            count = 0
        
        ##//counterattack  // contra-ataque após a manobra (PODE MUDAR DE ESTRATÉGIA NO MEIO DA LUTA OU EXECUTAR UMA FUNÇÃO PRÓPRIA DA ESTRATÉGIA 2)   
        elif action == 'attack' : 
            if enemyPos == 2: ##enemy on the right // inimigo à direita
                right_speed = speed * 0.8
                left_speed = speed * 1.0
            elif enemyPos == 0: ##enemy on the left // inimigo à esquerda
                right_speed = speed * 1.0
                left_speed = speed * 0.8
                            
        ##//if the enemy's position is '2', then the last position is 'right'  // se o inimigo estiver á direita, gira para a direita proporcionalmente ao 'erro' calculado  
        elif enemyPos == 2 :
            right_speed = speed * -(error/300)
            left_speed = speed * (error/300)
        
        ##//if the enemy's position is '0', then the last position is 'left'  // se o inimigo estiver á esquerda, gira para a esquerda proporcionalmente ao 'erro' calculado  
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
        if count >= 80: ##// change strategy after '1,333' seconds (count/60) /// muda de estratégia após 1,333 segundos. 
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
