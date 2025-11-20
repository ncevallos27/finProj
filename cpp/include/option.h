//
// Created by Nico Cevallos on 11/15/25.
//

#ifndef OPTION_H
#define OPTION_H

#include "payoff.h"
#include "stock.h"

enum class OptionPosition {
	Long, Short
};

class Option {
public:

	Option(const std::shared_ptr<Stock> &stock, const std::shared_ptr<Payoff> &payoff, double strike, double timeMaturity, OptionPosition position);

	double price();
	double price(double otherMaturity);
	[[nodiscard]] OptionPosition getPosition() const;

private:
	std::shared_ptr<Stock> stock;
	std::shared_ptr<Payoff> payoff;
	double strike;
	std::vector<std::vector<double>> prices;
	double timeMaturity;
	OptionPosition position;

};

#endif //OPTION_H
