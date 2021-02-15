ironcup-remote.ino

#include "motors.h"
#include "Linhas.h"
#include "Dist.h"
#include "config.h"

int SensorL_Detect;
int SensorR_Detect;
int flag = 0;

float LineL_read;
float LineR_read;

void setup {


	Serial.begin(9600);
	Serial.println("Setup Start...  ");
	Motors::init();
	Dist::init();
 	Linhas::init();

 	/***************INITIAL CONDITIONS***************** ----------inatel*/
 	 digitalWrite(LED, LOW); // LED off / LED desligado / LED apagado 
 	 Motors::stop() // left motor stopped / motor esquerdo parado / motor izquierdo parado 
 	 /*************INITIAL CONDITIONS - END*************/

}



void loop {

	if(Linhas::danger()){
		if(Dist::rightRead() && Dist::leftRead()){ // Taca-le pau Marcos
			Motors::driveTank(100,100);
		}

		else if(Dist::rightRead() && !Dist::leftRead()){ // adjusting the direction
			Motors::driveTank(0,50); // Confirmar a direcao
			flag = 0;
		}

		else if(!Dist::rightRead() && Dist::leftRead()){  // adjusting the direction
			Motors::driveTank(50,0); // Confirmar a direcao
			flag = 1;
		}

		else{ // Looking for the enemy
			flag == 1 ? Motors::driveTank(50,25) : Motors::driveTank(25,50); // 
		}
	}

	else(Linhas::danger()){
		Motors::driveTank(-100,-100);
	}
}