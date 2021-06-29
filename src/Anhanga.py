etapa = 0
motor_dir = 0
motor_esq = 0
count=0
rampa = True



def control(front_right, front_left, back_right, back_left, distance_right, distance_left):
    global motor_dir
    global motor_esq
    global etapa
    
    
    
    
    
    if front_right <= 0.25 or front_left <= 0.25:
        if etapa != 2:
            if distance_right == 300 and etapa == 1: ## dá ré e procura oponente
                motor_dir = -40
                motor_esq = 40
                etapa = 2
            elif front_left < 0.25 or front_right < 0.25 and etapa == 1:
                motor_dir = 40
                motor_esq = 40
            elif etapa == 0:
                etapa = 1
            
        elif distance_right < 300 and distance_left == 300: ## alinha acelerando esquerdo
            motor_dir = 39
            motor_esq = 40
        elif distance_right == 300 and distance_left < 300: ## alinha acelerando direita
            motor_dir = 40
            motor_esq = 39
       # elif distance_right < 300 and distance_left < 300: #acelera os dois lados
        #    motor_dir = 40
         #   motor_esq = 40
    
    
    
    
    
    
    #elif back_right < front_right and back_left < front_left: 
     #   motor_dir = 40
      #  motor_esq = -40    
        
         
        
    
    else:
        motor_dir = -40
        motor_esq = 40
        
    
    
    right_speed = motor_dir
    left_speed = motor_esq
    
    return {
        'leftSpeed': left_speed,
        'rightSpeed': right_speed,
        'log': [
            { 'name': 'Front Left',  'value':   front_left,    'min': 0, 'max': 1 },
            { 'name': 'Front Right', 'value':   front_right,   'min': 0, 'max': 1 },
            { 'name': 'Distance Left', 'value': distance_left, 'min': 0, 'max': 300 }
        ]
    }

