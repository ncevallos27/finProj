//
// Created by Nico Cevallos on 11/17/25.
//

#include "payoff.h"

Payoff::Payoff(Path type) : type(type) {}

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