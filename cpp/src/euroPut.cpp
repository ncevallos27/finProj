//
// Created by Nico Cevallos on 11/17/25.
//

#include "euroPut.h"

EuroPut::EuroPut(double strike) : Payoff(strike) {}

double EuroPut::calculate(double price) {
	return std::max(this->strike-price, 0.0);
}

