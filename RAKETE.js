//V9
var speedL, speedR;
var speed = 45;
var mem = 'r'; // m -> mid     r -> right     l -> left
var inicio = 0;

function control(front_right, front_left, back_right, back_left, distance_right, distance_left) {
    var sensorR = distance_right;
    var sensorL = distance_left;
    
    var error = 0 - (sensorL - sensorR);
    
    speedR = speed * (error/300);
    speedL = speed * (error/300) * (-1);
    
    if(Math.abs(error) <= 10 && (sensorR < 300 && sensorL < 300)){
        mem = 'm';
    }else if (error > 0){
        mem = 'l';
    }else if (error < 0){
        mem = 'r';
    }else{
        speedR = speed * -0.2;
        speedL = speed * 0.9;
    }
    
    switch (mem){
            
        case 'l':
            speedR = speed * 0.8;
            speedL = speed * 0.2;
            break;
        case 'r':
            speedL = speed * 0.8;
            speedR = speed * 0.2;
            break;
        case 'm':
            speedR = speed * 0.9;
            speedL = speed * 0.9;
            break;
        default: break;
    }
    
  
    
    
    if(front_left > 0.8 || front_left > 0.8){
        speedR = speed*-0.5;
        speedL = speed*-0.9;
    }
    
    if(inicio < 25){
        speedR = speed * -0.9;
        speedL = speed * -0.15;
        inicio++;
    }
    return {
        leftSpeed: speedL,
        rightSpeed: speedR,
        /*log : [
            {name: 'Left',  value: left_speed, min: -45, max: 45},
            {name: 'Right', value: right_speed, min: -45, max: 45},
            {name: 'LeftDist', value: distance_left, min: 0, max: 300},
            {name: 'RightDist', value: distance_right, min: 0, max: 300}
        ]*/
    };
}