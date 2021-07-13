flag = 1 # 0 esquerda | 1 direita
         #Nos fala para onde o inimigo foi (Da última vez que o inimigo foi avistado, foi por qual olho?)
search_state = True # A variável ficará como True enquanto o inimigo estiver distante, permitindo o robô se manter no Mode Busca
counter = 80 # É o tempo que o robô ficara no Modo Olé se desviando do inimigo
ole = True # A variável ficará como True enquanto o counter não zerar. Quando for False, o robô saírada do Modo Olé
refresh = True # Serve para a primeira vez que o Modo Olé começa. Ele vai ajudar a saber, no começo do Modo Olé, o inimigo
                #estava mais para a 

##########################################
#    Modo Busca - Não perder de vista    #
########################################## 

def search_mode(distance_right, distance_left):
    global flag
    
    if distance_right < 300 and distance_left == 300:
        # O oponente está para a direita => Gira para a direita
        leftSpeed  =  40
        rightSpeed =  5
        flag = 1
    elif distance_right == 300 and distance_left < 300:
        # O oponente está para a esquerda => Gira para a esquerda
        leftSpeed  =  5
        rightSpeed =  40
        flag = 0
    elif distance_right < 300 and distance_left < 300:
        # O oponente está para frente, entã irá andar lentamente para 
        # frente durante o search_mode para tentar ganhar terreno
        leftSpeed  = 10
        rightSpeed = 10
    else:# O oponente foi perdido e vista
        if flag == 0: # A última vez que foi visto estava para a esquerda => Gira para a esquerda
            leftSpeed  = -10
            rightSpeed = 40
        else: # A última vez que foi visto estava para a direita => Gira para a direita
            leftSpeed  = 40
            rightSpeed = -10
    return leftSpeed, rightSpeed

##########################################
#     Modo Olé - Desviar do inimigo      #
##########################################

def ole_mode(distance_right, distance_left):
    global ole, counter, refresh, flag
    
    # Se o inimigo estiver mais próximo do "olho" da esquerda, então a flag indicará que 
    # devemos nos desviar pelo sentido anti-horário (olhando por cima). Caso contrário
    # devemos nos desviar pelo sentido horário. Como precisamos dessa informação apenas
    # quando a função é chamada pela primeira vez, o refresh nos permite não atualizarmos
    # a variável flag novamente a cada iteração.
    if (distance_left < distance_right) and refresh == True:
        flag = 0
        refresh = False
    elif refresh == True:
        flag = 1
        refresh = False
    
    # Sentido anti-horário
    if flag == 0 and counter > 0:
        leftSpeed = -40
        rightSpeed = -5
        counter -= 1
    # Sentido horário
    elif counter > 0:
        leftSpeed = -5
        rightSpeed = -40
        counter -= 1
    
    # Enquanto Olé for True, essa função vai ficar se repetindo. Então assim que o 
    # Contador zerar (counter), queremos que o robô saia do Modo Olé e vá para o Modo Ataque
    if counter == 0:
        ole = False

    return leftSpeed, rightSpeed


##########################################
#    Modo Ataque - Hora de ir com tudo!  #
########################################## 

def attack_mode(front_right, front_left, distance_right, distance_left,back_left):
    global flag
    # Se a borda branca for identificada pelos sensores da frente, o robô vai pra trás
    if front_left > 0.8 or front_right > 0.8:
        leftSpeed  = -40
        rightSpeed = -40
    # Caso a borda seja identificada pelo sensor esquerdo traseiro, o robô vai para a direita
    elif back_left > 0.25:
        leftSpeed = 30
        rightSpeed =-30
    # Percebe o oponente na direita, faz com ele gire totalmente para a direita  
    elif distance_right < 300 and distance_left == 300:
        leftSpeed  =  35
        rightSpeed =  0
    # Percebe o oponente na esquerda, faz com ele gire totalmente para a esquerda
    elif distance_right == 300 and distance_left < 300:
        leftSpeed  = 0
        rightSpeed = 35
    # Caso os sensores vejam o oponente na sua frente, vai com tudo!
    elif distance_right < 300 and distance_left < 300:
        leftSpeed  = 40
        rightSpeed = 40

    # Modo auxiliar semelhante ao modo BUSCA - OPONENTE PERDIDO
    # A Flag será usada para saber qual foi o lado em que o oponente foi visto pela última vez
    # Caso o oponente não seja detectado pelo robô, ele irá:
    else:
        if flag == 0: # Caso a FLAG decectar a ultima localização na esquerda, o robô vira pra esquerda
            leftSpeed  = -10
            rightSpeed = 35
        else: #Caso contrário (FLAG IMPLICITA), o robô vira para a direita
            leftSpeed  = 35
            rightSpeed = -10
            
    return leftSpeed, rightSpeed

#####################################################
#    Função de Controle - Manter tudo nos eixos!    #
#####################################################

def control(front_right, front_left, back_right, back_left, distance_right, distance_left):
    global search_state, flag, ole
    
    if distance_left < 25 and distance_right < 25: # Torna a variável falsa, ou seja, diz que o inimigo está perto
        search_state = False
    
    if search_state == True: # A variável é verdadeira. O MODO BUSCA é chamado e entra em vigor
        leftSpeed, rightSpeed = search_mode(distance_right, distance_left)
    elif ole == True: # A variavel é verdadeira. O MODO OLE é chamado. Desviar é o foco!
        leftSpeed, rightSpeed = ole_mode(distance_right, distance_left)
    else: # Caso o MODO OLE for falso (implicito), o robô entra no MODO ATAQUE
        leftSpeed, rightSpeed = attack_mode(front_right, front_left, distance_right, distance_left,back_left)     
        
    return {
        'leftSpeed':  leftSpeed,
        'rightSpeed': rightSpeed,
        'log': [
            { 'name': 'Distance Right', 'value': distance_right, 'min': 0, 'max': 300 },
            { 'name': 'Distance Left', 'value': distance_left, 'min': 0, 'max': 300 }
        ]
    }