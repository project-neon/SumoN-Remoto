
#include "config.h"


#ifndef DIST_H
#define DIST_H


class Dist{
public:

  // Initialize pins
  static void init();

  // get value form sensors

  static int rightRead();

  static int leftRead();
};

#endif