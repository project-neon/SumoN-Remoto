Sensores.cpp





int SensorL=A2; 
int SensorR=A3;
int SensorLeitura; // We define variable for storing sensor output.

void Sensores::Init(){
	
pinMode(SensorL, INPUT); // Sensor1 is declared as input
pinMode(SensorR, INPUT); // Sensor1 is declared as input

}


void Linhas::Init(){

	 // line sensor
  pinMode(lineL, INPUT); // DO NOT CHANGE / NAO MUDAR / NO CAMBIAR
  pinMode(lineR, INPUT); // DO NOT CHANGE / NAO MUDAR / NO CAMBIAR
 

}

void setup() {

Serial.begin(9600); // Serial communication started with 9600 bits per second.

}


/*
value=digitalRead(Sensor1); // Sensor is read digitally and reflected to value.
Serial.print("Sensor Output: "); //IT will write Sensor Output to Serial Monitor Screen.
Serial.println(value); // It will write value variable raw value (0 or 1)
delay(100); // We added 100ms Delay for more balanced readings.