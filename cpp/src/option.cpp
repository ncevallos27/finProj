//
// Created by Nico Cevallos on 11/17/25.
//


#include "option.h"

Option::Option(const std::shared_ptr<Stock> &stock, const std::shared_ptr<Payoff> &payoff, double strike, double timeMaturity, OptionPosition position) : stock(stock), payoff(payoff), strike(strike), timeMaturity(timeMaturity), position(position) {}

double Option::price() {
	return this->price(this->timeMaturity);
}

double Option::price(double otherMaturity) {
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
			startPrice = startPrice * std::exp(-1 * this->stock->getPricerDiscount() * otherMaturity);
			break;
		case PricerType::MonteCarlo:
			for (auto & payoffD : payoffs) {
				startPrice += payoffD * prob;
			}
			startPrice = startPrice * std::exp(-1 * this->stock->getPricerDiscount() * otherMaturity);
		default:
			break;
	}

	return startPrice;
}

OptionPosition Option::getPosition() const {
	return this->position;
}
