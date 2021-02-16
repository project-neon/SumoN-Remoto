#include "config.h"
#include "motors.h"
// Initialize pins
void Motors::init(){

 
  // left motor
  pinMode(pwmL, OUTPUT);        // left motor power
  pinMode(leftMotor1, OUTPUT);  // left motor dir.
  pinMode(leftMotor2, OUTPUT);  // left motor dir.


  // right motor
  pinMode(pwmR, OUTPUT);        // right motor power
  pinMode(rightMotor1, OUTPUT); // right motor dir.
  pinMode(rightMotor2, OUTPUT); // right motor dir.

  
}

void Motors::driveTank(float m1, float m2){

  // Limit Powers
  m1 = min(max(m1, -100), 100);
  m2 = min(max(m2, -100), 100);

  // Map powers
  int powerOutL = m1 * (MOTOR_ABS_MAX / 100.0);
  int powerOutR = m2 * (MOTOR_ABS_MAX / 100.0);

  // Set power
  analogWrite(pwmL,powerOutL);
  analogWrite(pwmR,powerOutR);

  // Set Directions

  digitalWrite(leftMotor1, m1 > 0 ? LOW : HIGH);
  digitalWrite(leftMotor2, m1 > 0 ? HIGH : LOW);

  digitalWrite(rightMotor1, m2 > 0 ? LOW : HIGH);
  digitalWrite(rightMotor2, m2 > 0 ? HIGH : LOW);
}

void Motors::driveTankforMillis(float m1, float m2,int milis){
  // Limit Powers
  m1 = min(max(m1, -100), 100);
  m2 = min(max(m2, -100), 100);

  // Map powers
  int powerOutA = m1 * (MOTOR_ABS_MAX / 100.0);
  int powerOutB = m2 * (MOTOR_ABS_MAX / 100.0);

  // Set power
  //SoftPWMSetPercent(pwmL, abs(powerOutA));
  //SoftPWMSetPercent(pwmR, abs(powerOutB));
  //analogWrite(pwmL,abs(powerOutA));
 //analogWrite(pwmR,abs(powerOutB));
 // Set power (100)
  //digitalWrite(pwmL, HIGH);
  //digitalWrite(pwmR, HIGH);
  // Set Directions
  digitalWrite(leftMotor1, m1 > 0 ? HIGH : LOW);
  digitalWrite(leftMotor2, m1 > 0 ? LOW : HIGH);

  digitalWrite(rightMotor1, m2 > 0 ? HIGH : LOW);
  digitalWrite(rightMotor2, m2 > 0 ? LOW : HIGH);
 // delay(milis);
   // Set power (0)
  //digitalWrite(pwmL, LOW);
  //digitalWrite(pwmR, LOW);
  return;
}

void Motors::stop(){
  // Set power (0)
  digitalWrite(pwmL, LOW);
  digitalWrite(pwmR, LOW);

  // Set both DIRS to 0
  digitalWrite(leftMotor1, HIGH);
  digitalWrite(leftMotor2, HIGH);

  digitalWrite(rightMotor1, HIGH);
  digitalWrite(rightMotor2, HIGH);
}