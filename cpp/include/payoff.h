//
// Created by Nico Cevallos on 11/17/25.
//

#ifndef PAYOFF_H
#define PAYOFF_H
#include <vector>

class Payoff {
public:
	explicit Payoff(double strike);
	virtual ~Payoff() = default;

	std::vector<double>& getPayoffVector(std::vector<double> &prices);

	virtual double calculate(double price) = 0;

protected:
	double strike;
};

#endif //PAYOFF_H
