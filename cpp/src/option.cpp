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
	this->stock->price(this->prices, static_cast<int>(totalSteps));
	this->payoff->getPayoffVector(this->prices, strike);

	double startPrice = 0;
	double prob = this->stock->getPricerProb();
	switch(this->stock->getPricerIndentity()) {
		case PricerType::BinomialTree:
			for (unsigned int i = 0; i < this->prices.size(); i++) {
				double binom = std::tgamma(this->prices.size()) / (std::tgamma(i + 1) * std::tgamma(this->prices.size() - i));
				startPrice += binom * this->prices[i] * std::pow(prob, i) * std::pow(1 - prob, this->prices.size() - 1 - i);
			}
			startPrice = startPrice * std::exp(-1 * this->stock->getPricerDiscount() * otherMaturity);
			break;
		default:
			break;
	}

	return startPrice;
}

OptionPosition Option::getPosition() const {
	return this->position;
}

double Option::getPayoff(const double price) const {
	return this->payoff->calculate(price, this->strike);
}
