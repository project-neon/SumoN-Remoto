search = False
flag = 1
inicio = True
leftSpeed = 0
rightSpeed = 0
tatakae = False

def startou (distance_right, distance_left, back_left, back_right):
    global inicio, search, leftSpeed, rightSpeed
    
    leftSpeed = -30
    rightSpeed = -30
    if back_left > 0 or back_right > 0:
        leftSpeed = 50
        rightSpeed = 0
        inicio = False
        
    return leftSpeed, rightSpeed
           
            
def search_mode(distance_right, distance_left):
    global flag, leftSpeed, rightSpeed, tatakae
    
    if distance_right < 300 and distance_left == 300:
        leftSpeed  =  40
        rightSpeed =  0
        flag = 1
    elif distance_right == 300 and distance_left < 300:
        leftSpeed  =  0
        rightSpeed =  40
        flag = 0
    elif distance_right < 300 and distance_left < 300:
        leftSpeed  = 10
        rightSpeed = 10
        tatakae = True
    else:
        if flag == 0: 
            leftSpeed  = 0
            rightSpeed = 40
        else: 
            leftSpeed  = 40
            rightSpeed = 0
    return leftSpeed, rightSpeed

def ninja_attack (front_left, front_right, distance_right, distance_left, back_left, back_right):
    global leftSpeed, rightSpeed, takakae
    if front_left > 0 or front_right > 0:
        leftSpeed = -40
        rightSpeed = -40
    elif back_left > 0 or back_right > 0:
        leftSpeed = 20
        rightSpeed = -20
    elif distance_right < 300 and distance_left < 300:
        leftSpeed  = 40
        rightSpeed = 40
    return leftSpeed, rightSpeed

def control(front_right, front_left, back_right, back_left, distance_right, distance_left):
    global leftSpeed, rightSpeed, inicio, search, tatakae
    
    if inicio == True:
        leftSpeed, rightSpeed = startou(distance_right, distance_left, back_left, back_right)
    else:
        leftSpeed, rightSpeed = search_mode(distance_right, distance_left)
    if tatakae == True:
        leftSpeed, rightSpeed = ninja_attack(front_left, front_right, distance_right, distance_left, back_left, back_right)
        

        
    return {'leftSpeed': leftSpeed, 'rightSpeed': rightSpeed}