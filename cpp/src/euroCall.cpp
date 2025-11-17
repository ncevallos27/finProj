//
// Created by Nico Cevallos on 11/17/25.
//

#include "euroCall.h"

EuroCall::EuroCall(double strike) : Payoff(strike) {}

double EuroCall::calculate(double price) {
	return std::max(price-this->strike, 0.0);
}

