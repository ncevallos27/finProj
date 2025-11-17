//
// Created by Nico Cevallos on 11/15/25.
//

#ifndef OPTION_H
#define OPTION_H

#include "payoff.h"
#include "stock.h"

class Option {
public:

	Option(const std::shared_ptr<Stock> &stock, const std::shared_ptr<Payoff> &payoff, double strike, double timeMaturity);

	double price();
	double price(double otherMaturity);

private:
	std::shared_ptr<Stock> stock;
	std::shared_ptr<Payoff> payoff;
	double strike;
	std::vector<double> prices;
	double timeMaturity;
};

#endif //OPTION_H
