//
// Created by Nico Cevallos on 11/17/25.
//

#ifndef PAYOFF_H
#define PAYOFF_H
#include <vector>

enum class Path {
	Dependent, Independent
};

enum class PayoffType {
	Call, Put, Unknown
};

class Payoff {
public:
	explicit Payoff(Path type, PayoffType payoffType);
	virtual ~Payoff() = default;

	std::vector<double> getPayoffVector(std::vector<std::vector<double>> &prices, double strike);

	virtual double calculate(std::vector<double> &price, double strike) = 0;

	[[nodiscard]] Path getType() const;

	double fakeCalcuate(double price, double strike);

protected:
	Path type;
	PayoffType payoffType;
};

#endif //PAYOFF_H
