#include "motors.h"
#include "Linhas.h"
#include "Dist.h"
#include "config.h"

int SensorL_Detect;
int SensorR_Detect;
int flag = 0;

float LineL_read;
float LineR_read;

int readDIP(){
  int n=0;
  if(digitalRead(DIP4)==HIGH)
    n=1;
  if(digitalRead(DIP3)==HIGH)
    n|= (1<<1);
  if(digitalRead(DIP2)==HIGH)
    n|= (1<<2);
  if(digitalRead(DIP1)==HIGH)
    n|= (1<<3);
  return n;
}

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


void newDriveTank(int a, int b){

	MotorL(a); 
	MotorR(b);

}


void SeekLine(){

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

		else{ // Looking for the enemy/next line
			flag == 1 ? newDriveTank(150,75) : newDriveTank(75,150); // 
		}
	}

	else{

		MotorL(-175);
		MotorR(-175);
		delay(100);
		MotorL(175);
		MotorR(-175);
		delay(60);
	}

}


void motorTest(){
	int speed = 100;

	MotorL(speed);
	MotorR(speed);
	delay(500);

	MotorL(-speed);
	MotorR(-speed);
	delay(500);

	MotorL(-speed);
	MotorR(speed);
	delay(500);

	MotorL(speed);
	MotorR(-speed);
	delay(500);

}


void dangerGuy(){
	
	unsigned long times = millis();
	boolean ledControl = true;

	if(Linhas::NotInDanger()){
		MotorL(0);
		MotorR(0);
		while (digitalRead(microST) == 0)
  		{
			if(millis() - times > 60 )
			{	 
  				digitalWrite(LED, ledControl);
				ledControl = !ledControl;
				times = millis();
			}
  		}
	}
	
	else{
		MotorL(-175);
		MotorR(-175);
		delay(100);
		MotorL(175);
		MotorR(-175);
		delay(60);
	}
}


void Tornado(){	

	if(Linhas::NotInDanger()){
		digitalWrite(LED,LOW);
		if(Dist::rightRead() && Dist::leftRead()){ // Taca-le pau Marcos
			MotorL(200);
			MotorR(200);
		}

		// else if(Dist::rightRead() && !Dist::leftRead()){ // adjusting the direction
		// 	MotorR(150); 
		// 	MotorL(0);/// Confirmar a direcao
		// 	flag = 0;
		// }

		// else if(!Dist::rightRead() && Dist::leftRead()){  // adjusting the direction
		// 	MotorL(150);
		// 	MotorR(0); // Confirmar a direcao
		// 	flag = 1;
		// }

		else{ // Looking for the enemy
			if(flag){
				
			MotorL(100);
			MotorR(0); 
	
					}
			else{
			MotorR(100);
			MotorL(0); 
		
			}
	}

	else(Linhas::NotInDanger());{

		MotorL(-175);
		MotorR(-175);
		delay(100);
		MotorL(175);
		MotorR(-175);
		delay(60);
	}

	if(digitalRead(microST==0)){
		MotorR(0);
		MotorL(0); 

	}
}


void setup() {


	pinMode(microST, INPUT);
	Motors::init();
	Dist::init();
 	Linhas::init();

 	/***************INITIAL CONDITIONS***************** ----------inatel*/
 	digitalWrite(LED, HIGH); // LED off / LED desligado / LED apagado 
 	Motors::stop(); // left motor stopped / motor esquerdo parado / motor izquierdo parado 
 	/*************INITIAL CONDITIONS - END*************/

	unsigned long times = 0;
	boolean ledControl = true;
	MotorL(0);
	MotorR(0);
  	while (digitalRead(microST) == 0)
  	{
		if((millis() - times) > 60 )
		{	 
  			digitalWrite(LED, ledControl);
			ledControl = !ledControl;
			times = millis();
		}
  	}

}


void loop() {


	digitalWrite(LED,HIGH); 

	digitalWrite(LED,LOW);

	int DIP_Result = readDIP();

	if(digitalRead(microST) == 1){
		if(DIP_Result==1){
			MotorL(100);
			MotorR(200);
			
		}
	}

	/*MotorL(75);
	MotorR(150);
	delay(60);*/

	while (digitalRead(microST) == 1){

		digitalWrite(LED, LOW); 
    	 
    	switch (DIP_Result) {
         case 0:
		  	dangerGuy();
            break;
          case 1:
			//estratégia para quando robô começa na posição 5B
			SeekLine();
            break;

		  case 2:
		  	motorTest();
        	break;
        
		  case 3:
		  	dangerGuy();
			break;

		  default:
            // comando(s)
            break;
    }

  	digitalWrite(LED, LOW); 
	
	}

}