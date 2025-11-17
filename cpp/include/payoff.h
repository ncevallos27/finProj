//
// Created by Nico Cevallos on 11/17/25.
//

#ifndef PAYOFF_H
#define PAYOFF_H
#include <vector>

class Payoff {
public:
	Payoff() = default;
	virtual ~Payoff() = default;

	void getPayoffVector(std::vector<double> &prices, double strike);

	virtual double calculate(double price, double strike) = 0;
};

#endif //PAYOFF_H
