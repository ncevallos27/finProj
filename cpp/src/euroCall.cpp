//
// Created by Nico Cevallos on 11/17/25.
//

#include "euroCall.h"

EuroCall::EuroCall() : Payoff(Path::Independent) {}

void EuroCall::calculate(std::vector<double> &price, double strike) {
	price.back() = std::max(price.back()-strike, 0.0);
}

