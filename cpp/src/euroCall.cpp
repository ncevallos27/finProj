//
// Created by Nico Cevallos on 11/17/25.
//

#include "euroCall.h"

double EuroCall::calculate(double price, double strike) {
	return std::max(price-strike, 0.0);
}

