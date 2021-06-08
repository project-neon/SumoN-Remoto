//V6
var inicio = 0;
var left_speed, right_speed;
var speed = 45;
function control(front_right, front_left, back_right, back_left, distance_right, distance_left) {

   if(inicio == 0){
        right_speed = speed*0.9;
        left_speed = speed*0.6;
        inicio = 1;
    }else if (front_right > 0){
        left_speed = speed*0.8;
        right_speed = speed*-0.9;
        inicio = 1;
    }else if(front_left > 0){
        right_speed = speed*-0.9;
        left_speed = speed*0.7;
        inicio = 1;
    }else if(distance_left < 300){
        right_speed = speed*0.9;
        left_speed = speed*0.4;
    }else if(distance_right < 300){
        left_speed = speed*0.9;
        right_speed = speed*0.4;
    }else if((Math.abs(distance_right - distance_left))<=20){
        left_speed = speed*0.9;
        right_speed = speed*0.7;
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