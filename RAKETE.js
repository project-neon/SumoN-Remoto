//V10
var inicio = 0;
var left_speed, right_speed;
var speed = 45;
function control(front_right, front_left, back_right, back_left, distance_right, distance_left) {

   if(back_left > 0.8){
        right_speed = speed*0.9;
        left_speed = speed*0.9;
        inicio = 1;
    }else if(inicio === 0 ){
        left_speed = speed * -0.9;
        right_speed = speed * -0.9;
    }else if (front_right > 0.8){
        left_speed = speed*-0.8;
        right_speed = speed*0.8;
    }else if(front_left > 0.8){
        right_speed = speed*-0.8;
        left_speed = speed*0.8;
    }else if(distance_left < 300){
        right_speed = speed*0.9;
        left_speed = speed*0.85;
    }else if(distance_right < 300){
        left_speed = speed*0.9;
        right_speed = speed*0.85;
    }
    
    return { leftSpeed: left_speed,    rightSpeed: right_speed,   };
}