//
// Created by Nico Cevallos on 11/17/25.
//

#include "payoff.h"

Payoff::Payoff(Path type, PayoffType payoffType) : type(type), payoffType(payoffType) {}

std::vector<double> Payoff::getPayoffVector(std::vector<std::vector<double>>&prices, double strike) {
	std::vector<double> payoffs;

	payoffs.reserve(prices.size());
	for (auto &price : prices) {
		payoffs.emplace_back(this->calculate(price, strike));
	}

	return payoffs;
}

Path Payoff::getType() const {
	return this->type;
}

double Payoff::fakeCalcuate(double price, double strike) {
	std::vector payoffs{price};
	return this->calculate(payoffs, strike);
}
