//
// Created by Nico Cevallos on 11/15/25.
//

#ifndef STOCK_H
#define STOCK_H
#include "pricer.h"

class Stock {
public:
	Stock(std::shared_ptr<Pricer> model, double start, double vol);

	std::vector<double> price(int step) const;
private:
	std::shared_ptr<Pricer> model;
	double start;
	double vol;
};

#endif //STOCK_H
