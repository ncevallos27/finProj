#include "binomialTree.h"

#include <cmath>
#include <sstream>

BinomialTree::BinomialTree(int paths, double timeStep, double discount) : Pricer(paths, timeStep, discount, PricerType::BinomialTree) {
	this->u = 0;
	this->d = 0;
}

BinomialTree::BinomialTree(int paths, double timeStep, double discount, double u, double d) : Pricer(paths, timeStep, discount, PricerType::BinomialTree), u(u), d(d) {}

// TODO: this needs to be sorted as well as the improper setup() command, this might cuase some tech debt
void BinomialTree::calcUp(double vol) {
	this->u = std::exp(vol * std::sqrt(this->timeStep));
	this->d = 1/this->u;
}

double BinomialTree::getProb() {
	// (exp(r * timeStep) - d) / (u - d)
	return (std::exp(r * timeStep) - d) / (u - d);
}

void BinomialTree::priceIndependent(std::vector<std::vector<double>> &prices, double start, int step) {
	prices.clear();
	prices.reserve(step + 1);

	// start * u^i * d^(step - i), i from 0 to step
	for (int i = 0; i <= step; ++i) {
		double price = start * std::pow(u, i) * std::pow(d, step - i);
		prices.emplace_back(std::vector{price});
	}
}

void BinomialTree::setup(double vol, double drift) {
	if (this->u == 0) {
		this->calcUp(vol);
	}
}
