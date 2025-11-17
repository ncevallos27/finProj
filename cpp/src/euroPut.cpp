//
// Created by Nico Cevallos on 11/17/25.
//

#include "euroPut.h"

double EuroPut::calculate(double price, double strike) {
	return std::max(strike-price, 0.0);
}

