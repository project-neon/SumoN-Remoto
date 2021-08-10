####### #   #    ##    ###
   #    #  # #  #  ## #   #
   #    # #   #  ###   ###
                    """"+tweaks by matz <3"""

etapa = 0
motor_dir = 0
motor_esq = 0

MAX_SPEED = 40

def control(front_right, front_left, back_right, back_left, distance_right, distance_left):
    global motor_dir
    global motor_esq
    global etapa


    if(front_right < 0.8 and front_left < 0.8): #check if it's safe // checar se está seguro

        if front_right < 0.25 or front_left < 0.25:
            if etapa == 0:
                if distance_right == 300: ## dá ré e procura oponente
                    motor_dir = -MAX_SPEED
                    motor_esq = MAX_SPEED
                    etapa = 1

            elif distance_right < 300 and distance_left == 300: ## alinha acelerando esquerdo
                motor_dir = -5
                motor_esq = MAX_SPEED
            elif distance_right == 300 and distance_left < 300: ## alinha acelerando direita
                motor_dir = MAX_SPEED
                motor_esq = -5
            elif distance_right < 300 and distance_left < 300: #acelera os dois lados

                if distance_left < 10:
                    motor_dir = MAX_SPEED
                    motor_esq = -MAX_SPEED
                else:
                    motor_dir = MAX_SPEED
                    motor_esq = MAX_SPEED


        elif back_right == 0.25 or back_left == 0.25: ## foge na borda se oponente empurra
            motor_dir = 35
            motor_esq = 40

        else:
            motor_dir = 0
            motor_esq = 40
    
    else:
        left_speed, right_speed  = -MAX_SPEED, -MAX_SPEED

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