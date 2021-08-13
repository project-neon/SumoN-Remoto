left_speed = 0      # velocidade da roda esquerda
right_speed = 0     # velocidade da roda direita
speed = 40          # velocidade máxima

erro = 0            # variável de erro para utilizar no ajuste e correção da velocidade nas rodas
flag = 0            # variável para memorizar a última posição do inimigo ---> 0:direita   1:esquerda
margem = 50         # margem de segurança para poder atacar

count = 1           # contador
var = 1             # variável de controle

def ctrl(distance_right, distance_left): # função para posicionar o robô na direção do inimigo
    global erro, flag, left_speed, right_speed, speed,margem
    
    erro = (distance_left - distance_right) #erro positivo: inimigo á direita    erro negativo: inimigo á esquerda
    
    if erro == 0: #isso ocorre quando perdemo o inimigo de vista
        if distance_left >= 300:
            if flag == 0:   #procura pela direita
                left_speed = speed
                right_speed = -speed
            else:           #procura pela esquerda
                left_speed = -speed
                right_speed = speed
    else:
        if erro > 0 : #muda o valor da flag de acordo com o valor do erro
            flag = 0
        if erro < 0 : 
            flag = 1
        #movimenta o robô proporcionalmente ao valor de erro calculado
        left_speed = (speed*0.5) * (erro)/300 + (speed*0.4) 
        right_speed = (speed*0.5) * -(erro)/300 + (speed*0.4)
    
    return left_speed, right_speed,erro,flag

def manobra(var): #função para acelerar aos poucos, para diminuir a chance de ser "rampado"
    global left_speed, right_speed, count
    
    if var == 2: #primeiro estágio da aceleração
        left_speed = speed*0.9
        right_speed = speed*0.9
        count = count+1
        
    if count >40: #segundo estágio da aceleração
        left_speed = speed
        right_speed = speed
        count = count+1
     
    if count > 60: #reset da função
        var = 'atk'
        count = 1
        
    return left_speed, right_speed,var,count

def control(front_right, front_left, back_right, back_left, distance_right, distance_left): # função principal
    global left_speed, right_speed,erro, margem, var,count
    
    left_speed,right_speed,erro,flag = ctrl(distance_right, distance_left) #chamada da função "ctrl"
    
    if (distance_right < 40 or distance_left < 40) and var ==1: #quando o inimigo estiver perto, mudamos a o valor de "var" para poder chamar a função "manobra"
        var = 2
    
    if var == 2:
        left_speed, right_speed,var,count = manobra(var) # chamada da função "manobra"
        
    
    if erro > -margem and erro < margem and distance_left < 300 and var == 'atk': # ataca quando já foi executado a "manobra"
        left_speed = speed
        right_speed = speed
    
    if front_left > 0.8 or front_right > 0.8: # uso dos sensores para evitar a queda da arena
        left_speed = -speed
        right_speed = -speed
   
        
##//OUTPUTS
    return {'leftSpeed': left_speed, 'rightSpeed': right_speed
           #'log': [ 
        
          # { 'name': 'count',  'value':   count,    'min': 0, 'max': 120 },
          # { 'name': 'meio', 'value':   0,   'min': -300, 'max': 300 }
          # { 'name': 'flag', 'value':   flag,   'min': -1, 'max': 2 },
          # { 'name': 'speed', 'value':   left_speed,   'min': -40, 'max': 40 }
          # { 'name': 'Distance Left', 'value': distance_left, 'min': 0, 'max': 300 }
        
        #]
           }