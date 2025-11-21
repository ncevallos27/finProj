//
// Created by Nico Cevallos on 11/15/25.
//

#ifndef STOCK_H
#define STOCK_H
#include <vector>

#include "pricer.h"

class Stock {
public:
	Stock(const std::shared_ptr<Pricer> &model, double start, double vol, double drift);

	void price(int step);

	double getPricerTimeStep() const;
	PricerType getPricerIdentity();
	double getPricerDiscount() const;

	double getPricerProb() const;

	[[nodiscard]] std::vector<std::vector<double>>& getRefPrices();

private:
	bool priced;
	double lastPricedStep;
	double drift;
	std::shared_ptr<Pricer> model;
	double start;
	double vol;
	std::vector<std::vector<double>> prices;
};

#endif //STOCK_H
