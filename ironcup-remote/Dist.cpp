
#include "config.h"
#include "Dist.h"
// Initialize pins

void Dist::init(){

	// line sensor
    pinMode(SensorL, INPUT); // Sensor1 is declared as input
    pinMode(SensorR, INPUT); // Sensor1 is declared as input

}

int Dist::rightRead(){

	 // line sensor
  return(digitalRead(SensorR)); // DO NOT CHANGE / NAO MUDAR / NO CAMBIAR
  
}

int Dist::leftRead(){

	 // line sensor
  return(digitalRead(SensorL)); // DO NOT CHANGE / NAO MUDAR / NO CAMBIAR
  
}