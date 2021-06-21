flag = 1 # 0 left | 1 right, Nos diz para onde o inimigo foi
best_eye = 1
turn_side = 1
search_state = True
ole = True
refresh = True
counter = 90
delta = 0


def search_mode(distance_right, distance_left):
    global flag
    
    if distance_right < 300 and distance_left == 300:
        # Opponent to the right => Turn right
        leftSpeed  =  40
        rightSpeed =  5
        flag = 1
    elif distance_right == 300 and distance_left < 300:
        # Opponent to the left => Turn left
        leftSpeed  =  5
        rightSpeed =  40
        flag = 0
    elif distance_right < 300 and distance_left < 300:
        # Opponent in front
        leftSpeed  = 5
        rightSpeed = 5
    else:# Lost the opponent
        if flag == 0: #Last time seen was to the left
            leftSpeed  = -10
            rightSpeed = 40
        else: #Last time seen was to the right
            leftSpeed  = 40
            rightSpeed = -10
    return leftSpeed, rightSpeed

def ole_mode(distance_right, distance_left):
    global ole, counter, refresh, turn_side, flag
    
    if (distance_left < 300) and refresh == True:
        turn_side = 0
        flag = 0
        refresh = False
    elif refresh == True:
        turn_side = 1
        flag = 1
        refresh = False
        
    if turn_side == 0 and counter > 0:
        if counter > 70:
            leftSpeed = -40
            rightSpeed = -5
        else:
            leftSpeed = -40
            rightSpeed = 40
        counter -= 1
    elif counter > 0:
        if counter > 70:
            leftSpeed = -5
            rightSpeed = -40
        else:
            leftSpeed = 40
            rightSpeed = -40
        counter -= 1
    
    if counter == 0:
        ole = False

    return leftSpeed, rightSpeed

def attack_mode(front_right, front_left, distance_right, distance_left,back_left):
    global flag
    # Se identificar a borda branca => Recua
    if front_left > 0.8 or front_right > 0.8:
        leftSpeed  = -40
        rightSpeed = -40
    
    elif back_left > 0.25:
        leftSpeed = 30
        rightSpeed =-30
    # Oponente na direita => Vira pra direita    
    elif distance_right < 300 and distance_left == 300:
        leftSpeed  =  35
        rightSpeed =  0
    # Oponente na esquerda => Vira esquerda
    elif distance_right == 300 and distance_left < 300:
        leftSpeed  = 0
        rightSpeed = 35
    # Oponente na frente => Ataque    
    elif distance_right < 300 and distance_left < 300:
        leftSpeed  = 40
        rightSpeed = 40
    # Oponente perdido => Procurar o oponente
    else:# Perdeu o oponente
        if flag == 0: # Visto pela última vez à esquerda
            leftSpeed  = -10
            rightSpeed = 35
        else: #Visto pela última vez à direita
            leftSpeed  = 35
            rightSpeed = -10
            
    return leftSpeed, rightSpeed


def control(front_right, front_left, back_right, back_left, distance_right, distance_left):
    global search_state, flag, delta, ole
    
    if distance_left < 20 and distance_right < 20:
        search_state = False
    
    if search_state == True:
        leftSpeed, rightSpeed = search_mode(distance_right, distance_left)
    elif ole == True:
        leftSpeed, rightSpeed = ole_mode(distance_right, distance_left)
    else: 
        leftSpeed, rightSpeed = attack_mode(front_right, front_left, distance_right, distance_left,back_left)     
        
    return {
        'leftSpeed':  leftSpeed,
        'rightSpeed': rightSpeed,
        'log': [
            { 'name': 'Distance Right', 'value': distance_right, 'min': 0, 'max': 300 },
            { 'name': 'Distance Left', 'value': distance_left, 'min': 0, 'max': 300 }
        ]
    }