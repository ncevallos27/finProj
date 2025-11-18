//
// Created by Nico Cevallos on 11/15/25.
//

#ifndef OPTION_H
#define OPTION_H

#include "payoff.h"
#include "stock.h"

enum class optionPosition {
	Long, Short
};

class Option {
public:

	Option(const std::shared_ptr<Stock> &stock, const std::shared_ptr<Payoff> &payoff, double strike, double timeMaturity, optionPosition position);

	double price();
	double price(double otherMaturity);
	[[nodiscard]] optionPosition getPosition() const;
	[[nodiscard]] double getPayoff(double price) const;

private:
	std::shared_ptr<Stock> stock;
	std::shared_ptr<Payoff> payoff;
	double strike;
	std::vector<double> prices;
	double timeMaturity;
	optionPosition position;

};

#endif //OPTION_H
