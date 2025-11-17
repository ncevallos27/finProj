//
// Created by Nico Cevallos on 11/17/25.
//

#include "payoff.h"

Payoff::Payoff(double strike) : strike(strike) {}

std::vector<double> &Payoff::getPayoffVector(std::vector<double> &prices) {
	for (double & price : prices) {
		price = this->calculate(price);
	}
	return prices;
}

