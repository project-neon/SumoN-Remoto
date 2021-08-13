left_speed = 0      
right_speed = 0     
speed = 40          

erro = 0
flag = 0
margem = 50

count = 1
var = 1

def ctrl(distance_right, distance_left):
    global erro, flag, left_speed, right_speed, speed,margem
    
    erro = (distance_left - distance_right)
    
    if erro == 0:
        if distance_left >= 300:
            if flag == 0:
                left_speed = speed
                right_speed = -speed
            else: 
                left_speed = -speed
                right_speed = speed
    else:
        if erro > 0 : 
            flag = 0
        if erro < 0 : 
            flag = 1
     
        left_speed = (speed*0.5) * (erro)/300 + (speed*0.4)
        right_speed = (speed*0.5) * -(erro)/300 + (speed*0.4)
    
    return left_speed, right_speed,erro,flag

def manobra(var):
    global left_speed, right_speed, count
    
    if var == 2:
        left_speed = speed*0.9
        right_speed = speed*0.9
        count = count+1
        
    if count >40:
        left_speed = speed
        right_speed = speed
        count = count+1
     
    if count > 60:
        var = 'atk'
        count = 1
        
    return left_speed, right_speed,var,count

def control(front_right, front_left, back_right, back_left, distance_right, distance_left):
    global left_speed, right_speed,erro, margem, var,count
    
    left_speed,right_speed,erro,flag = ctrl(distance_right, distance_left)
    
    if (distance_right < 40 or distance_left < 40) and var ==1:
        var = 2
    
    if var == 2:
        left_speed, right_speed,var,count = manobra(var)
        
    
    if erro > -margem and erro < margem and distance_left < 300 and var == 'atk':
        left_speed = speed
        right_speed = speed
    
    if front_left > 0.8 or front_right > 0.8:
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