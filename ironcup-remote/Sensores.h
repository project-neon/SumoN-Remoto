Sensors.h

#include "config.h"


class Sensors{
public:

	static void init();
	
	static void Serial();

}


int Sensor1=5; // Digital sensor connected to D5 // We define variable for storing sensor output.

void setup() {

Serial.begin(9600); // Serial communication started with 9600 bits per second.
}


/*void loop() {
value=digitalRead(Sensor1); // Sensor is read digitally and reflected to value.
Serial.print("Sensor Output: "); //IT will write Sensor Output to Serial Monitor Screen.
Serial.println(value); // It will write value variable raw value (0 or 1)
delay(100); // We added 100ms Delay for more balanced readings.
}