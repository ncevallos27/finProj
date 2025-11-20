//
// Created by Nico Cevallos on 11/17/25.
//

#ifndef PAYOFF_H
#define PAYOFF_H
#include <vector>

enum class Path {
	Dependent, Independent
};

class Payoff {
public:
	explicit Payoff(Path type);
	virtual ~Payoff() = default;

	void getPayoffVector(std::vector<std::vector<double>> &prices, double strike);

	virtual void calculate(std::vector<double> &price, double strike) = 0;

	[[nodiscard]] Path getType() const;
protected:
	Path type;
};

#endif //PAYOFF_H
