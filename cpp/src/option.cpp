//
// Created by Nico Cevallos on 11/17/25.
//


#include "option.h"

Option::Option(const std::shared_ptr<Stock> &stock, const std::shared_ptr<Payoff> &payoff, double strike, double timeMaturity, OptionPosition position) : stock(stock), payoff(payoff), strike(strike), timeMaturity(timeMaturity), position(position) {}

double Option::price() {
	return this->price(this->timeMaturity);
}

double Option::getExpectation(double otherMaturity) {
	double totalSteps = std::round(otherMaturity/this->stock->getPricerTimeStep());
	this->stock->price(static_cast<int>(totalSteps));
	std::vector<double> payoffs = this->payoff->getPayoffVector(this->stock->getRefPrices(), strike);

	double startPrice = 0;
	double prob = this->stock->getPricerProb();
	switch(this->stock->getPricerIdentity()) {
		case PricerType::BinomialTree:
			for (unsigned int i = 0; i < payoffs.size(); i++) {
				double binom = std::tgamma(payoffs.size()) / (std::tgamma(i + 1) * std::tgamma(payoffs.size() - i));
				startPrice += binom * payoffs[i] * std::pow(prob, i) * std::pow(1 - prob, payoffs.size() - 1 - i);
			}
			break;
		case PricerType::MonteCarlo:
			for (auto & payoffD : payoffs) {
				startPrice += payoffD * prob;
			}
		default:
			break;
	}

	return startPrice;
}

OptionPosition Option::getPosition() const {
	return this->position;
}

double Option::fakeCalculate(double price, double strike) {
	return this->payoff->fakeCalcuate(price, strike);
}

double Option::price(double otherMaturity) {
	return this->getExpectation(otherMaturity) * this->stock->getDiscount(otherMaturity);
}

double Option::getMaturity() {
	return this->timeMaturity;
}