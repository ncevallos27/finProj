//
// Created by Nico Cevallos on 11/17/25.
//

#include "payoff.h"

void Payoff::getPayoffVector(std::vector<double> &prices, double strike) {
	for (double & price : prices) {
		price = this->calculate(price, strike);
	}
}

