search = False # Define se está no modo procura/ Setssearch mode 
flag = 1 # 0 esquerda | 1 direita / 0 left | 1 right
inicio = True # Faz com que a função STARTOU seja sempre a primeira a ser utilizada / makes the STARTOU function always the first one to be used
leftSpeed = 0
rightSpeed = 0
tatakae = False # Define o modo de ataque / Sets Attack Mode

##########################################
#       Modo Inicial / Initial Mode      #
########################################## 

def startou (distance_right, distance_left, back_left, back_right):
    global inicio, search, leftSpeed, rightSpeed
    
    leftSpeed = -30 # Vai para trás até encontrar a borda do dohyo / go backward until detecting the white border of the dohyo
    rightSpeed = -30
    if back_left > 0 or back_right > 0: # Após detectar a borda branca, vai para a direita / After detecting the white border, go to the right
        leftSpeed = 50
        rightSpeed = 0
        inicio = False # Seta a variavel falso, para sair da função / Set the variable to false to exit the function
        
    return leftSpeed, rightSpeed
           

##########################################
#      Modo de Procura / Search Mode     #
########################################## 
            
def search_mode(distance_right, distance_left):
    global flag, leftSpeed, rightSpeed, tatakae
    
    if distance_right < 300 and distance_left == 300: 
        #O oponente está para a direita => Gira para a direita / Opponent is to the right => Rotate to the right
        leftSpeed  =  40
        rightSpeed =  0
        flag = 1 # Memorizar ultimo lado qu3 viu o inimigo / Memorize last side that saw the enemy
    elif distance_right == 300 and distance_left < 300:
        #O oponente está para a esquerda => Gira para a esquerda / Opponent is to the left => Rotate to the left
        leftSpeed  =  0
        rightSpeed =  40
        flag = 0 # Memorizar ultimo lado qu3 viu o inimigo / Memorize last side that saw the enemy
    elif distance_right < 300 and distance_left < 300:
        # O oponente esta na frente => Anda lentamente para frente / Opponent is in front => Slowly walk forward
        leftSpeed  = 10
        rightSpeed = 10
        tatakae = True # Define como verdadeira => Chama a função de ataque / Set to true => Call attack function
    else: # Inimigo está perdido => Verifica o valor da flag / Enemy is lost => Check the flag value
        if flag == 0: # Inimigo na esquerda => Vira para a esquerda /  Opponent is to the left => Rotate to the left
            leftSpeed  = 0
            rightSpeed = 40
        else: # Inimigo está na direita => Vira para a direita / Opponent is to the right > Rotate to the right
            leftSpeed  = 40
            rightSpeed = 0
    return leftSpeed, rightSpeed

##################################
#    Modo Ataque - Attack Mode   #
################################## 

def ninja_attack (front_left, front_right, distance_right, distance_left, back_left, back_right):
    global leftSpeed, rightSpeed, tatakae

    # Sensor esquerdo identificaram a borda branca => Virar suavemente para esquerda
    # Left sensor identify white edge => Smooth left turn
    if front_left > 0.9:
        leftSpeed = -5
        rightSpeed = -20
    elif front_right > 0.9:
    # Sensor direito identificaram a borda branca => Virar suavemente para direita
    # Right sensor identify white edge => Smooth right turn
        leftSpeed = -20
        rightSpeed = -5
    elif back_left > 0:
    # Sensor traseiro esquerdo identifica a borda branca => Vira para a direita
    # Left rear sensor identifies white border => Turns to the right
        leftSpeed = 20
        rightSpeed = -5
    elif back_right > 0:
    # Sensor traseiro direito identifica a borda branca => Vira para a esquerda
    # Right rear sensor identifies white border => Turns to left
        leftSpeed = -5
        rightSpeed = 20
    elif distance_right < 300 and distance_left < 300:
    # Inimigo está na sua frente => ATAQUEEEEE!!!!!    
    # Enemy is in front of you => ATTACK!!!!!
        leftSpeed  = 40
        rightSpeed = 40
    return leftSpeed, rightSpeed

#####################################################
#       Função de Controle - Control Function      #
#####################################################

def control(front_right, front_left, back_right, back_left, distance_right, distance_left):
    global leftSpeed, rightSpeed, inicio, search, tatakae
    
    if inicio == True: # Variavel INICIO verdadeira => Começa a função STARTOU / # INICIO is True => Starts the function Startou
        leftSpeed, rightSpeed = startou(distance_right, distance_left, back_left, back_right)
    else: # Caso seja falsa => Começa o modo de procura / If INICIO is false => Search Mode
        leftSpeed, rightSpeed = search_mode(distance_right, distance_left)
    if tatakae == True: # Caso Tatakae seja verdadeira => Modo de ataque / If Tatakae is true => Attack mode
        leftSpeed, rightSpeed = ninja_attack(front_left, front_right, distance_right, distance_left, back_left, back_right)
        

        
    return {'leftSpeed': leftSpeed, 'rightSpeed': rightSpeed}