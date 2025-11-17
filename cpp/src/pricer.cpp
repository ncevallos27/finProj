//
// Created by Nico Cevallos on 11/15/25.
//


#include "pricer.h"

Pricer::Pricer(int paths, double timeStep, double discount) : paths(paths), timeStep(timeStep), r(discount), currentTime(0) {}
