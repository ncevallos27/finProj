//
// Created by Nico Cevallos on 11/17/25.
//

#include "euroPut.h"

EuroPut::EuroPut() : Payoff(Path::Independent) {}

double EuroPut::calculate(std::vector<double> &price, double strike) {
	return std::max(strike-price.back(), 0.0);
}

