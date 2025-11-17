#include "binomialTree.h"

#include <cmath>
#include <sstream>

BinomialTree::BinomialTree(int paths, double timeStep, double discount) : Pricer(paths, timeStep, discount) {
	this->u = 0;
	this->d = 0;
}

BinomialTree::BinomialTree(int paths, double timeStep, double discount, double u, double d) : Pricer(paths, timeStep, discount), u(u), d(d) {}

void BinomialTree::calcUp(double vol) {
	this->u = std::exp(vol * std::sqrt(this->timeStep));
	this->d = 1/this->u;
}

double BinomialTree::getProb() {
	// (exp(r * timeStep) - d) / (u - d)
	return (std::exp(r * timeStep) - d) / (u - d);
}

std::vector<double> BinomialTree::price(double start, int step) {
	std::vector<double> prices;
	prices.reserve(step + 1);

	// start * u^i * d^(step - i), i from 0 to step
	for (int i = 0; i <= step; ++i) {
		double price = start * std::pow(u, i) * std::pow(d, step - i);
		prices.push_back(price);
	}

	return prices;
}

std::string BinomialTree::identify() {
	std::stringstream ss;
	ss << "BinomialTree";
	return ss.str();
}

void BinomialTree::setup(double vol) {
	if (this->u == 0) {
		this->calcUp(vol);
	}
}
