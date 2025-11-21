//
// Created by Nico Cevallos on 11/15/25.
//

#ifndef PRICER_H
#define PRICER_H
#include <string>

enum class PricerType {
	BinomialTree, MonteCarlo
};

class Pricer {
public:
	Pricer(int paths, double timeStep, double discount, PricerType type);
	virtual ~Pricer() = default;
	virtual void priceIndependent(std::vector<std::vector<double>> &vector, double start, int step) = 0;
	PricerType identify();
	virtual void setup(double vol, double drift) = 0;
	virtual double getProb() = 0;

	double getTimeStep() const;
	double getDiscount() const;

protected:
	PricerType pricerType;
	int paths;
	double timeStep;
	double r;
};

#endif //PRICER_H
