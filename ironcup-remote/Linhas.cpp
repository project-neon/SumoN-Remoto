#include "config.h"
#include "Linhas.h"
// Initialize pins

void Linhas::init(){


	 // line sensor
  pinMode(lineL, INPUT); // DO NOT CHANGE / NAO MUDAR / NO CAMBIAR
  pinMode(lineR, INPUT); // DO NOT CHANGE / NAO MUDAR / NO CAMBIAR
 

}


int Linhas::NotInDanger(){
     

     int threshold = 800;


	 // line sensor
     if(analogRead(lineR)<threshold||analogRead(lineL)<threshold){
         return 0;
     } 

     else{
         return 1;
     }
     
}

  