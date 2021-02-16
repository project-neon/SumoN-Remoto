#include "config.h"

#ifndef LINHAS_H
#define LINHAS_H


class Linhas{
public:

  // Initialize pins
  static void init();

  // verify if robot is at treshold white value
  static int danger();

};

#endif