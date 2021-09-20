#include <LiquidCrystal.h> // includes the LiquidCrystal Library 
#include <Keypad.h>
#include <Servo.h>

#define buzzer 10
#define echoPin 8

long duration;
int screenOffMsg =0;
String password="1234";
String tempPassword;
boolean activated = false; // State of the alarm
boolean isActivated;
boolean activateAlarm = false;
boolean alarmActivated = false;
boolean enteredPassword; // State of the entered password to stop the alarm
boolean passChangeMode = false;
boolean passChanged = false;
const byte ROWS = 4; //four rows
const byte COLS = 4; //four columns
char keypressed;
Servo myServo;


//define the symbols on the buttons of the keypads
char keyMap[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};

byte rowPins[ROWS] = {9, 8, 7, 6}; //Row pinouts of the keypad
byte colPins[COLS] = {5, 4, 3, 2}; //Column pinouts of the keypad
Keypad myKeypad = Keypad( makeKeymap(keyMap), rowPins, colPins, ROWS, COLS); 
LiquidCrystal lcd(A0, A1, A2, A3, A4, A5); // Creates an LC object. Parameters: (rs, enable, d4, d5, d6, d7) 


void setup() { 
  lcd.begin(16,2); 
  pinMode(buzzer, OUTPUT); // Set buzzer as an output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  
  
}

void loop() {

    myServo.attach(13); //locks the safebox
  
    if (screenOffMsg == 0 ){
      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("A - Enter Password");
      lcd.setCursor(0,1);
      lcd.print("B - Change Pass");
      screenOffMsg = 1;
    }
    keypressed = myKeypad.getKey();
     if (keypressed == 'A'){  
      tone(buzzer, 1000, 200);
      enterPassword();
    }
    else if (keypressed == 'B') {
      int i=1;
      tone(buzzer, 2000, 100);
      tempPassword = "";
      message("Current Password",">", 0);
      passChangeMode = true; 
      while(passChangeMode) {      
      keypressed = myKeypad.getKey();
      if (keypressed != NO_KEY){
        if (keypressed == '0' || keypressed == '1' || keypressed == '2' || keypressed == '3' ||
            keypressed == '4' || keypressed == '5' || keypressed == '6' || keypressed == '7' ||
            keypressed == '8' || keypressed == '9' ) {
         tempPassword += keypressed;
         lcd.setCursor(i,1);
         lcd.print("*");
         i++;
         tone(buzzer, 2000, 100);
        }
      }
      
      if (i > 5 || keypressed == '#') {
    /**starts over if the user presses
        more buttons than requested or 
        presses # to exit  */
        tempPassword = "";
        i=1;
        message("Current Password",">", 0); 
      }
      if ( keypressed == '*') {
        i=1;
        tone(buzzer, 2000, 100);
        if (password == tempPassword) {
          tempPassword="";
          message("Set New Password",">", 0);
          while(passChangeMode) {
            keypressed = myKeypad.getKey();
            if (keypressed != NO_KEY){
              if (keypressed == '0' || keypressed == '1' || keypressed == '2' || keypressed == '3' ||
                  keypressed == '4' || keypressed == '5' || keypressed == '6' || keypressed == '7' ||
                  keypressed == '8' || keypressed == '9' ) {
                tempPassword += keypressed;
                lcd.setCursor(i,1);
                lcd.print("*");
                i++;
                tone(buzzer, 2000, 100);
              }
            }
            if (i > 5 || keypressed == '#') {
              message("Set New Password","", 0);
            }
            if ( keypressed == '*') {
              i=1;
              tone(buzzer, 2000, 100);
              password = tempPassword;
              passChangeMode = false;
              passChanged = false;
              message("Password changed","successfully!", 0);
              delay(2000);
              screenOffMsg = 0;
            }            
          }
        }
      }
    }
   }
 }


void message(char *say1, char *say2, int time) {
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print(say1);
    lcd.setCursor(0,1);
    lcd.print(say2); 
    delay(time);
}

void enterPassword() {
  int k=5;
  int t=3;
  tempPassword = "";
  activated = true;
  message("Password",">", 0);
      while(activated) {
      keypressed = myKeypad.getKey();
      if (keypressed != NO_KEY){
        if (keypressed == '0' || keypressed == '1' || keypressed == '2' || keypressed == '3' ||
            keypressed == '4' || keypressed == '5' || keypressed == '6' || keypressed == '7' ||
            keypressed == '8' || keypressed == '9' ) {
          tempPassword += keypressed;
          lcd.setCursor(k,1);
          lcd.print("*");
          k++;
          tone(buzzer, 2000, 100);
        }
      }
      if (k > 9 || keypressed == '#') {
        tempPassword = "";
        k=5;
        message("Password",">", 0);
      }
      if ( keypressed == '*') {
        if ( tempPassword == password ) {
          activated = false;
          alarmActivated = false;
          noTone(buzzer);
          screenOffMsg = 0;
          myServo.write(117); //unlocks the safe!
          int time = 461.53*2;
          tone(buzzer, 523.25, time/2);
          tone(buzzer, 523.25, time/2);
          tone(buzzer, 523.25, time/2);
          tone(buzzer, 523.25, time);
          tone(buzzer, 51.91, time);
          tone(buzzer, 58.27, time);
          tone(buzzer, 523.25, time);
          tone(buzzer, 58.27, time/2);
          tone(buzzer, 523.25, time*2);
          message("Vault opened","successfully!", 3000);
          
          
          
        }
        else if (tempPassword != password) {
          message("Wrong password!","", 2000);
          t--;
          if (t == 0){ //ALARM
          tone(buzzer, 2000, 100);
          message("You thief >:( ", "", 18000000);
          }
          else{
          lcd.print("Tries left: ");
          lcd.print(t);
          lcd.setCursor(0,1);
          lcd.print("Pass >");
          }
        }
        
      }    
    }
   }
