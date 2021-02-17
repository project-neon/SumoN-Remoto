#include "motors.h"
#include "Linhas.h"
#include "Dist.h"
#include "config.h"

int SensorL_Detect;
int SensorR_Detect;
int flag = 0;

float LineL_read;
float LineR_read;

void MotorL(int pwm){
  // leftMotor1=0 and leftMotor2=0 -> stopped / parado / parado 
  // leftMotor1=0 and leftMotor2=1 -> moves forward / avanca / avanzar
  // leftMotor1=1 and leftMotor2=0 -> moves back / recua / retrocede
  // leftMotor1=1 and leftMotor2=1 -> stopped (braked) / parado (travado) / parado (frenado)
 
  if(pwm==0){
    digitalWrite(leftMotor1, LOW);
    digitalWrite(leftMotor2, LOW);
  }
  else if(pwm<0)
  {
	digitalWrite(LED,HIGH);
    analogWrite(pwmL, -pwm);
    digitalWrite(leftMotor1, HIGH);
    digitalWrite(leftMotor2, LOW);
  }
  else
  {
    analogWrite(pwmL, pwm);
    digitalWrite(leftMotor1, LOW);
    digitalWrite(leftMotor2, HIGH);
  }
}
 
 
/**RIGHT MOTOR CONTROL / CONTROLE DO MOTOR DIREITO / CONTROL DEL MOTOR DERECHO**/
// pwm = 0 -> stopped / parado / parado
// 0<pwm<=255 -> forward / frente / adelante
// -255<=pwm<0 -> backward / tras / espalda
void MotorR(int pwm){
  // rightMotor1=0 and rightMotor2=0 -> stopped / parado / parado 
  // rightMotor1=0 and rightMotor2=1 -> moves forward / avanca / avanzar
  // rightMotor1=1 and rightMotor2=0 -> moves back / recua / retrocede
  // rightMotor1=1 and rightMotor2=1 -> stopped (braked) / parado (travado) / parado (frenado)
 
  if(pwm==0){
    digitalWrite(rightMotor1, LOW);
    digitalWrite(rightMotor2, LOW);
  }
  else if(pwm<0)
  {

	digitalWrite(LED,HIGH);
    analogWrite(pwmR, -pwm);
    digitalWrite(rightMotor1, HIGH);
    digitalWrite(rightMotor2, LOW);
  }
  else
  {
    analogWrite(pwmR, pwm);
    digitalWrite(rightMotor1, LOW);
    digitalWrite(rightMotor2, HIGH);
  }
}


/*void setup {


	Serial.begin(9600);
	Serial.println("Setup Start...  ");
	Motors::init();
	Sensores::init();
 	/***************INITIAL CONDITIONS***************** ----------inatel
	
 	 digitalWrite(LED, LOW); // LED off / LED desligado / LED apagado 
 	 MotorL(0); // left motor stopped / motor esquerdo parado / motor izquierdo parado 
 	 MotorR(0); // right motor stopped / motor direito parado / motor derecho parado 
 	 
	  /*************INITIAL CONDITIONS - END*************/



void Tornado(){	

	if(Linhas::NotInDanger()){
		digitalWrite(LED,LOW);
		if(Dist::rightRead() && Dist::leftRead()){ // Taca-le pau Marcos
			MotorL(200);
			MotorR(200);
		}

		else if(Dist::rightRead() && !Dist::leftRead()){ // adjusting the direction
			MotorR(175); 
			MotorL(0);/// Confirmar a direcao
			flag = 0;
		}

		else if(!Dist::rightRead() && Dist::leftRead()){  // adjusting the direction
			MotorL(175);
			MotorR(0); // Confirmar a direcao
			flag = 1;
		}

		else{ // Looking for the enemy
			flag == 1 ? MotorL(100) : MotorR(100); // 
		}
	}

	else(Linhas::NotInDanger());{

		MotorL(-175);
		MotorR(-175);
	}
}


void setup() {

	pinMode(microST, INPUT);
	Serial.begin(9600);
	Serial.println("Setup Start...  ");
	Motors::init();
	Dist::init();
 	Linhas::init();

 	/***************INITIAL CONDITIONS***************** ----------inatel*/
 	digitalWrite(LED, HIGH); // LED off / LED desligado / LED apagado 
 	Motors::stop(); // left motor stopped / motor esquerdo parado / motor izquierdo parado 
 	/*************INITIAL CONDITIONS - END*************/

  
  	while (digitalRead(microST) == 0)
  	{
  		digitalWrite(LED, HIGH);
		delay(60);
		digitalWrite(LED,LOW);
		MotorL(0);
		MotorR(0);
  	}
}



void loop() {

	digitalWrite(LED,HIGH); 

	digitalWrite(LED,LOW);

	while (digitalRead(microST) == 1){

  	digitalWrite(LED, LOW); 
	Tornado();
	
	}

}