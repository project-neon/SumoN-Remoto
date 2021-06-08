//V8
var inicio = 0;
var left_speed, right_speed;
var speed = 45;
function control(front_right, front_left, back_right, back_left, distance_right, distance_left) {
    
    var error = 0 - (distance_left - distance_right);
    
        
    if (front_right > 0.8 || front_left > 0.8){
        left_speed = speed*0.9;
        right_speed = speed*-0.9;
        
    }else if(Math.abs(error) <= 10 && distance_left < 300){
        right_speed = speed;
        left_speed = speed;
        
    }else if(error>0){
        right_speed = 0.9*speed*(error/300);
        left_speed = 0.9*speed*(error/300);
        
    }else if(error<0){
        error = Math.abs(error);
        right_speed = 0.9*speed*(error/300);
        left_speed = 0.9*speed*(error/300);
        
    }else if(distance_left < 300 || distance_right < 300){
        right_speed = speed*0.8;
        left_speed = speed*0.8;
        
    }else if((Math.abs(error))<=20){
        left_speed = speed*0.7;
        right_speed = speed*-0.1;
    }
    return {
        leftSpeed: left_speed,
        rightSpeed: right_speed,
        /*log : [
            {name: 'Left',  value: left_speed, min: -45, max: 45},
            {name: 'Right', value: right_speed, min: -45, max: 45},
            {name: 'LeftDist', value: distance_left, min: 0, max: 300},
            {name: 'RightDist', value: distance_right, min: 0, max: 300}
        ]*/
    };
}