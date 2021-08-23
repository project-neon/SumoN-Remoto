cont = 0;
estado = 1;
tre = 16;
contTre = 0;
ini = 14;
def control(front_right, front_left, back_right, back_left, distance_right, distance_left):
    global cont
    global estado
    global tre
    global contTre
    global ini
    leftSpeed=40;
    rightSpeed=40;
    Fspeed = 40;
    
    if ini>0:
        leftSpeed=40;
        rightSpeed=-40;
        ini-=1;
    
    elif cont <=0:
        if estado == 1:
            if contTre > tre/2:
                leftSpeed=Fspeed;
                rightSpeed=Fspeed-5;
             
            elif contTre <tre/2:
                leftSpeed=Fspeed-5;
                rightSpeed=Fspeed;
                ##if contTre % 2 == 0:
                ##    leftSpeed=-20;
                  ##  rightSpeed=40; 
            contTre -=1;
            
        if estado == 3:
            leftSpeed=Fspeed;
            rightSpeed=Fspeed;
        
        
        
        if distance_right<300 or distance_left <300:
            estado = 3;
            if contTre == 0:
                contTre = tre;
    
        elif (front_right<0.25 and front_left<0.25) :
            estado = 1;
            if contTre == 0:
                contTre = tre;
        
        elif distance_right==300 and distance_left ==300:
            estado = 2;
            cont = 25;
        else:
            estado =1;
            
        ini -=1;
       
    
    if estado == 2:
        if distance_right==300 and distance_left ==300:
            leftSpeed=30;
            rightSpeed=-30;
        
        elif distance_right<300 or distance_left <300:
            leftSpeed=Fspeed;
            rightSpeed=Fspeed;
            
        elif front_right<0.25 and front_left<0.25  :
            leftSpeed=Fspeed;
            rightSpeed=Fspeed;
        
                
        cont-=1;
    

    return {
        'leftSpeed': leftSpeed,
        'rightSpeed': rightSpeed,
        'log': [
            { 'name': 'Distance Left', 'value': distance_left, 'min': 0, 'max': 300 },
            { 'name': 'ddd', 'value': front_right, 'min': 0, 'max': 1 },
            { 'name': 'eee', 'value': front_left, 'min': 0, 'max': 1 }
        ]
    }
