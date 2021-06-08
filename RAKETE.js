//V7
var left_speed, right_speed;   //variáveis usadas para atribuir valores aos motores das rodas.
var speed = 45;                //valor máximo da velocidde;                
var count = 30;                //contador inicial de tempo  (tempo real=count/60)


function control(front_right, front_left, back_right, back_left, distance_right, distance_left) {
    
    
    // vai pra trás no inicio por 0,5 segundo
    // estratégia para sair do campo de visão inicialmente
    if (count>0 && (distance_right-distance_left)==0){
        left_speed = speed*-0.8;
        right_speed = speed*-0.7;
        count = count - 1;
    }
    
    //ao terminar a contagem, verifica se chegou na borda e começa a procurar o adversário
    else if(back_left > 0){
        right_speed = speed*0.5;
        left_speed = speed*0.8;
    }else if(back_right > 0){
        left_speed = speed*0.5;
        right_speed = speed*0.8;
    }else if(front_right > 0){
        left_speed = speed * -0.8;
        right_speed = speed * 0.8;
    }else if(front_left > 0){
        left_speed = speed * 0.8;
        right_speed = speed * -0.8;
    }
    
    //quando encontra algum adversário, gira para o lado em que ele está.
    else if(distance_left < 300){
        right_speed = speed*0.9;
        left_speed = speed*0.7;
    }else if(distance_right < 300){
        left_speed = speed*0.9;
        right_speed = speed*0.7;
    }
    
    //se não encontra nenhum inimigo, gira em seu próprio eixo procurando o adversário
    else if((Math.abs(distance_right - distance_left))<=1){
        left_speed = speed*0.6;
        right_speed = speed*-0.3;
    }
    
    //outpus
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