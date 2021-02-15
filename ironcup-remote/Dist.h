#include "_config.h"

#ifndef DIST_H
#define DIST_H


class Dist{
public:

  // Initialize pins
  static void init();

  // Set power of both motors
  static int rightRead();

  static int leftRead();
};

#endif