//V11

var inicio = 'r';              //initial condition, 'r'=rear, 'f'=foward, 'e'=estrategy
var left_speed, right_speed;   //motor's variables
var speed = 45;                //speed MAX set point
var enemyPos = 1;              //memory of enemy position, 0=left, 1=center, 2=right
var last = 1;                  //last enemy position memory

function control(front_right, front_left, back_right, back_left, distance_right, distance_left) {

//--------- CALCULATE ENEMY POSITION -------------
    
    enemyPos = distance_left - distance_right;
    
   
    if(enemyPos >= 10){
        enemyPos = 2; //enemy to the right
    }else if (enemyPos <= -10){
        enemyPos = 0; //enemy to the left
    }else {
        if(last == 2){
            enemyPos = 2; // last enemy position to the right
        }else if (last == 0){
            enemyPos = 0; // last enemy position to the left
        }else {
            enemyPos = 1; //enemy in the center or lost enemy
        }
    }
    
    last = enemyPos;    //capture the last enemy position
    
//---------------- VERIFICATIONS ----------------  
    
    //if the back_sensor > 0.5, go to the 'foward'
    if (back_left > 0.5){
        left_speed = speed*0.9;
        right_speed = speed*0.7;
        inicio = 'f';
    
    // if the front_sensor > 0.5, go to 'estrategy'    
    }else if (front_right > 0.5){
        //turn to the left
        left_speed = speed*-0.875;
        right_speed = speed*0.875;
        inicio = 'e';
        last = 1; //'last' changed
    }else if(front_left > 0.5){
        //turn to the right
        right_speed = speed*-0.875;
        left_speed = speed*0.875;
        inicio = 'e';
        last = 1;//'last' changed

//--------- MAKE DECISIONS ------------------        
    
    //if the enemy position is '2', then the last position is 'right'     
    }else if(enemyPos == 2){
        //go! go! go!
        right_speed = speed*0.9;
        left_speed = speed*0.9;
        
    //if the enemy position is '0', then the last position is 'left'    
    }else if(enemyPos == 0){
        // go! go! go! again kkkkkkk
        left_speed = speed*0.9;
        right_speed = speed*0.9;

//------- INITIAL CONDITION ---------------
        
    //initial condition
    }else if(inicio === 'r' ){
        //go to te back
        left_speed = speed * -0.9;
        right_speed = speed * -0.9;

        
//----------- ESTARTEGY, MAYBE ----------------- 
        
    //if the enemy is ahead
    }else if (enemyPos == 1 && distance_left < 300){
        // go! go! go! more faster!!!!!
        left_speed = speed;
        right_speed = speed;
        
    //if 'inicio' = 'f', o to the foward    
    }else if (inicio === 'f'){
        //turn looking for enemy
        left_speed = speed*0.9;
        right_speed = speed*-0.9;
    }
    
    
    //OUTPUTS
    return { 
        leftSpeed: left_speed, 
        rightSpeed: right_speed,
    };
}