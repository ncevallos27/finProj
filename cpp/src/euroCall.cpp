//
// Created by Nico Cevallos on 11/17/25.
//

#include "euroCall.h"

EuroCall::EuroCall() : Payoff(Path::Independent) {}

double EuroCall::calculate(std::vector<double> &price, double strike) {
	return std::max(price.back()-strike, 0.0);
}

