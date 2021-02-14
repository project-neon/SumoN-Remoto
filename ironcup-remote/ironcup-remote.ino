ironcup-remote.ino

#include "motors.h"
#include "config.h"

int SensorL_Detect;
int SensorR_Detect;

float LineL_read;
float LineR_read;



void setup {


	Serial.begin(9600);
	Serial.println("Setup Start...  ");
	Motors::init();
	Sensores::init();
 	/***************INITIAL CONDITIONS***************** ----------inatel*/
 	 digitalWrite(LED, LOW); // LED off / LED desligado / LED apagado 
 	 MotorL(0); // left motor stopped / motor esquerdo parado / motor izquierdo parado 
 	 MotorR(0); // right motor stopped / motor direito parado / motor derecho parado 
 	 /*************INITIAL CONDITIONS - END*************/
}



void loop {

	Motors::driveTank(100,100);

}