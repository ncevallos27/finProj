//
// Created by Nico Cevallos on 11/17/25.
//

#include "payoff.h"

Payoff::Payoff(Path type) : type(type) {}

void Payoff::getPayoffVector(std::vector<std::vector<double>>&prices, double strike) {
	for (auto &price : prices) {
		this->calculate(price, strike);
	}
}

Path Payoff::getType() const {
	return this->type;
}